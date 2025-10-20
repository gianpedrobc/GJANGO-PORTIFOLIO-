from django.shortcuts import render
from .models import Skill, Projeto, Certificado, SobreMim, Apresentacao

def index(request):
    apresentacao = Apresentacao.objects.first()
    skills = Skill.objects.all()
    projetos = Projeto.objects.all()
    certificados = Certificado.objects.all()
    sobre = SobreMim.objects.first()
    return render(request, 'index.html', {
        'apresentacao':apresentacao,
        'skills': skills,
        'projetos': projetos,
        'certificados': certificados,
        'sobre': sobre,
    })

