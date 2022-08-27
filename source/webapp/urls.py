from django.conf.urls.static import static
from django.urls import path

from webapp.views.products import IndexView, ProductView, CreateProduct, UpdateProduct, DeleteProduct
from newPro import settings

app_name = "webapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/<int:pk>/", ProductView.as_view(), name="detail_view"),
    path("product/new/", CreateProduct.as_view(), name="create_product"),
    path("product/<int:pk>/update/", UpdateProduct.as_view(), name="update_product"),
    path("product/<int:pk>/delete/", DeleteProduct.as_view(), name="delete_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)