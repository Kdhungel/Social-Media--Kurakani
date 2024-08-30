from django.shortcuts import render
from .models import Kurakani
from .forms import KurakaniForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

#list view
def kurakani_list(request):
    kurakanis = Kurakani.objects.all().order_by('-created_at')
    return render(request, 'kurakani_list.html', {'kurakanis': kurakanis})

# create
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
def kurakani_delete(request, kurakani_id):
    kurakani = get_object_or_404(Kurakani, pk= kurakani_id, user = request.user)
    if request.method == "POST":
        kurakani.delete()
        return redirect('kurakani_list')
    return render(request, "kurakani_confirm_delete.html", {'kurakani': kurakani})
    