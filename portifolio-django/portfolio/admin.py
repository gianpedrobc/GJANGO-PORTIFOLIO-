from django.contrib import admin

# Register your models here.
from .models import Skill, Projeto, Certificado, SobreMim, Apresentacao

admin.site.register(Apresentacao)
admin.site.register(Skill)
admin.site.register(Projeto)
admin.site.register(Certificado)
admin.site.register(SobreMim)
