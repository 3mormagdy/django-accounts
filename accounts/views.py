from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST': ## save
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')

    else: ## show form
        form = SignupForm

    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST': # save
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myform = profileform.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')

    else: # show
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request, 'profile/profile_edit.html', {
        'userform': userform,
        'profileform': profileform,
    })
    
