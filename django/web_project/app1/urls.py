from django.urls import path, include
from .views import *

urlpatterns = [
   # path('reg/', reg),
   # path('reg/register/', register, name='register'),
   # path('reg/spikers/', spikers, name='spikers'),
   # path('reg/guests/', guests, name='guests'),
   # path('reg/login/', user_login, name='user_login'),
    path('accounts/', include('django.contrib.auth.urls')),
   # path('accounts/', include('accounts.urls')),
   # path('login/', user_login, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('rand/', get_num, name='randomizer'),



]