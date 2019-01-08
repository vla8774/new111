from django.shortcuts import render, redirect


def home(request):

   # if request.user.is_authenticated:

        #return redirect("home_account")

    return render(request, 'home.html')


#def home_account(request):

   # return render(request, 'home_account.html')
