from django.contrib import admin
from django.urls import path
from sports import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('',views.home,name='home'),
    path('badminton/',views.badminton,name='badminton'),
    path('cricket/',views.cricket,name='cricket'),
    path('football/',views.football,name='football'),
    path('basketball/',views.basketball,name='basketball'),

    path('checkout/',views.checkout,name='checkout'),
    path('aboutus/',views.aboutus,name='about'),
    path('buy/', views.buynow, name='buy-now'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('pluscart/',views.plus_cart, name='pluscart'),
    path('minuscart/',views.minus_cart, name='minuscart'),
    path('removecart/',views.remove_cart, name='removecart'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='sports/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('SignUp/', views.CustomerRegistrationView.as_view(), name='signup'),

    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),
    path('address/', views.address, name='address'),

    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='productdetail'),

    path('menaccessories/',views.men_accss,name='men_accss'),
    path('menfoot/',views.men_foot,name='men_foot'),
    path('mencloth/',views.men_cloth,name='men_cloth'),
    path('meninfo/',views.men_info,name='men_info'),

    path('womenaccessories/',views.women_accss,name='women_accss'),
    path('womenfoot/',views.women_foot,name='women_foot'),
    path('womencloth/',views.women_cloth,name='women_cloth'),
    path('womeninfo/',views.women_info,name='women_info'),

    path('kidsaccessories/',views.kids_accss,name='kids_accss'),
    path('kidsfoot/',views.kids_foot,name='kids_foot'),
    path('kidscloth/',views.kids_cloth,name='kids_cloth'),
    path('kidsinfo/',views.kids_info,name='kids_info'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='sports/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'), name='passwordchange'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='sports/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='sports/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='sports/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='sports/password_reset_complete.html'), name='password_reset_complete'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='sports/passwordchangedone.html'), name='passwordchangedone'),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)