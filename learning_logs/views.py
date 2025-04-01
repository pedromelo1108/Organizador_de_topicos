from django.shortcuts import render
from .models import Topic

def index(request):
    """Página principal do Learning_Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos"""
    topic = Topic.objects.order_by('date_added')
    context = {'topics': topics}