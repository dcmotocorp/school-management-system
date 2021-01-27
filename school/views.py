from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from random import randint
from .utils import sendmail
# Create your views here.
def add(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        return render(request,'school/index.html',{'uid':uid})
    else:
        return render(request, 'school/index.html')



def add1(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        return render(request, 'school/index.html', {'uid': uid})
    else:
        return render(request,'school/about.html')

def add2(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        return render(request, 'school/codes.html', {'uid': uid})

    else:
        return render(request,'school/codes.html')

def add3(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        return render(request, 'school/contact.html', {'uid': uid})

    else:
        return render(request,'school/contact.html')

def add4(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        return render(request, 'school/gallery.html', {'uid': uid})

    else:
        return render(request,'school/gallery.html')

def add5(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        return render(request, 'school/services.html', {'uid': uid})

    else:
        return render(request,'school/services.html')

def add6(request):
    return render(request,'school/studentregistration.html')

def add7(request):
    return render(request,'school/facultyregistration.html')


def add8(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        return render(request, 'school/index.html', {'uid':uid})
    else:
        return render(request,'school/studentlogin.html')

def registration(request):
    role=request.POST['role']
    u_name=request.POST['username']
    e_mail = request.POST['email']
    p_ss= request.POST['password']
    uid=user.objects.create(username=u_name,email=e_mail,password=p_ss,role=role)
    if uid:
        k="success"
        if role=="Student":
            sid=Student.objects.create(username=u_name,email=e_mail,password=p_ss,user_id=uid)
            send_mail("conformation-message","wel come to school", "dipenpatel898065@gmail.com",[e_mail])
            return render(request,'school/studentlogin.html',{'key':k})
        elif role=="Faculty":
            fid = Student.objects.create(username=u_name, email=e_mail, password=p_ss,user_id=uid)
            send_mail("conformation-message", "wel come to school", "dipenpatel898065@gmail.com", [e_mail])
            return render(request, 'school/studentlogin.html', {'key': k})
        else:
            k = "unsucess"
            return render(request, 'school/studentregistration.html', {'key': k})

    else:
        k="unsucess"
        return render(request, 'school/studentregistration.html',{'key':k})

def loginredirect(request):
    try:
        e_name=request.POST['email']
        p_ssw=request.POST['password']
        uid=user.objects.get(email=e_name)

        if uid:
            if uid.password==p_ssw:
                request.session['username']=uid.username
                request.session['email'] = uid.email
                return render(request, 'school/index.html',{'uid':uid})
            else:
                return render(request, 'school/studentlogin.html')
        else:
            return render(request, 'school/studentlogin.html')

    except:

       return render(request, 'school/studentlogin.html')


def logout(request):
    if 'email' in request.session:
        del request.session['username']
        del request.session['email']
        return render(request, 'school/studentlogin.html')
    else:
        return render(request, 'school/studentlogin.html')


def view_all(request):
    data=user.objects.all()

    return render(request, 'school/view_all.html',{'data':data})
def delete_data(request,pk):
    uid=user.objects.get(id=pk)
    uid.delete()
    data=user.objects.all()
    return render(request, 'school/view_all.html',{'data':data})


def edit_data(request,ck):
    pass

def edit_page(request):
    return render(request,"school/edit-page.html")


def forgotpassword(request):
    return render(request,'school/forgotpassword.html')

def sentotp(request):
    email=request.POST['email']
    uid=user.objects.get(email=email)
    if uid:
        otp=randint(1111,9999)
        uid.otp=otp #update otp
        uid.save()
        if uid.role=='Student':
            sid=Student.objects.get(user_id=uid)
            context={
                  'sid':sid,
                  'otp':otp
            }
            sendmail("Forgot Password","mail_template",email,{'context': context})
            return render(request, "school/reset.html", {'email':email})
    elif uid.role=='Faculty':
        otp = randint(1111, 9999)
        uid.otp = otp  # update otp
        uid.save()
        fid = Faculty.objects.get(user_id=uid)
        context = {
            'fid': fid,
            'otp': otp
        }
        sendmail("Forgot Password", "mail_template", email, {'context': context})
        return render(request, "school/reset.html", {'email': email})

def reset(request):
    email = request.POST['email']
    otp = request.POST['otp']
    newpassword = request.POST['newpassword']
    repassword = request.POST['repassword']
    uid =user.objects.get(email=email)
    if uid:
        if str(uid.otp) == otp and newpassword == repassword:
            uid.password = newpassword
            uid.save()
            k= "succesful save"
            return render(request, "school/index.html", {'k': k})
        else:
            k= "unsuccesful save"
            return render(request, "school/forgotpassword", {'k': k}, {'email': email})
    else:
        return render(request, "school/forgotpassword")
