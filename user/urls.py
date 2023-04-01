from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import all_reg,Login,forget_password,password_reset_request,vendor_dashboard,customer_dashboard,logoutuser,notification,super_user,update_status,remove,details

urlpatterns = [
   path('vendor/dashboard/',vendor_dashboard,name="vdash"),
   path('dashboard/',customer_dashboard,name="cdash"),
   path('product/approve/<pk>',update_status,name="status"),
   path('product/remove/<pk>',remove,name="remove"),
   path('super_admin/',super_user,name="super"),
   path('register/',all_reg,name="vreg"),
   path('notification/',notification,name="notification"),
   path('login/',Login.as_view(),name="login"),
   path('logout/',logoutuser,name="logout"),
   path('forgot_password',forget_password,name="forgotpassword"),
   path("password_reset", password_reset_request, name="password_reset"),
   path("details/<pk>/",details,name="detail"),
]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)