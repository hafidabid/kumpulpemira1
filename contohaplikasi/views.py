from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from . import models
# Create your views here.

def home(request):
    
    if(request.method=="POST"):
        email = request.POST["email"]
        pswd = request.POST["password"]
        hitung = 1+20
        if(pswd=="abc123"):
            kal = "ini emailmu tadi "+email
            arr = ["hafid","andiko","fawwaz","alif","julian","berhasil masuk semua"]
            request.session["aktif"] = 1
        else:
            kal = "salah password"
            arr = ["salah bosq","salah bosq","salah bosq"]
        
    else:
        if ('aktif' in request.session and request.session["aktif"] == 1) :
            hitung = 100
            kal = "sudah login borr"
            arr = ["hafid","andiko","fawwaz","alif","julian","berhasil masuk semua"]

        else :
            hitung = -1
            kal = "belum login"
            arr = models.StaffIT.objects.all()
    
    sess = 0
    if 'aktif' in request.session:
        if (request.session["aktif"] == 1): sess = 1

    return render(request, "index.html", {
        "angka" : hitung,
        "kata" : "burung bangau",
        "kalimat" : kal,
        "arai" : arr,
        "sesion" : sess
    })

def cobalagi(request):
    return HttpResponse('<p style="color:green">cobalagii</p>')

def keluar(request):
    if 'aktif' in request.session:
        request.session['aktif'] = 0
    return redirect('home')

def member(request):
    hitung = models.StaffIT.objects.all().count()

    if request.method=="POST":
        nama = request.POST["nama"]
        fak = request.POST["fakultas"]
        angkatan = request.POST["angkatan"]

        newStaffIT = models.StaffIT(hitung+1,nama,fak,angkatan)
        newStaffIT.save()
    
    return redirect('home')

