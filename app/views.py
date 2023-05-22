from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
# Create your views here.


#funtion Render Insert Page Only
def InsertPageView(request):
    return render(request, "app/insert.html")


def InsertData(request):
    #Data Come From HTML to View
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    #Creating Object of Model Class
    #Inserting Data Into Table
    newuser = Student.objects.create(Firstname = fname , Lastname = lname , Email = email, Contact = contact)

    #After Insert render on Show Page View
    return redirect('showpage')


#Show Page View
def ShowPage(request):
    #select * from table name
    #for fetching all the data on table
    all_data = Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})


#Edit Page View
def EditPage(request,pk):
    #fetching the data of particuler id
    get_data = Student.objects.get(id=pk)
    return render(request, "app/edit.html",{'key2':get_data})


#Update Data View
def UpdateData(request, pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

    #Query for Update
    udata.save()
    #render to show Page
    return redirect("showpage")


#Delete Data 
def DeleteData(request, pk):
    ddata = Student.objects.get(id=pk)
    #Query for Delete
    ddata.delete()
    return redirect("showpage")

