from django.urls import path, include
from .views import *

urlpatterns = [
   # path('reg/', reg),
   # path('reg/register/', register, name='register'),
   # path('reg/spikers/', spikers, name='spikers'),
   # path('reg/guests/', guests, name='guests'),
   # path('reg/login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('signup/', SignUpView.as_view(), name='signup'),
   # path('home/', get_num, name='home'),

    path('rand/', get_num, name='randomizer'),



]