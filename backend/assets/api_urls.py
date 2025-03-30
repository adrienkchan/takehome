from django.urls import path
from .views import asset_list, asset_show

urlpatterns = [
    path("", asset_list, name="list_create_assets"),
    path("<int:pk>/", asset_show, name="get_del_put_asset"),
]
