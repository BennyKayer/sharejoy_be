# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# First Party
from sharejoy import views

router = DefaultRouter()
router.register("items", views.ItemViewSet)
router.register("categories", views.CategoryViewSet)

app_name = "sharejoy"

urlpatterns = [
    path("", include(router.urls)),
    path("create_user/", views.CreateUserView.as_view(), name="create"),
    path("get_token/", views.CreateTokenView.as_view(), name="token"),
    path("my_details/", views.ManageUserView.as_view(), name="me"),
]
