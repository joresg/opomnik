""" vews file for wall app """
from django.shortcuts import render, redirect
from django.http import HttpResponse
from wall.models import Objava, IzbrisanaObjava
from django.contrib.auth.models import User, auth

# Create your views here.

def wall(request):
    """ homepage """
    return render(request, 'wall.html', {'objave':Objava.objects.filter(created_by=request.user)})

def add(request):
    """ metoda za dodajanje nove objave """
    nova_objava = Objava(tekst=request.POST['nova_objava'], created_by=request.user)
    nova_objava.save()
    return redirect('/wall')

def delete_all(request):
    """ izbrisi vse objave """
    for i in Objava.objects.filter(created_by=request.user):
        prestavi = IzbrisanaObjava(tekst=i, created_by=i.created_by)
        prestavi.save()
        i.delete()
    return redirect('/wall')

def delete_all_final(request):
    """ izbrisi vse objave """
    for i in IzbrisanaObjava.objects.filter(created_by=request.user):
        i.delete()
    return render(request, 'deleted.html')

def delete(request):
    """ izbrisi izbrano objavo """
    #for pozicija, i in enumerate(Objava.objects.all()):
    for i in Objava.objects.filter(created_by=request.user):
        if request.POST.get(str(i.id), "dont_delete") != "dont_delete":
            #prestavi jo med izbrisane in jo potem izbrisi
            prestavi = IzbrisanaObjava(tekst=i, created_by=i.created_by)
            prestavi.save()
            i.delete()
    return redirect('/wall')

def deleted(request):
    """ poglej izbrisane objave in
    jih po zelji dokoncno izbrisi """
    izbrisane_objave = IzbrisanaObjava.objects.filter(created_by=request.user)
    return render(request, 'deleted.html', {'izbrisane_objave':izbrisane_objave})

def edit(request):
    """ posodobi objavo na serverju """
    haha = request.POST['new_post']
    id_objave1 = request.POST['id_objave']
    #id_objave = int(id_objave1)
    for objava in Objava.objects.filter(created_by=request.user):
        if str(objava.id) == id_objave1:
            objava.tekst = haha
            objava.save()
            break
    return redirect('/wall')

def ajax_update_posts(request):
    """ funkcija za posodobit stran brez osvezevanja """
    odziv = ''
    for objava in Objava.objects.filter(created_by=request.user):
        odziv = odziv + objava.tekst + ':' + str(objava.id) + '&'
    return HttpResponse(odziv[0:len(odziv)-1])

def start_page(request):
    """ start page za prijavo ali registracijo """
    return render(request, 'start_page.html')

def register(request):
    
    if request.method == 'POST':
        uname = request.POST["uname"]
        mail = request.POST["mail"]
        passwd1 = request.POST["passwd1"]
        passwd2 = request.POST["passwd2"]

        if passwd1 == passwd2:
            if User.objects.filter(username=uname).exists():
                print("username taken")
            elif User.objects.filter(email=mail).exists():
                print("email already registered")
            else:
                user = User.objects.create_user(username=uname, password=passwd1, email=mail)
                user.save()
                print("user "+uname+" added")
        else:
            print("gesli se ne ujemata")

    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST["uname"]
        password = request.POST["passwd"]

        #return HttpResponse("hello "+username)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/wall')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)

    return redirect('/')






