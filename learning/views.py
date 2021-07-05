from learning.models import Student
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import ProfileForm,UserForm,EnterpriseForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("<h1>Logged In</h1>")
            message="Incorrect Credentials"
            form=UserForm()
        return render(request, 'learning/login.html', {'form':form,"message":message})
            
    else:
        form = UserForm()
        return render(request, 'learning/login.html', {'form':form})


def login_view(request):
    if request.method=="POST":
        print(request.POST)
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("form valid")
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print(username,password)
            # user=User.objects.filter(username=username)[0]
            if user is not None:
                print("verified")
                login(request,user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request,"uno_startup/login.html",{"form":form})  
    

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        profileform = ProfileForm(request.POST, request.FILES)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            profile = profileform.save(user)
            return HttpResponse("<h1>Signed Up</h1>")
        #for dev
        else:
            raise Exception (f"Profile form not valid {profileform}")
    else:
        userform = UserForm()
        profileform = ProfileForm()
    return render(request, 'learning/signup.html', {'userform':userform, 'profileform':profileform})

@csrf_exempt
def signupEnterprise(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        enterpriseform = EnterpriseForm(request.POST)
        if userform.is_valid() and enterpriseform.is_valid():
            user = userform.save()
            enterprise = enterpriseform.save(user)
            return HttpResponse("<h1>Signed Up</h1>")
        else:
            print(enterpriseform.data)
            raise Exception (f"Profile form not valid {enterpriseform.is_valid()}")
    else:
        enterprise = EnterpriseForm()
        user = UserForm()
        return render(request, 'learning/signup_enterprise.html', {'enterprise':enterprise, 'user':user})
