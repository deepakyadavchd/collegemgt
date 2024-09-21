from django.shortcuts import render, redirect
from .models import*



def createview(request):

    if(request.POST.get("crtbtn")):
        srollno = request.POST["rbtn"]
        sname = request.POST["nbtn"]
        smarks = request.POST["mbtn"]
        sresult = request.POST["rst"]

        if(  srollno =="" and sname =="" and smarks =="" ):
            er= {"error":" Enter All Details "}
            return  render(request, 'create.html', context=er)
      
        elif(srollno==""and sname=="" ):
            er= {"errorx":" Enter Roll no and name "}
            return render(request, 'create.html', context=er)
        
        elif(sname==""and smarks=="" ):
            er= {"errorxz":" Enter name and marks"}
            return render(request, 'create.html', context=er)
        
        elif(srollno==""and smarks=="" ):
            er= {"errorv":" Enter Roll no and marks "}
            return render(request, 'create.html', context=er)
        
        elif(srollno=="" ):
            er= {"error":" Enter Roll no "}
            return render(request, 'create.html', context=er)
        
        elif(sname=="" ):
            er2= {"error2":" Enter name "}
            return render(request, 'create.html', context=er2)

        elif(smarks=="" ):
            er3= {"error3":" Enter marks "}
            return render(request, 'create.html', context=er3)
        
        #Students.objects.create(roll_no=srollno, name=sname, marks=smarks, result=sresult)
        st_obj = Students(roll_no=srollno, name=sname, marks=smarks, result=sresult)
        st_obj.save()
        
    if(request.POST.get("crtbtn")):
            mess={"msg": "thankyou for submission"}
            return render(request, 'create.html', context=mess)
    return render(request, 'create.html')


def resultview(request):
    if(request.POST.get("btnxyz")):
        rl = request.POST.get("input")
        mems = Students.objects.filter(roll_no=rl)
        
        l = len(mems)
        if l==0:
            data={"min":" Record not found "}

        if l=="" :   
            data={"queryset":"enter rollno "}
        else:
            data={"queryset":mems}
        return render(request, 'results.html', context=data)
    
    mems=Students.objects.all()
    l = len(mems)
    if l==0:
        data={"min":" Record not found "}
    else:
        data={"queryset":mems}
    return render(request, 'results.html', context=data)

def detailsview(request):
    roll = request.GET.get("r")
    print("rollno>>>>>", roll)
    mems=Students.objects.filter(roll_no=roll)
    data={"queryset":mems}
    return render(request, 'detail.html', context=data)

def deleteview(request):
    roll = request.GET.get("r")
    print("rollno>>>>>", roll)
    Students.objects.filter(roll_no=roll).delete()
    return redirect("../result")


def editview(request):
    roll = request.GET.get("re")
    print("rollno>>>>>", roll)
    Students.objects.filter(roll_no=roll).update()
    return redirect("../result")
