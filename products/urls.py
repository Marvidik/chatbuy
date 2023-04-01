from django.urls import path
from .views import product_delete,add_product,admin_dashboard,ProductUpdateView,SearchResultsView,products,add_to_cart,increment,checkout,HomeResultsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',products,name="home"),
   path('dashboard/',admin_dashboard,name="dash"),
   path('add/',add_product,name="padd"),
   path("delete/<int:id>/",product_delete,name="delete"),
   path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
   path("search/",SearchResultsView.as_view(template_name="products/products.html"),name="search"),
   path("home_search/",HomeResultsView.as_view(template_name="products/indexE.html"),name="hsearch"),
   path("addcart/<product_id>",add_to_cart,name="cart_add"),
   path("increment/<cart_id>",increment,name="increment"),
   path("checkout/",checkout,name="checkout")
]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


