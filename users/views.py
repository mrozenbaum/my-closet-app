from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse




def logout_view(request):
    """ log the user out """
    logout(request)
    return HttpResponseRedirect(reverse('closetclient:index'))


def signup(request):
    """ register a new user """
    if request.method != 'POST':
        # display blank registration form
        form = UserCreationForm()
    else:
        # process completed forms    
        if form.is_valid():
            new_user = form.save()
            # log the user in and redirect them to the index
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)

            return HttpResponseRedirect(reverse('closetclient:index'))
    context = {'form':form}        

    return render(request, 'users/signup.html', context)