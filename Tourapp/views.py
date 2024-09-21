from rest_framework import generics
from .models import TouristDestination
from .serializers import TouristDestinationSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView
from .forms import DestinationForm
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.views import View
from django.utils.decorators import method_decorator
#@login_required use for security



class DestinationListCreate(generics.ListCreateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

# Retrieve, Update and Delete View

class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer


def destination_list(request):
    destinations = TouristDestination.objects.all()
    return render(request, 'destination_list.html', {'destinations': destinations})

# Create and Update View
@login_required
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('destination-list'))
    else:
        form = DestinationForm()
    return render(request, 'destination_form.html', {'form': form, 'title': 'Add Destination'})

# Update a destination
@login_required
def destination_update(request, pk):
    destination = get_object_or_404(TouristDestination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect(reverse('destination-list'))
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'destination_form.html', {'form': form, 'title': 'Edit Destination'})

# Delete a destination
@login_required
def destination_delete(request, pk):
    destination = get_object_or_404(TouristDestination, pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect(reverse('destination-list'))
    return render(request, 'destination_confirm_delete.html', {'destination': destination})

def index(request):
    return render(request,'index.html')
def index2(request):
    return render(request,'index2.html')



class DestinationDetailView(DetailView):
    model = TouristDestination
    template_name = 'destination_detail.html'
    context_object_name = 'destination'







class DestinationListView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        destinations = TouristDestination.objects.all()

        if search_query:
            destinations = destinations.filter(place_name__icontains=search_query)

        context = {
            'destinations': destinations
        }
        return render(request, 'destination_list.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the new user and hash the password automatically
            user = form.save()
            # Extract the username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get(
                'password1')  # It's password1 because UserRegistrationForm usually has two fields (password1 and password2).

            # Authenticate the user using the provided credentials
            user = authenticate(username=username, password=password)

            # If authentication is successful, log the user in
            if user is not None:
                login(request, user)
                # Redirect to a specific page (like the destination list)
                return redirect('destination-list')
    else:
        form = UserRegistrationForm()  # Instantiate an empty form

    # If form submission fails or it's a GET request, render the registration page with the form
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        # Extract the username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # If authentication is successful, log the user in
        if user is not None:
            login(request, user)
            # Redirect to the destination list page after login
            return redirect('destination-list')
        else:
            # Handle login failure (wrong username/password)
            error_message = "Invalid username or password."
            return render(request, 'registration/login.html', {'error': error_message})

    # If it's a GET request, just render the login page
    return render(request, 'registration/login.html')


def user_logout(request):
    logout(request)
    return redirect('user-login')  # Change to your login URL
