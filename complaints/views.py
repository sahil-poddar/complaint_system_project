from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Complaint
from .forms import ComplaintForm

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complaint submitted successfully.')
            return redirect('submit_complaint')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/complaint_form.html', {'form': form})

def complaint_list(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    complaints = Complaint.objects.all().order_by('-created_at')
    if query:
        complaints = complaints.filter(
            Q(name__icontains=query) | Q(subject__icontains=query) | Q(email__icontains=query)
        )
    if status_filter:
        complaints = complaints.filter(status=status_filter)
    return render(request, 'complaints/complaint_list.html', {
        'complaints': complaints, 'query': query, 'status_filter': status_filter
    })

def update_status(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    complaint.status = 'Solved' if complaint.status == 'Pending' else 'Pending'
    complaint.save()
    return redirect('complaint_list')

def delete_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    complaint.delete()
    messages.success(request, 'Complaint deleted.')
    return redirect('complaint_list')