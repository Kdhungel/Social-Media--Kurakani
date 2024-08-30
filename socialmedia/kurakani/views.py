from django.shortcuts import render
from .models import Kurakani
from .forms import KurakaniForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.

def index(request):
    return render(request, 'index.html')

#list view
def kurakani_list(request):
    kurakanis = Kurakani.objects.all().order_by('-created_at')
    return render(request, 'kurakani_list.html', {'kurakanis': kurakanis})

# create
@login_required
def kurakani_create(request):
    if request.method == "POST":
       form = KurakaniForm(request.POST, request.FILES) # accepts user filled form and files also.
       if form.is_valid(): # validation
           kurakani = form.save(commit = False) # donot save in db yet
           kurakani.user = request.user # there is user in every request
           kurakani.save() # saved in db
           return redirect('kurakani_list')

    else:
        form = KurakaniForm()
    return render(request, "kurakani_form.html", {'form': form})

#edit
@login_required
def kurakani_edit(request, kurakani_id):
    kurakani = get_object_or_404(Kurakani, pk= kurakani_id, user = request.user)
    if request.method == 'POST':
        form = KurakaniForm(request.POST, request.FILES, instance= kurakani) 
        if form.is_valid(): 
            kurakani = form.save(commit = False) 
            kurakani.user = request.user 
            kurakani.save() 
            return redirect('kurakani_list')
    else:
        form = KurakaniForm(instance=kurakani) # pre filled data to edit
    return render(request, "kurakani_form.html", {'form': form})


# delete
@login_required
def kurakani_delete(request, kurakani_id):
    kurakani = get_object_or_404(Kurakani, pk= kurakani_id, user = request.user)
    if request.method == "POST":
        kurakani.delete()
        return redirect('kurakani_list')
    return render(request, "kurakani_confirm_delete.html", {'kurakani': kurakani})

def register(request):
    if request.method == 'POST':
       form = UserRegistrationForm(request.POST)
       if form.is_valid():
           user = form.save(commit= False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(request, user)
           return redirect('kurakani_list')
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {'form': form})