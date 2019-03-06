from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def proposal(request):
    context = {}
    return render(request, 'chris_design/proposal.html', context)

@login_required()
def wireframe(request):
    context = {}
    return render(request, 'chris_design/wireframe.html', context)