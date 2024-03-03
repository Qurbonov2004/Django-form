# views.py
from django.shortcuts import render, redirect
from .forms import UserForm

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Ma'lumotlar saqlangan so'ng success sahifasiga yo'naltirish
    else:
        form = UserForm()

    return render(request, 'create_user.html', {'form': form})
