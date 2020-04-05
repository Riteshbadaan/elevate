from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from first.models import Userprofile,userprofile2,teamdetails,User
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

flag404=True

def intro(request):
    global flag404
    flag404 = True
    return render(request, "first/index.html")


def register(request):
    if request.method == "POST":
        if 'register' in request.POST:
            mainphone = request.POST.get('reg-phone')
            mainemail = request.POST.get('reg-email')
            mainpassword = request.POST.get('reg-password')
            print(mainemail)
            try:
                usernoobkanoob=User.objects.get(username=mainemail)
            except User.DoesNotExist:
                usernoobkanoob=None
            if usernoobkanoob is None:
                fun = 1
                a = User.objects.create_user(username=mainemail, password=mainpassword)
                a.save()
                b = Userprofile()
                b.user = a
                b.phone = mainphone
                b.save()
                dict = {'f': fun}
                return render(request, "first/index_infopage.html", context=dict)
            else:
                print("here")
                fun=4
                dict = {'f': fun}
                # print("post")
                return render(request, "first/index_infopage.html", context=dict)
        else:
            loginemail=request.POST.get('log-email')
            loginpassword = request.POST.get('log-password')
            dropdown=request.POST.get('drop')
            print(dropdown)
            a=auth.authenticate(username=loginemail,password=loginpassword)
            if a is not None:
                print("pass")
                auth.login(request, a)
                b = userprofile2(user=request.user)
                b.game = dropdown
                b.save()
                if dropdown == "BasketBall-Man":
                    return redirect("https://www.payumoney.com/paybypayumoney/#/44D817A090C0C2EE8E99DE5C148E8C4C")
                elif dropdown == "Basketball-Women":
                    return redirect("https://www.payumoney.com/paybypayumoney/#/A8EBEEDB53F1FC4C518ADBB81A02821A")
                elif dropdown == "Volleyball-Men":
                    return redirect("https://www.payumoney.com/paybypayumoney/#/A54377A13C605E41EABD47C895227748")
                elif dropdown == "Volleyball-Women":
                    return redirect("https://www.payumoney.com/paybypayumoney/#/4232CCD50D9FAE0125993B4F29568C41")
                elif dropdown == "Cricket":
                    #return redirect("https://www.payumoney.com/paybypayumoney/#/CE315536CF626BD5C08A5B29FA18E06A")
                     return redirect("https://www.payumoney.com/paybypayumoney/#/FA30EF106DF3C730F4B164885CDF61BA")
                else:
                    return redirect("https://www.payumoney.com/paybypayumoney/#/CE315536CF626BD5C08A5B29FA18E06A")
            else:
                print("fail")
                fun = 3
                dict = {'f': fun}
                return render(request, "first/index_infopage.html", context=dict)
    else:
        return render(request, 'first/index_infopage.html')

def team(request):
    if request.method == "POST":
        college=request.POST.get('selection')
        collegename=request.POST.get('inst-name')
        name1=request.POST.get('name1')
        email1 = request.POST.get('email1')
        phone1=request.POST.get('phone1')

        name2 = request.POST.get('name2')
        email2 = request.POST.get('email2')
        phone2 = request.POST.get('phone2')

        name3 = request.POST.get('name3')
        email3 = request.POST.get('email3')
        phone3 = request.POST.get('phone3')

        name4 = request.POST.get('name4')
        email4 = request.POST.get('email4')
        phone4 = request.POST.get('phone4')

        name5 = request.POST.get('name5')
        email5 = request.POST.get('email5')
        phone5 = request.POST.get('phone5')

        name6 = request.POST.get('name6')
        email6 = request.POST.get('email6')
        phone6 = request.POST.get('phone6')

        if len(phone1) is not 10:
            return HttpResponseRedirect(reverse('team'))
        if len(phone2) is not 10:
            return HttpResponseRedirect(reverse('team'))
        if len(phone3) is not 10:
            return HttpResponseRedirect(reverse('team'))
        if len(phone4) is not 10:
            return HttpResponseRedirect(reverse('team'))
        if len(phone5) is not 10:
            return HttpResponseRedirect(reverse('team'))

        if phone6 == "":
            phone6 = 0
        elif len(phone6) is not 10:
            return HttpResponseRedirect(reverse('team'))

        name7 = request.POST.get('name7')
        email7 = request.POST.get('email7')
        phone7 = request.POST.get('phone7')
        if phone7 == "":
            phone7 = 0
        elif len(phone7) is not 10:
            return HttpResponseRedirect(reverse('team'))

        name8 = request.POST.get('name8')
        email8 = request.POST.get('email8')
        phone8 = request.POST.get('phone8')
        if phone8 == "":
            phone8 = 0
        elif len(phone8) is not 10:
            return HttpResponseRedirect(reverse('team'))
        phone9 = request.POST.get('phone9')
        name9 = request.POST.get('name9')
        email9 = request.POST.get('email9')
        if phone9 == "":
            phone9 = 0
        elif len(phone9) is not 10:
            return HttpResponseRedirect(reverse('team'))
        phone10 = request.POST.get('phone10')
        name10 = request.POST.get('name10')
        email10 = request.POST.get('email10')
        if phone10 == "":
            phone10 = 0
        elif len(phone10) is not 10:
            return HttpResponseRedirect(reverse('team'))

        phone11 = request.POST.get('phone10')
        name11 = request.POST.get('name11')
        email11 = request.POST.get('email11')
        if phone11 == "":
            phone11 = 0
        elif len(phone11) is not 10:
            return HttpResponseRedirect(reverse('team'))
        phone12 = request.POST.get('phone12')
        name12 = request.POST.get('name12')
        email12 = request.POST.get('email12')
        if phone12 == "":
            phone12 = 0
        elif len(phone12) is not 10:
            return HttpResponseRedirect(reverse('team'))

        c=teamdetails(user=request.user)
        c.typeofcompany=college
        c.insti_name=collegename
        c.pl1 = name1
        c.pl2 = name2
        c.pl3 = name3
        c.pl4 = name4
        c.pl5 = name5
        c.pl6 = name6
        c.pl7 = name7
        c.pl8 = name8
        c.pl9 = name9
        c.pl10 = name10
        c.pl11 = name11
        c.pl12 = name12

        c.email1 = email1
        c.email2 = email2
        c.email3 = email3
        c.email4 = email4
        c.email5 = email5
        c.email6 = email6
        c.email7 = email7
        c.email8 = email8
        c.email9 = email9
        c.email10 = email10
        c.email11 = email11
        c.email12 = email12

        c.phone1=phone1
        c.phone2 = phone2
        c.phone3 = phone3
        c.phone4 = phone4
        c.phone5 = phone5
        c.phone6 = phone6
        c.phone7 = phone7
        c.phone8 = phone8
        c.phone9=phone9
        c.phone10 = phone10
        c.phone11 = phone11
        c.phone12 = phone12

        c.save()
        if c is not None:
            auth.logout(request)
            return HttpResponseRedirect(reverse('intro'))
        else:
            return render(request, 'first/registration_form.html')
    else:
        if flag404==True:
            return HttpResponseRedirect(reverse('register'))
        else:
            return render(request, 'first/registration_form.html')
@csrf_exempt
def team1(request):
    if request.method =="POST":
        global flag404
        flag404=False
        print("in here")
        print(request.POST)
        return HttpResponseRedirect(reverse('team'))