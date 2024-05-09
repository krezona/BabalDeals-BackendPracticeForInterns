from django.urls import path

from .views import CutsomUserCreate, BlacklistTokenView


app_name = 'users'

urlpatterns = [
    path('register/', CutsomUserCreate.as_view(), name ="create_user"),

    path('logout/blacklist/', BlacklistTokenView.as_view(),
         name = "blacklist"
         )
]