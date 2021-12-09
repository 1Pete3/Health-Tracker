from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LiftForm, NutritionForm, WeightForm, CreateUserForm
from .models import Lift, Nutrition, Weight
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Views for the lift page
def home_lifts(request):
    lift = Lift.objects.all()
    return render(request, 'home-lift.html', {'lift': lift})

@login_required(login_url='login')
def create_lift(request):
    form = LiftForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_lifts')
    return render(request, 'create-lift.html', {'form': form})


@login_required(login_url='login')
def delete_lift(request, id):
    lift = Lift.objects.get(id=id)
    if request.method == 'POST':
        lift.delete()
        return redirect('home_lifts')
    return render(request, 'delete-lift.html', {'lift': lift})


@login_required(login_url='login')
def edit_lift(request, id):
    lift = Lift.objects.get(id=id)
    form = LiftForm(request.POST or None, instance=lift)
    if form.is_valid():
        form.save()
        return redirect('home_lifts')
    return render(request, 'edit-lift.html', {'form': form, 'lift': lift})


# Views for the Nutrition page
def home_nutrition(request):
    nutrition = Nutrition.objects.all()
    return render(request, 'home-nutrition.html', {'nutrition': nutrition})


@login_required(login_url='login')
def create_food(request):
    form = NutritionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_nutrition')
    return render(request, 'create-food.html', {'form': form})

@login_required(login_url='login')
def delete_food(request, id):
    food = Nutrition.objects.get(id=id)
    if request.method == 'POST':
        food.delete()
        return redirect('home_nutrition')
    return render(request, 'delete-nutrition.html', {'food': food})


@login_required(login_url='login')
def edit_food(request, id):
    food = Nutrition.objects.get(id=id)
    form = NutritionForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        return redirect('home_nutrition')
    return render(request, 'edit-nutrition.html', {'form': form, 'food': food})


# View for Dynamic page
def motivation(request):
    return render(request, 'motivation.html')


# View for Weight
def home_weight(request):
    weight = Weight.objects.all()
    return render(request, 'home-weight.html', {'weight': weight})


@login_required(login_url='login')
def add_weight(request):
    form = WeightForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_weight')
    return render(request, 'add-weight.html', {'form': form})


@login_required(login_url='login')
def delete_weight(request, id):
    # Get the product based on its id
    weight = Weight.objects.get(id=id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        weight.delete()
        # after deleting redirect to view_product page
        return redirect('home_weight')

    # if the request is not post, render the page with the product's info
    return render(request, 'delete-weight.html', {'weight': weight})


@login_required(login_url='login')
def edit_weight(request, id):
    weight = Weight.objects.get(id=id)
    form = WeightForm(request.POST or None, instance=weight)
    if form.is_valid():
        form.save()
        return redirect('home_weight')
    return render(request, 'edit-weight.html', {'form': form, 'weight': weight})


# View for Register
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home_lifts')
    else:
        # This function renders the registration form page and create a new user based on the form data
        if request.method == 'POST':
            # We use Django's UserCreationForm which is a model created by Django to create a new user.
            # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
            form = CreateUserForm(request.POST)
            # check whether it's valid: for example it verifies that password1 and password2 match
            if form.is_valid():
                form.save()
                # redirect the user to login page so that after registration the user can enter the credentials
                messages.success(request, 'Account Creation Successful')
                return redirect('login')
        else:
            # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.

            form = CreateUserForm()
        return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_lifts')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('home_lifts')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(login_view)
