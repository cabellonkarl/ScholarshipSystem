from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from .models import *

# Create your views here.
class MyIndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class MyDashboardView(View):
    def get(self, request):
        scholarType = ScholarType.objects.all()
        scholar = Scholar.objects.all()
        working = Working.objects.all()
        bank = Bank.objects.all()
        scholarshipType = ScholarshipType.objects.all()
        scholarship = Scholarship.objects.all()
        subsidized = Subsidized.objects.all()
        percentile = Percentile.objects.all()
        nonWorking = NonWorking.objects.all()
        context = {
            'scholarType': scholarType,
            'scholar': scholar,
            'working': working,
            'bank': bank,
            'scholarshipType': scholarshipType,
            'scholarship': scholarship,
            'subsidized': subsidized,
            'percentile': percentile,
            'nonWorking': nonWorking,
        }
        return render(request, 'dashboard.html', context)


class MyScholarRegistrationView(View):
    def get(self, request):

        scholarType = ScholarType.objects.all()
        context = {
            "scholarType": scholarType
        }
        return render(request, 'addScholar.html', context)

    def post(self, request):
        form = scholarForm(request.POST)

        if form.is_valid():

            scholar_id = request.POST.get("scholar_id")
            fname = request.POST.get("firstName")
            mname = request.POST.get("middleName")
            lname = request.POST.get("lastName")
            course = request.POST.get("course")
            year = request.POST.get("year")
            totalfees = request.POST.get("totalFees")
            scholartype = ScholarType.objects.get(
            scholarType_id=request.POST.get("scholar_type"))
            form = Scholar(
                scholar_id=scholar_id,firstName=fname, middleName=mname,
                lastName=lname, course=course, year=year,
                totalFees=totalfees, scholar_type=scholartype)
            form.save()

            return redirect('final:my_dashboard_view')

        else:
            print(form.errors)
            return HttpResponse("NOT VALID")

class MyWorkingScholarRegistrationView(View):
    def get(self, request):

        working = Scholar.objects.all()
        context = {
            "working": working
        }
        return render(request, 'addWorking.html', context)

    def post(self, request):
         form = workingForm(request.POST)

         if form.is_valid():

             scholar_id = Scholar.objects.get(
                 scholar_id_id=request.POST.get("scholar_id"))
             office = request.POST.get("office")
             form = Working(
                   scholar_id_id=scholar_id,
                 officeAssigned=office)
             form.save()

             return redirect('final:my_dashboard_view')

         else:
             print(form.errors)
             return HttpResponse("NOT VALID")

class MyNonWorkingScholarRegistrationView(View):
    def get(self, request):

        nonworking = Scholar.objects.all()
        scholarships = Scholarship.objects.all()
        context = {
            "nonworking": nonworking,
            "scholarships": scholarships
        }
        return render(request, 'addNonWorking.html', context)
        
class MyScholarshipRegistrationView(View):
    def get(self, request):

        bank = Bank.objects.all()
        scholarshipType = ScholarshipType.objects.all()
        context = {
            "bank": bank,
            "scholarshipType": scholarshipType
        }
        return render(request, 'addScholarship.html', context)

class MySubsidizedScholarshipRegistrationView(View):
    def get(self, request):

        scholarship = Scholarship.objects.all()
        context = {
            "scholarship": scholarship
        }
        return render(request, 'addSubsidized.html', context)

class MyPercentileScholarshipRegistrationView(View):
    def get(self, request):

        scholarship = Scholarship.objects.all()
        context = {
            "scholarship": scholarship
        }
        return render(request, 'addPercentile.html', context)

class MyBankRegistrationView(View):
    def get(self, request):

        return render(request, 'addBank.html',{})