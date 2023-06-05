from django.urls import path
from final import views

app_name='final'

urlpatterns = [
    path('index', views.MyIndexView.as_view(), name="my_index_view"),
    path('dashboard', views.MyDashboardView.as_view(), name="my_dashboard_view"),
    path('addScholar', views.MyScholarRegistrationView.as_view(), name="my_addScholar_view"),
    path('addWorking', views.MyWorkingScholarRegistrationView.as_view(), name="my_addWorking_view"),
    path('addNonWorking', views.MyNonWorkingScholarRegistrationView.as_view(), name="my_addNonWorking_view"),
    path('addScholarship', views.MyScholarshipRegistrationView.as_view(), name="my_addScholarship_view"),
    path('addSubsidized', views.MySubsidizedScholarshipRegistrationView.as_view(), name="my_addSubsidized_view"),
    path('addPercentile', views.MyPercentileScholarshipRegistrationView.as_view(), name="my_addPercentile_view"),
    path('addBank', views.MyBankRegistrationView.as_view(), name="my_addBank_view"),

]
