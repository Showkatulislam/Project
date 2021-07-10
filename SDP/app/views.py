from django.db.models.query_utils import PathInfo
from .models import Doctor,Disease,Prescription,Symptoms
from django.shortcuts import render,HttpResponse,redirect
from .forms import Customerregistration
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,'home.html')
def Registation(request):
    if request.method=='POST':
        fm=Customerregistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Done your Registration")
        return render(request,'Registation.html',{'form':fm})
    else:
        fm=Customerregistration()
        return render(request,'Registation.html',{'form':fm})
def Profile(request):
        # inputlist=[]
        # for i in range(1,26):
        #     if(request.POST.get(str(f"{i}"))!=None):
        #         inputlist.append(request.POST.get(str(f"{i}")))
        #         print(inputlist)
        obj=Symptoms.objects.all()
        context={
            'obj':obj,
             'j':0
        }
        return render(request,'profile.html',context)

def suggestion(request):
    inputlist=[]
    for i in range(1,26):
        if(request.GET.get(str(f"{i}"))!=None):
            inputlist.append(request.GET.get(str(f"{i}")))
    percentage=00
    listlen=len(inputlist)
    if listlen==5:
        dis=Disease.objects.filter((Q(symptom1=inputlist[0]) & Q(symptom2=inputlist[1]) &
        Q(symptom3=inputlist[2]) & Q(symptom4=inputlist[3]) & Q(symptom5=inputlist[4])))
        percentage=100
        print(dis)

    elif listlen==4:
        dis=Disease.objects.filter(Q(symptom1=inputlist[0]) & Q(symptom2=inputlist[1]) &
        Q(symptom3=inputlist[2]) & Q(symptom4=inputlist[3]))
        percentage=80
        print(dis)

    elif listlen==3:
        dis=Disease.objects.filter(Q(symptom1=inputlist[0]) & Q(symptom2=inputlist[1]) &
        Q(symptom3=inputlist[2]))
        percentage=60
        print(dis)
    
    elif listlen==2:
        dis=Disease.objects.filter(Q(symptom1=inputlist[0]) & Q(symptom2=inputlist[1]))
        percentage=40
        print(dis)
    elif listlen==1:
        dis=Disease.objects.filter(Q(symptom1=inputlist[0]) | Q(symptom2=inputlist[0]) | Q(symptom3=inputlist[0]) | Q(symptom4=inputlist[0]) or Q(symptom5=inputlist[0]))
        percentage=20
    dis1=dis.first()
    print(dis1.name_disease)
    doctor=Doctor.objects.get(specialist=dis1.name_disease)
    print(doctor.name)
    context={
            'disease':dis,
            'percentage':percentage,
            'doctor':doctor
        }

    return render(request,'suggestion.html',context)

def doctor(request,pk):
    return render(request,'doctor.html')
def takepre(request):
    if request.method=='POST':
        f_name=request.POST.get('fullname')
        phone=request.POST.get('phone')
        doctor=request.POST.get('doctor')
        pre=Prescription(f_name=f_name,phone=phone,doctor=doctor)
        pre.save()
        return render(request,'done.html')
       
    return render(request,'prescription.html')