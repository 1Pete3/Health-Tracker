import motivation as motivation
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_lifts, name='home_lifts'),
    path('edit/<int:id>', views.edit_lift, name='edit'),
    path('add-lift', views.create_lift, name='create_lift'),
    path('delete-lift/<int:id>', views.delete_lift, name='delete_lift'),
    path('edit-lift/<int:id>', views.edit_lift, name='edit_lift'),
    # Nutrition paths
    path('nutrition', views.home_nutrition, name='home_nutrition'),
    path('add-food', views.create_food, name='create_food'),
    path('delete-food/<int:id>', views.delete_food, name='delete_food'),
    path('edit-food/<int:id>', views.edit_food, name='edit_food'),
    # Motivation path
    path('motivation', views.motivation, name='motivation'),
    # Weight Paths
    path('weight', views.home_weight, name='home_weight'),
    path('add-weight', views.add_weight, name='add_weight'),
    path('delete-weight/<int:id>', views.delete_weight, name='delete_weight'),
    path('edit-weight/<int:id>', views.edit_weight, name='edit_weight'),
    # Register Path
    path('register', views.register_view, name="register"),
    # Login Path
    path('login', views.login_view, name="login"),
    # Logout Path
    path('logout', views.logout_view, name="logout"),



]
