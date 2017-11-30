from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext

from principal.forms import *
from principal.models import *


# from django.core.mail import EmailMessage
def inicio(request):
    autenticado = False
    profesor = False
    user = request.user
    if request.user.is_authenticated():
        autenticado = True
        try:
            Profesor.objects.get(usuario_id=request.user.id)
            profesor= True
        except:
            pass
    tfgs = TFG.objects.all()
    return render_to_response("inicio.html", {'tfgs':tfgs, 'auth':autenticado, 'profesor':profesor, 'usuario':user})

def real_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        formulario = LogInForm(request.POST)
        if formulario.is_valid():
            user = authenticate(username=formulario.cleaned_data['user'], password=formulario.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = 'Usuario o Password incorrectos'
                return render_to_response('login.html',{'formulario':formulario, 'error':error}, context_instance=RequestContext(request)) 
    else:
        formulario = LogInForm()
    
    return render_to_response('login.html',{'formulario':formulario}, context_instance=RequestContext(request))

def real_signin(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        formulario = AlumnoForm(request.POST, request.FILES)
        if formulario.is_valid():
            if formulario.cleaned_data['password']==formulario.cleaned_data['password2']:
                usuario = User.objects.create_user(formulario.cleaned_data['user'], formulario.cleaned_data['email'], formulario.cleaned_data['password'])
                Alumno.objects.create(usuario=usuario, nombre=formulario.cleaned_data['nombre'], apellidos=formulario.cleaned_data['apellidos'],
                                           universidad=formulario.cleaned_data['universidad'], titulacion=formulario.cleaned_data['titulacion'])
                return HttpResponseRedirect('/login')
            else:
                error = "Las password no coinciden"
                return render_to_response('signin.html',{'formulario':formulario, 'error':error}, context_instance=RequestContext(request))
    else:
        formulario = AlumnoForm()
    return render_to_response('signin.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def profesor_signin(request):
    try:
        Profesor.objects.get(usuario_id=request.user.id)
    except:
        return HttpResponseRedirect('/')
    if request.method=='POST':
        formulario = ProfesorForm(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = User.objects.create_user(formulario.cleaned_data['user'], formulario.cleaned_data['email'], formulario.cleaned_data['password'])
            Profesor.objects.create(usuario=usuario, nombre=formulario.cleaned_data['nombre'], apellidos=formulario.cleaned_data['apellidos'],
                                       universidad=formulario.cleaned_data['universidad'], departamento=formulario.cleaned_data['departamento'])
            return HttpResponseRedirect('/')
    else:
        formulario = ProfesorForm()
    return render_to_response('signin.html',{'formulario':formulario}, context_instance=RequestContext(request))

def real_logout(request):
    logout(request)
#     autenticado = 0
    tfgs = TFG.objects.all()
    return render_to_response("inicio.html", {'tfgs':tfgs, 'auth':False})

@login_required(login_url='/login')
def create_tfg(request):
    try:
        Profesor.objects.get(usuario_id=request.user.id)
    except:
        return HttpResponseRedirect('/')
    if request.method=='POST':
        formulario = TFGForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = TFGForm()
    return render_to_response('tfg.html',{'formulario':formulario}, context_instance=RequestContext(request))
    
def lista_tfgs(request):
    tfgs = TFG.objects.all()
    return render_to_response("lista_tfgs.html", {'tfgs':tfgs})

def busca_tfgs(request):
    if request.method=='POST':
        formulario = SearchForm(request.POST)
        if formulario.is_valid():
            tfgs = TFG.objects.filter(titulacion=formulario.cleaned_data['titulacion'])
            return render_to_response('lista_tfgs.html',{'tfgs':tfgs})
    else:
        formulario = SearchForm()
    return render_to_response('search.html',{'formulario':formulario}, context_instance=RequestContext(request))
