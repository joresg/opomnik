""" vews file for wall app """
from django.shortcuts import render, redirect
from django.http import HttpResponse
from wall.models import Objava, IzbrisanaObjava

# Create your views here.

def wall(request):
    """ homepage """
    return render(request, 'wall.html', {'objave':Objava.objects.all()})

def add(request):
    """ metoda za dodajanje nove objave """
    nova_objava = Objava(tekst=request.POST['nova_objava'])
    nova_objava.save()
    return redirect('/')

def delete_all(request):
    """ izbrisi vse objave """
    for i in Objava.objects.all():
        prestavi = IzbrisanaObjava(tekst=i)
        prestavi.save()
        i.delete()
    return redirect('/')

def delete_all_final(request):
    """ izbrisi vse objave """
    for i in IzbrisanaObjava.objects.all():
        i.delete()
    return render(request, 'deleted.html')

def delete(request):
    """ izbrisi izbrano objavo """
    #for pozicija, i in enumerate(Objava.objects.all()):
    for i in Objava.objects.all():
        if request.POST.get(str(i.id), "dont_delete") != "dont_delete":
            #prestavi jo med izbrisane in jo potem izbrisi
            prestavi = IzbrisanaObjava(tekst=i)
            prestavi.save()
            i.delete()
    return redirect('/')

def deleted(request):
    """ poglej izbrisane objave in
    jih po zelji dokoncno izbrisi """
    izbrisane_objave = IzbrisanaObjava.objects.all()
    return render(request, 'deleted.html', {'izbrisane_objave':izbrisane_objave})

def edit(request):
    """ posodobi objavo na serverju """
    haha = request.POST['new_post']
    id_objave1 = request.POST['id_objave']
    #id_objave = int(id_objave1)
    for objava in Objava.objects.all():
        if str(objava.id) == id_objave1:
            objava.tekst = haha
            objava.save()
            break
    return redirect('/')

def ajax_update_posts(request):
    """ funkcija za posodobit stran brez osvezevanja """
    odziv = ''
    for objava in Objava.objects.all():
        odziv = odziv + objava.tekst + ':' + str(objava.id) + '&'
    return HttpResponse(odziv[0:len(odziv)-1])
