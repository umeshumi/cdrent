from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView

app_name = 'rentapp'

urlpatterns=[
	path('',views.homePage, name='home'),
	path('addnew/',views.AddNewitem, name='addnew'),
	path('cart/',views.Cart, name='cart'),
	path('history/',views.History, name='history'),
	path('rent/<int:productid>',views.Rented, name='rent'),
	path('cart/<int:rentid>',views.ReturnCD, name='returnedcd'),
	path('logout/', views.logoutView, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('login/',LoginView.as_view(template_name='login.html'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)