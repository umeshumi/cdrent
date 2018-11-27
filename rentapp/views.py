from django.shortcuts import render, redirect
from .models import Product, Rent
from .forms import ProductForm, RentForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def homePage(request):
	productss = Product.objects.all()
	context = {'products': productss}
	return render(request, 'home.html', context)


@user_passes_test(lambda u: u.is_superuser)

def AddNewitem(request):
	 if request.method == "POST":
	 	form = ProductForm(request.POST, request.FILES)
	 	if form.is_valid():
	 		form.save()
	 		return redirect('rentapp:home')
	 else:
	 	form = ProductForm()
	 return render(request, 'addproduct.html', {'form': form})


@login_required
def Rented(request, productid):
	try:
		productss = Product.objects.get(id=productid)
	except Product.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		form = RentForm(request.POST)
		if form.is_valid():
			Product.objects.filter(pk=productid).update(Rented=True)
			Product.objects.filter(pk=productid).update(Returned=False)
			


			selected_days = form.cleaned_data['days']
			rents = form.save(commit=False)
			rents.product = productss
			rents.user = request.user
			rents.actived =True
			total = selected_days*productss.Rent_Price
			rents.save()
			
			return render(request, 'confirm.html', {'total':total})
	else:
		form = RentForm()
	context = {'product':productss, 'form':form}
	return render(request, 'rent.html', context)


@login_required
def Cart(request):
	rents = Rent.objects.filter(user__username=request.user, actived=True)
	context = {'rents':rents}
	return render(request, 'cart.html', context)

@login_required
def ReturnCD(request, rentid):
	productss = Product.objects.all()
	rents = Rent.objects.get(id=rentid)
	if rents.user == request.user:
		Rent.objects.filter(pk=rentid).update(actived=False)
		Product.objects.filter(pk=rents.product.id).update(Rented=False)
		Product.objects.filter(pk=rents.product.id).update(Returned=True)
		context = {'products': productss}
		return render(request, 'home.html', context)
	else:
		raise Http404

@login_required
def History(request):
	rents = Rent.objects.filter(user__username=request.user)
	context = {'rents':rents}
	return render(request, 'history.html', context)

def logoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse('rentapp:home'))



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('rentapp:home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})