from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

#     def register(request):
#         registered = False
#         if request.method == 'POST':
#             user_form = UserRegisterForm(data=request.POST)
#             profile_form = ProfileUpdateForm(data=request.POST)
#
#             if user_form.is_valid() and profile_form.is_valid():
#                 user = user_form.save()
#                 user.set_password(user.password)
#                 user.save()
#                 profile = profile_form.save(commit=False)
#                 profile.user = user
#                 if 'picture' in request.FILES:
#                     profile.picture = request.FILES['picture']
#                 profile.save()
#                 registered = True
#             else:
#                 print(user_form.errors, profile_form.errors)
#
#         else:
#             user_form = UserRegisterForm()
#             profile_form = ProfileUpdateForm()
#         return render(request, 'users/register.html',
#                       {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
#
#
#     def user_login(request):
#
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect(reverse('home'))
#                 else:
#                     return HttpResponse("Your eSports account is disabled.")
#             else:
#                 print("Invalid login details: {0}, {1}".format(username, password))
#                 return HttpResponse("Invalid login details supplied.")
#         else:
#             return render(request, 'registration/login.html', {})
#
#     @login_required
#     def user_logout(request):
#         logout(request)
#         return redirect(reverse('auth_login'))
@login_required
def register_profile(request):
    form = ProfileUpdateForm()

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('home')
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'contest/profile_registration.html', context_dict)


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        userprofile = Profile.objects.get_or_create(user=user)[0]
        form = ProfileUpdateForm()

        return user, userprofile, form

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, userprofile, form) = self.get_user_details(username)
        except TypeError:
            return redirect('home')

        context_dict = {'userprofile': userprofile,
                        'selecteduser': user,
                        'form': form}

        return render(request, 'contest/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, userprofile, form) = self.get_user_details(username)
        except TypeError:
            return redirect('home')

        form = ProfileUpdateForm(request.POST, request.FILES, instance=userprofile)

        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

        context_dict = {'userprofile': userprofile,
                        'selecteduser': user,
                        'form': form}

        return render(request, 'contest/profile.html', context_dict)



class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
        profiles = Profile.objects.all()
        return render(request,
                      'contest/list_profiles.html', {'userprofile_list': profiles})