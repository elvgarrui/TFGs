from principal.models import *
from django.contrib.auth.models import User
from django.core.management import call_command


def principal():
    call_command('flush', interactive=False)
    call_command('syncdb', interactive=False)

    usuario = User.objects.create_user('admin', 'admin@admin.es', 'admin')
    Profesor.objects.create(usuario=usuario, nombre='Admin', apellidos='Admin Admin', universidad='Universidad de Sevilla', departamento='LSI')

if __name__ == '__main__':
    principal()
