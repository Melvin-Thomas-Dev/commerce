from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listings/<int:pk>/", views.bid_view, name="detail"),
    # path("listings/<int:pk>/bid", views.bid_view, name="bid"),

]
