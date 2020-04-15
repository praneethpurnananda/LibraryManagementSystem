from django.conf.urls import url
from first_app import views


urlpatterns = [
 url(r'^first_app/',views.index,name='index'),
 url(r'^cs/',views.cs,name='cs'),
url(r'^program/',views.program,name='program'),
    url(r'^allbooks/',views.allbooks,name='allbooks'),
    url(r'^mech/',views.mech,name='mech'),
    url(r'^history/',views.history,name='history'),
    url(r'^ece/',views.ece,name='ece'),
]
