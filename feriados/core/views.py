from django.shortcuts import render
from datetime import today
dataatual= datetime.today
def natal(request):
 contexto = {'natal': True,
 'carnaval': False}
 return render(request, 'natal.html', contexto)
def tiradentes(request):
  contexto = {'tiradentes':True, 'pascoa':False}
  return render(request,'tiradentes.html', contexto)
