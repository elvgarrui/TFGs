from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TFGs.views.home', name='home'),
    # url(r'^TFGs/', include('TFGs.foo.urls')),
    
    url(r'^$','principal.views.inicio'),
    url(r'^login/$','principal.views.real_login'),
    url(r'^logout/$','principal.views.real_logout'),
    url(r'^signin/$','principal.views.real_signin'),
    url(r'^signinprofesor/$','principal.views.profesor_signin'),
    url(r'^creatfg/$','principal.views.create_tfg'),
    url(r'^listatfgs/$','principal.views.lista_tfgs'),
    url(r'^search/$','principal.views.busca_tfgs'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
