from django.shortcuts import render
from django.contrib import messages
from .models import student
from .forms import regform,loginform
from django.http import *

def index(request):
	return render(request,'student/index.html')

def Register(request):
	return render(request,'student/Register.html',{'regform':regform})

def Login(request):
	return render(request,'student/Login.html',{'loginform':loginform})

def studentreg(request):

	# two way form register this 1st way
		# name=request.POST.get('name')
		# std=request.POST.get('std')
		# roll_no=request.POST.get('roll_no')
		# password=request.POST.get('password')
		# data=student.objects.create(name=name,std=std,roll_no=roll_no,password=password)
		# return render(request,'student/index.html',{'sucmsg':'You Are Register Successfully...'})

	# 2nd way

	if request.method =="POST": # use first way
		form = regform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'You Are Register Successfully Now Login...') #ignore
			return HttpResponseRedirect('/Slogin/') # use return render
	else:
		form = regform()
		return render(request,'student/Register.html',{'regform':form})

def chklogin(request):
	if request.method == "POST":
		txtname=request.POST['name']
		txtpassword=request.POST['password']

		formlogin = loginform(request.POST)

		if formlogin.is_valid():

			if student.objects.filter(name=txtname,password=txtpassword):
				messages.success(request, 'Your Wellcome ...')
				return HttpResponseRedirect('/display/') # use return render
			else:
				messages.error(request, 'Invalid Username Or Password...')
				return HttpResponseRedirect('/Slogin/') # use return render
	else:
		formlogin = loginform()
		return render(request,'student/Login.html',{'loginform':formlogin})	
def display(request):
	data = student.objects.all()	
	return render(request,'student/Display.html',{'data':data})

def updatestud(request, student_e_id):
	studdata = student.objects.filter(pk = student_e_id)
	return render(request,'student/StudentUpdate.html',{'studdata':studdata})

def deletstud(request, student_d_id):
	studdata = student.objects.get(pk = student_d_id)
	studdata.delete()
	data = student.objects.all()	
	messages.success(request, 'Record Is Successfully Deleted...')
	return render(request,'student/Display.html',{'data':data})

def finalstudupdate(request):
	if request.method == 'POST':

		studid=request.POST.get('studid')
		name=request.POST.get('name')
		std=request.POST.get('std')
		roll_no=request.POST.get('roll_no')
		password=request.POST.get('password')
		data = student.objects.get(pk = studid)
		data.name=name
		data.std=std
		data.roll_no=roll_no
		data.password=password
		data.save()

		messages.success(request, 'Record Updated Successfully...')
		data2 = student.objects.all()	
		return render(request,'student/Display.html',{'data':data2})

	else:
		return render(request,'student/StudentUpdate.html',{'studdata':'Method Is Not Valid'})

def getjson(request):
	data=list(student.objects.values())
	return JsonResponse(data,safe=False)







