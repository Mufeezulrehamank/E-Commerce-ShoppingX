from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="productview"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('electronics/<slug:data>/', views.electronics, name='electronics'),
    path('electronics/', views.electronics, name='electronicsdata'),    
    path('registration/', views.RegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/login.html",form_class=LoginForm,), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),   
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name="app/changepassword.html", form_class=MyPasswordChangeForm, success_url = "/mychangepassworddone/"), name='changepassword'),
    path('mychangepassworddone/', auth_views.PasswordChangeDoneView.as_view(template_name="app/home.html"), name='changepassworddone'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('address/', views.Address.as_view(), name='address'),

    path('showcart/', views.show_cart, name='show-cart'),
    path('cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('plus_cart/', views.plus_cart, name='plus_cart'),

    path('buy/', views.buy_now, name='buy-now'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
