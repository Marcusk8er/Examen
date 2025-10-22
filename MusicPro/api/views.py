from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from api.models import Cliente

# Create your views here.
def registro(request):
    context = {}
    if request.POST:
        form = Cliente(request.POST)
        if form.is_valid():
            user = form.save( commit = False)
            user.save()
            group = Group.objects.get( name = 'Cliente')
            user.groups.add(group)
            return redirect('index')
        else:
            context['registro'] = form
    else:
        form = Cliente()
        context['registro'] = form
    return render(request, 'register.html', context)