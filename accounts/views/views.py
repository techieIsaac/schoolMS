from django.shortcuts import *
from django.views.generic import CreateView
from accounts.models import *
from accounts.forms import *
from django.contrib.auth.decorators import login_required

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

@login_required
def home(request):
    return render(request, 'accounts/home.html')


def login(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    return render(request, 'accounts/login.html')

    #######################################


# THE CRUD OPERATIONS ON A CLASS MODULE #
#######################################
@login_required
def createclassinformation(request):
    if request.method == "POST":
        form = ClassinformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createclassinformation')
    else:
        form = ClassinformationForm()
        context = {'form': form}
        return render(request, 'accounts/Class/createclassinformation.html', context)

@login_required
def editclassinformation(request, pk):
    item = get_object_or_404(Classinformation, id=pk)
    if request.method == "POST":
        form = EditclassinformationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewclassinformation')
    else:
        form = EditclassinformationForm(instance=item)
        return render(request, 'accounts/Class/editclassinformation.html', {'form': form})

@login_required
def viewclassinformation(request):
    all_info = Classinformation.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Class/viewclassinformation.html', context)


#######################################
# THE CRUD OPERATIONS ON SECTION MODULE #
#######################################
@login_required
def createsectioninformation(request):
    if request.method == "POST":
        form = SectioninformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createsectioninformation')
    else:
        form = SectioninformationForm()
        context = {'form': form}
        return render(request, 'accounts/Section/createsectioninformation.html', context)

@login_required
def editsectioninformation(request, pk):
    item = get_object_or_404(Sectioninformation, id=pk)
    if request.method == "POST":
        form = EditsectioninformationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewsectioninformation')
    else:
        form = EditsectioninformationForm(instance=item)
        return render(request, 'accounts/Section/editsectioninformation.html', {'form': form})

@login_required
def viewsectioninformation(request):
    all_info = Sectioninformation.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Section/viewsectioninformation.html', context)


#######################################
#   CRUD FOR THE SUBJECT MODULE          #
#######################################
@login_required
def addsubject(request):
    if request.method == "POST":
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addsubject')
    else:
        form = AddSubjectForm()
        context = {'form': form}
        return render(request, 'accounts/Subject/addsubject.html', context)

@login_required
def editsubject(request, pk):
    item = get_object_or_404(Subjects, id=pk)
    if request.method == "POST":
        form = EditSubjectForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewsubjects')
    else:
        form = EditSubjectForm(instance=item)
        return render(request, 'accounts/Subject/editsubject.html', {'form': form})

@login_required
def deletesubject(request, pk):
    Subjects.objects.filter(id=pk).delete()
    all_info = Subjects.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Subject/viewsubjects.html', context)

@login_required
def viewsubjects(request):
    all_info = Subjects.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Subject/viewsubjects.html', context)


#######################################
#   CRUD FOR THE Syllabus MODULE        #
#######################################
@login_required
def addsyllabus(request):
    if request.method == "POST":
        form = AddSyllabusForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addsyllabus')
    else:
        form = AddSyllabusForm()
        context = {'form': form}
        return render(request, 'accounts/Syllabus/addsyllabus.html', context)

@login_required
def editsyllabus(request, pk):
    item = get_object_or_404(Syllabus, id=pk)
    if request.method == "POST":
        form = EditSyllabusForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewsyllabus')
    else:
        form = EditSyllabusForm(instance=item)
        return render(request, 'accounts/Syllabus/editsyllabus.html', {'form': form})

@login_required
def deletesyllabus(request, pk):
    Syllabus.objects.filter(id=pk).delete()
    all_info = Syllabus.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Syllabus/viewsyllabus.html', context)

@login_required
def viewsyllabus(request):
    all_info = Syllabus.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Syllabus/viewsyllabus.html', context)


###############################################
#   CRUD FOR THE HUMAN RESOURCES MANAGER MODULE #
###############################################
@login_required
def addhumanresource(request):
    if request.method == "POST":
        form = AddHumanResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addhumanresource')
    else:
        form = AddHumanResourceForm()
        context = {'form': form}
        return render(request, 'accounts/HumanResource/addhumanresource.html', context)

@login_required
def edithumanresource(request, pk):
    item = get_object_or_404(HumanResource, id=pk)
    if request.method == "POST":
        form = EditHumanResourceForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewhumanresource')
    else:
        form = EditHumanResourceForm(instance=item)
        return render(request, 'accounts/HumanResource/edithumanresource.html', {'form': form})

@login_required
def deletehumanresource(request, pk):
    HumanResource.objects.filter(id=pk).delete()
    all_info = HumanResource.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/HumanResource/viewhumanresource.html', context)

@login_required
def viewhumanresource(request):
    all_info = HumanResource.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/HumanResource/viewhumanresource.html', context)


###############################################
############  CRUD FOR THE ROUTINE #############
###############################################
@login_required
def addroutine(request):
    if request.method == "POST":
        form = AddRoutineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addroutine')
    else:
        form = AddRoutineForm()
        context = {'form': form}
        return render(request, 'accounts/Routine/addroutine.html', context)

@login_required
def editroutine(request, pk):
    item = get_object_or_404(Routine, id=pk)
    if request.method == "POST":
        form = EditRoutineForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewroutine')
    else:
        form = EditRoutineForm(instance=item)
        return render(request, 'accounts/Routine/editroutine.html', {'form': form})

@login_required
def deleteroutine(request, pk):
    Routine.objects.filter(id=pk).delete()
    all_info = Routine.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Routine/viewroutine.html', context)

@login_required
def viewroutine(request):
    all_info = Routine.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Routine/viewroutine.html', context)


#######################################
#   CRUD FOR THE ASSIGNMENT MODULE    #
#######################################
@login_required
def addassignment(request):
    if request.method == "POST":
        form = AddAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addassignment')
    else:
        form = AddAssignmentForm()
        context = {'form': form}
        return render(request, 'accounts/Assignment/addassignment.html', context)

@login_required
def editassignment(request, pk):
    item = get_object_or_404(Assignment, id=pk)
    if request.method == "POST":
        form = EditAssignmentForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewassignment')
    else:
        form = EditAssignmentForm(instance=item)
        return render(request, 'accounts/Assignment/editassignment.html', {'form': form})

@login_required
def deleteassignment(request, pk):
    Assignment.objects.filter(id=pk).delete()
    all_info = Assignment.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Assignment/viewassignment.html', context)

@login_required
def viewassignment(request):
    all_info = Assignment.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Assignment/viewassignment.html', context)


#######################################
#   CRUD FOR THE EXAM GRADE MODULE    #
#######################################
@login_required
def addexamgrade(request):
    if request.method == "POST":
        form = AddExamGradeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexamgrade')
    else:
        form = AddExamGradeForm()
        context = {'form': form}
        return render(request, 'accounts/Exam/addexamgrade.html', context)

@login_required
def editexamgrade(request, pk):
    item = get_object_or_404(ExamGrade, id=pk)
    if request.method == "POST":
        form = EditExamGradeForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewexamgrade')
    else:
        form = EditExamGradeForm(instance=item)
        return render(request, 'accounts/Exam/editexamgrade.html', {'form': form})

@login_required
def deleteexamgrade(request, pk):
    ExamGrade.objects.filter(id=pk).delete()
    all_info = ExamGrade.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Exam/viewexamgrade.html', context)

@login_required
def viewexamgrade(request):
    all_info = ExamGrade.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Exam/viewexamgrade.html', context)


#######################################
#   CRUD FOR THE EXAM TERM MODULE    #
#######################################
@login_required
def addexamterm(request):
    if request.method == "POST":
        form = AddExamTermForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexamterm')
    else:
        form = AddExamTermForm()
        context = {'form': form}
        return render(request, 'accounts/Exam/addexamterm.html', context)

@login_required
def editexamterm(request, pk):
    item = get_object_or_404(ExamTerm, id=pk)
    if request.method == "POST":
        form = EditExamTermForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewexamterm')
    else:
        form = EditExamTermeForm(instance=item)
        return render(request, 'accounts/Exam/editexamterm.html', {'form': form})

@login_required
def deleteexamterm(request, pk):
    ExamTerm.objects.filter(id=pk).delete()
    all_info = ExamTerm.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Exam/viewexamterm.html', context)

@login_required
def viewexamterm(request):
    all_info = ExamTerm.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Exam/viewexamterm.html', context)


#######################################
#   CRUD FOR THE EXAM SCHEDULE MODULE    #
#######################################
@login_required
def addexamschedule(request):
    if request.method == "POST":
        form = AddExamScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexamschedule')
    else:
        form = AddExamScheduleForm()
        context = {'form': form}
        return render(request, 'accounts/Exam/addexamschedule.html', context)

@login_required
def editexamschedule(request, pk):
    item = get_object_or_404(ExamSchedule, id=pk)
    if request.method == "POST":
        form = EditExamScheduleForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewexamschedule')
    else:
        form = EditExamScheduleForm(instance=item)
        return render(request, 'accounts/Exam/editexamschedule.html', {'form': form})

@login_required
def deleteexamschedule(request, pk):
    ExamSchedule.objects.filter(id=pk).delete()
    all_info = ExamSchedule.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Exam/viewexamschedule.html', context)

@login_required
def viewexamschedule(request):
    all_info = ExamSchedule.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Exam/viewexamschedule.html', context)


#######################################
#   CRUD FOR THE EXAM SUGGESTION MODULE    #
#######################################
@login_required
def addexamsuggestion(request):
    if request.method == "POST":
        form = AddExamSuggestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexamsuggestion')
    else:
        form = AddExamSuggestionForm()
        context = {'form': form}
        return render(request, 'accounts/Exam/addexamsuggestion.html', context)

@login_required
def editexamsuggestion(request, pk):
    item = get_object_or_404(ExamSuggestion, id=pk)
    if request.method == "POST":
        form = EditExamSuggestionForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewexamsuggestion')
    else:
        form = EditExamSuggestionForm(instance=item)
        return render(request, 'accounts/Exam/editexamsuggestion.html', {'form': form})

@login_required
def deleteexamsuggestion(request, pk):
    ExamSuggestion.objects.filter(id=pk).delete()
    all_info = ExamSuggestion.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Exam/viewexamsuggestion.html', context)

@login_required
def viewexamsuggestion(request):
    all_info = ExamSuggestion.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Exam/viewexamsuggestion.html', context)


#######################################
#   CRUD FOR THE LIBRARY MODULE         #
#######################################
def addlibrarybook(request):
    if request.method == "POST":
        form = AddLibraryBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addlibrarybook')
    else:
        form = AddLibraryBookForm()
        context = {'form': form}
        return render(request, 'accounts/Library/addlibrarybook.html', context)


def editlibrarybook(request, pk):
    item = get_object_or_404(Library, id=pk)
    if request.method == "POST":
        form = EditLibraryBookForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewlibrarybook')
    else:
        form = EditLibraryBookForm(instance=item)
        return render(request, 'accounts/Library/editlibrarybook.html', {'form': form})


def deletelibrarybook(request, pk):
    Library.objects.filter(id=pk).delete()
    all_info = Library.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Library/viewlibrarybook.html', context)

@login_required
def viewlibrarybook(request):
    all_info = Library.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Library/viewlibrarybook.html', context)


#######################################
#   CRUD FOR THE VEHICLE MODULE         #
#######################################
def addvehicle(request):
    if request.method == "POST":
        form = AddVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addvehicle')
    else:
        form = AddVehicleForm()
        context = {'form': form}
        return render(request, 'accounts/Transport/addvehicle.html', context)


def editvehicle(request, pk):
    item = get_object_or_404(Transport, id=pk)
    if request.method == "POST":
        form = EditVehicleForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewvehicle')
    else:
        form = EditVehicleForm(instance=item)
        return render(request, 'accounts/Transport/editvehicle.html', {'form': form})


def deletevehicle(request, pk):
    Transport.objects.filter(id=pk).delete()
    all_info = Transport.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Transport/viewvehicle.html', context)

@login_required
def viewvehicle(request):
    all_info = Transport.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Transport/viewvehicle.html', context)


#############################################
#   CRUD FOR THE TRANSPORT ROUTE MODULE         #
#############################################
def addroute(request):
    if request.method == "POST":
        form = AddRouteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addroute')
    else:
        form = AddRouteForm()
        context = {'form': form}
        return render(request, 'accounts/Transport/addroute.html', context)


def editroute(request, pk):
    item = get_object_or_404(Transport, id=pk)
    if request.method == "POST":
        form = EditRouteForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewroute')
    else:
        form = EditRouteForm(instance=item)
        return render(request, 'accounts/Transport/editroute.html', {'form': form})


def deleteroute(request, pk):
    Route.objects.filter(id=pk).delete()
    all_info = Route.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Transport/viewroute.html', context)

@login_required
def viewroute(request):
    all_info = Route.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Transport/viewroute.html', context)


################################################
#   CRUD FOR THE HOSTEL INFORMATION MODULE         #
################################################
def addhostel(request):
    if request.method == "POST":
        form = AddHostelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addhostel')
    else:
        form = AddHostelForm()
        context = {'form': form}
        return render(request, 'accounts/Hostel/addhostel.html', context)


def edithostel(request, pk):
    item = get_object_or_404(Hostel, id=pk)
    if request.method == "POST":
        form = EditHostelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewhostel')
    else:
        form = EditHostelForm(instance=item)
        return render(request, 'accounts/Hostel/edithostel.html', {'form': form})


def deletehostel(request, pk):
    Hostel.objects.filter(id=pk).delete()
    all_info = Hostel.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Hostel/viewhostel.html', context)

@login_required
def viewhostel(request):
    all_info = Hostel.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Hostel/viewhostel.html', context)


################################################
#   CRUD FOR THE HOSTEL ROOM MODULE              #
################################################
def addroom(request):
    if request.method == "POST":
        form = AddHostelRoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addroom')
    else:
        form = AddHostelRoomForm()
        context = {'form': form}
        return render(request, 'accounts/Hostel/addhostelroom.html', context)


def editroom(request, pk):
    item = get_object_or_404(HostelRooms, id=pk)
    if request.method == "POST":
        form = EditHostelRoomForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewroom')
    else:
        form = EditHostelRoomForm(instance=item)
        return render(request, 'accounts/Hostel/edithostelroom.html', {'form': form})


def deleteroom(request, pk):
    HostelRooms.objects.filter(id=pk).delete()
    all_info = HostelRooms.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Hostel/viewhostelroom.html', context)

@login_required
def viewroom(request):
    all_info = HostelRooms.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Hostel/viewhostelroom.html', context)


################################################
#   CRUD FOR THE VISITOR INFO MODULE              #
################################################
def addvisitor(request):
    if request.method == "POST":
        form = AddVistorInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addvisitor')
    else:
        form = AddVistorInfoForm()
        context = {'form': form}
        return render(request, 'accounts/Visitor/addvisitor.html', context)


def editvisitor(request, pk):
    item = get_object_or_404(VisitorInfor, id=pk)
    if request.method == "POST":
        form = EditVistorInfoForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewvisitor')
    else:
        form = EditVistorInfoForm(instance=item)
        return render(request, 'accounts/Visitor/editvisitor.html', {'form': form})


def deletevisitor(request, pk):
    VisitorInfor.objects.filter(id=pk).delete()
    all_info = VisitorInfor.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Visitor/viewvisitor.html', context)

@login_required
def viewvisitor(request):
    all_info = VisitorInfor.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Visitor/viewvisitor.html', context)


################################################
#   CRUD FOR THE SALARY GRADE INFO MODULE        #
################################################
def addsalarygrade(request):
    if request.method == "POST":
        form = AddSalaryGradeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addsalarygrade')
    else:
        form = AddSalaryGradeForm()
        context = {'form': form}
        return render(request, 'accounts/Payroll/addsalarygrade.html', context)


def editsalarygrade(request, pk):
    item = get_object_or_404(SalaryGrade, id=pk)
    if request.method == "POST":
        form = EditSalaryGradeForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewsalarygrade')
    else:
        form = EditSalaryGradeForm(instance=item)
        return render(request, 'accounts/Payroll/editsalarygrade.html', {'form': form})


def deletesalarygrade(request, pk):
    SalaryGrade.objects.filter(id=pk).delete()
    all_info = SalaryGrade.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Payroll/viewsalarygrade.html', context)

@login_required
def viewsalarygrade(request):
    all_info = SalaryGrade.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Payroll/viewsalarygrade.html', context)


################################################
#   CRUD FOR THE DISCOUNT MODULE        #
################################################
def adddiscount(request):
    if request.method == "POST":
        form = AddFeeTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adddiscount')
    else:
        form = AddFeeTypeForm()
        context = {'form': form}
        return render(request, 'accounts/Accounting/adddiscount.html', context)


def editdiscount(request, pk):
    item = get_object_or_404(Discount, id=pk)
    if request.method == "POST":
        form = EditDiscountForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewdiscount')
    else:
        form = EditDiscountForm(instance=item)
        return render(request, 'accounts/Accounting/editdiscount.html', {'form': form})


def deletediscount(request, pk):
    Discount.objects.filter(id=pk).delete()
    all_info = Discount.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewdiscount.html', context)

@login_required
def viewdiscount(request):
    all_info = Discount.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewdiscount.html', context)


################################################
#   CRUD FOR THE FEE TYPE MODULE        #
################################################
def addfeetype(request):
    if request.method == "POST":
        form = AddFeeTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addfeetype')
    else:
        form = AddFeeTypeForm()
        context = {'form': form}
        return render(request, 'accounts/Accounting/addfeetype.html', context)


def editfeetype(request, pk):
    item = get_object_or_404(FeeType, id=pk)
    if request.method == "POST":
        form = EditFeeTypeForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewfeetype')
    else:
        form = EditFeeTypeForm(instance=item)
        return render(request, 'accounts/Accounting/editfeetype.html', {'form': form})


def deletefeetype(request, pk):
    FeeType.objects.filter(id=pk).delete()
    all_info = FeeType.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewfeetype.html', context)

@login_required
def viewfeetype(request):
    all_info = FeeType.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewfeetype.html', context)


################################################
#   CRUD FOR THE FEE COLLECTION MODULE        #
################################################
def addfeecollection(request):
    if request.method == "POST":
        form = AddFeeCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addfeecollection')
    else:
        form = AddFeeCollectionForm()
        context = {'form': form}
        return render(request, 'accounts/Accounting/addfeecollection.html', context)


def editfeecollection(request, pk):
    item = get_object_or_404(FeeCollection, id=pk)
    if request.method == "POST":
        form = EditFeeCollectionForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewfeecollection')
    else:
        form = EditFeeCollectionForm(instance=item)
        return render(request, 'accounts/Accounting/editfeecollection.html', {'form': form})


def deletefeecollection(request, pk):
    FeeCollection.objects.filter(id=pk).delete()
    all_info = FeeCollection.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/feecollection.html', context)

@login_required
def viewfeecollection(request):
    all_info = FeeCollection.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewfeecollection.html', context)


################################################
#   CRUD FOR THE FEE INCOME MODULE        #
################################################
def addincome(request):
    if request.method == "POST":
        form = AddIncomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addincome')
    else:
        form = AddIncomeForm()
        context = {'form': form}
        return render(request, 'accounts/Accounting/addincome.html', context)


def editincome(request, pk):
    item = get_object_or_404(Income, id=pk)
    if request.method == "POST":
        form = EditIncomeForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewincome')
    else:
        form = EditIncomeForm(instance=item)
        return render(request, 'accounts/Accounting/editincome.html', {'form': form})


def deleteincome(request, pk):
    Income.objects.filter(id=pk).delete()
    all_info = Income.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewincome.html', context)

@login_required
def viewincome(request):
    all_info = Income.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewincome.html', context)


################################################
#   CRUD FOR THE FEE EXPENDITURE MODULE        #
################################################
def addexpenditure(request):
    if request.method == "POST":
        form = AddExpenditureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexpenditure')
    else:
        form = AddExpenditureForm()
        context = {'form': form}
        return render(request, 'accounts/Accounting/addexpenditure.html', context)


def editexpenditure(request, pk):
    item = get_object_or_404(Expenditure, id=pk)
    if request.method == "POST":
        form = EditExpenditureForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewincome')
    else:
        form = EditExpenditureForm(instance=item)
        return render(request, 'accounts/Accounting/editexpenditure.html', {'form': form})


def deleteexpenditure(request, pk):
    Expenditure.objects.filter(id=pk).delete()
    all_info = Expenditure.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewexpenditure.html', context)

@login_required
def viewexpenditure(request):
    all_info = Expenditure.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewexpenditure.html', context)


################################################
#   CRUD FOR THE EVENTS MODULE        #
################################################
def addevents(request):
    if request.method == "POST":
        form = AddEventsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addevents')
    else:
        form = AddEventsForm()
        context = {'form': form}
        return render(request, 'accounts/Events/addevents.html', context)


def editevents(request, pk):
    item = get_object_or_404(Events, id=pk)
    if request.method == "POST":
        form = EditEventsForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewevents')
    else:
        form = EditEventsForm(instance=item)
        return render(request, 'accounts/Events/editevents.html', {'form': form})


def deleteevents(request, pk):
    Events.objects.filter(id=pk).delete()
    all_info = Events.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Events/viewevents.html', context)

@login_required
def viewevents(request):
    all_info = Events.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Events/viewevents.html', context)


################################################
#   CRUD FOR THE FEE INCOME MODULE        #
################################################
def addincome(request):
    if request.method == "POST":
        form = AddIncomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addincome')
    else:
        form = AddIncomeForm()
        context = {'form': form}
        return render(request, 'accounts/Accounting/addincome.html', context)


def editincome(request, pk):
    item = get_object_or_404(Income, id=pk)
    if request.method == "POST":
        form = EditIncomeForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewincome')
    else:
        form = EditIncomeForm(instance=item)
        return render(request, 'accounts/Accounting/editincome.html', {'form': form})


def deleteincome(request, pk):
    Income.objects.filter(id=pk).delete()
    all_info = Income.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewincome.html', context)

@login_required
def viewincome(request):
    all_info = Income.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewincome.html', context)


################################################
#   CRUD FOR THE FEE EXPENDITURE MODULE        #
################################################
def addexpenditure(request):
    if request.method == "POST":
        form = AddExpenditureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addexpenditure')
    else:
        form = AddExpenditureForm()
        context = {'form': form}
        return render(request, 'accounts/Accounting/addexpenditure.html', context)


def editexpenditure(request, pk):
    item = get_object_or_404(Expenditure, id=pk)
    if request.method == "POST":
        form = EditExpenditureForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewincome')
    else:
        form = EditExpenditureForm(instance=item)
        return render(request, 'accounts/Accounting/editexpenditure.html', {'form': form})


def deleteexpenditure(request, pk):
    Expenditure.objects.filter(id=pk).delete()
    all_info = Expenditure.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewexpenditure.html', context)

@login_required
def viewexpenditure(request):
    all_info = Expenditure.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Accounting/viewexpenditure.html', context)


################################################
#   CRUD FOR THE NOTICE MODULE                #
################################################
def addnotice(request):
    if request.method == "POST":
        form = AddNoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addnotice')
    else:
        form = AddNoticeForm()
        context = {'form': form}
        return render(request, 'accounts/Announcement/addnotice.html', context)


def editnotice(request, pk):
    item = get_object_or_404(Notice, id=pk)
    if request.method == "POST":
        form = EditNoticeForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewnotice')
    else:
        form = EditNoticeForm(instance=item)
        return render(request, 'accounts/Announcement/editnotice.html', {'form': form})


def deletenotice(request, pk):
    Notice.objects.filter(id=pk).delete()
    all_info = Notice.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Announcement/viewnotice.html', context)


def viewnotice(request):
    all_info = Notice.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Announcement/viewnotice.html', context)


################################################
#   CRUD FOR THE NEWS MODULE                #
################################################
def addnews(request):
    if request.method == "POST":
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addnews')
    else:
        form = AddNewsForm()
        context = {'form': form}
        return render(request, 'accounts/Announcement/addnews.html', context)


def editnews(request, pk):
    item = get_object_or_404(News, id=pk)
    if request.method == "POST":
        form = EditNewsForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewnews')
    else:
        form = EditNewseForm(instance=item)
        return render(request, 'accounts/Announcement/editnews.html', {'form': form})


def deletenews(request, pk):
    News.objects.filter(id=pk).delete()
    all_info = News.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Announcement/viewnews.html', context)

@login_required
def viewnews(request):
    all_info = News.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Announcement/viewnews.html', context)


################################################
#   CRUD FOR THE HOLIDAYS MODULE                #
################################################
def addholiday(request):
    if request.method == "POST":
        form = AddHolidaysForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addholiday')
    else:
        form = AddHolidaysForm()
        context = {'form': form}
        return render(request, 'accounts/Announcement/addholiday.html', context)


def editholiday(request, pk):
    item = get_object_or_404(Holiday, id=pk)
    if request.method == "POST":
        form = EditHolidaysForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewholidays')
    else:
        form = EditHolidaysForm(instance=item)
        return render(request, 'accounts/Announcement/editholiday.html', {'form': form})


def deleteholiday(request, pk):
    Holiday.objects.filter(id=pk).delete()
    all_info = Holiday.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Announcement/viewholidays.html', context)

@login_required
def viewholidays(request):
    all_info = Holiday.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Announcement/viewholidays.html', context)


################################################
#   CRUD FOR THE Profile MODULE                #
################################################
def addprofile(request):
    if request.method == "POST":
        form = AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addprofile')
    else:
        form = AddProfileForm()
        context = {'form': form}
        return render(request, 'accounts/Profile/addprofile.html', context)


def editprofile(request, pk):
    item = get_object_or_404(Profile, id=pk)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewprofile')
    else:
        form = EditProfileForm(instance=item)
        return render(request, 'accounts/Profile/editprofile.html', {'form': form})


def deleteprofile(request, pk):
    Profile.objects.filter(id=pk).delete()
    all_info = Profile.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Profile/viewprofile.html', context)

@login_required
def viewprofile(request):
    all_info = Profile.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Profile/viewprofile.html', context)


################################################
#   CRUD FOR THE SCHOOL MODULE                #
################################################
def addschool(request):
    if request.method == "POST":
        form = AddSchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addschool')
    else:
        form = AddSchoolForm()
        context = {'form': form}
        return render(request, 'accounts/School/addschool.html', context)


def editschool(request, pk):
    item = get_object_or_404(School, id=pk)
    if request.method == "POST":
        form = EditSchoolForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewschools')
    else:
        form = EditSchoolForm(instance=item)
        return render(request, 'accounts/School/editschool.html', {'form': form})


def deleteschool(request, pk):
    School.objects.filter(id=pk).delete()
    all_info = School.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/School/viewschools.html', context)

@login_required
def viewschools(request):
    all_info = School.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/School/viewschools.html', context)


#######################################
#     CRUD FOR THE TEACHER MODULE        #
#######################################

def createteacher(request):
    if request.method == "POST":
        form = CreateTeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createteacher')
        return render(request, 'accounts/Teachers/createteacher.html', {'form': form})
    else:
        form = CreateTeacherForm()
        context = {'form': form}
        return render(request, 'accounts/Teachers/createteacher.html', context)


def editteacher(request, pk):
    item = get_object_or_404(TeachersInformation, id=pk)
    if request.method == "POST":
        form = CreateTeacherForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewteachers')
    else:
        form = CreateTeacherForm(instance=item)
        return render(request, 'accounts/Teachers/editteacher.html', {'form': form})


def deleteteacher(request, pk):
    TeachersInformation.objects.filter(id=pk).delete()
    all_info = TeachersInformation.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Teachers/viewteacher.html', context)

@login_required
def viewteachers(request):
    all_info = TeachersInformation.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Teachers/viewteacher.html', context)


def singleteacherdetails(request, pk):
    all_info = TeachersInformation.objects.filter(id=pk)
    context = {'all_info': all_info}
    return render(request, 'accounts/Teachers/singleteacherdetails.html', context)


################################################
#   CRUD FOR THE STUDENTS MODULE                #
################################################
def addstudent(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addstudent')
        return render(request, 'accounts/Students/addstudent.html', {'form': form})
    else:
        form = AddStudentForm()
        context = {'form': form}
        return render(request, 'accounts/Students/addstudent.html', context)


def editstudent(request, pk):
    item = get_object_or_404(DataStudent, id=pk)
    if request.method == "POST":
        form = EditStudentForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('viewstudents')
    else:
        form = EditStudentForm(instance=item)
        return render(request, 'accounts/Students/editstudent.html', {'form': form})


def deletestudent(request, pk):
    DataStudent.objects.filter(id=pk).delete()
    all_info = DataStudent.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Students/viewstudents.html', context)

@login_required
def viewstudents(request):
    all_info = DataStudent.objects.all()
    context = {'all_info': all_info}
    return render(request, 'accounts/Students/viewstudents.html', context)


################################################
#         STUDENT ATTENDANCE MODULE               #
################################################
@login_required
def studentattendance(request):
    time = datetime.now()
    queryset = StudentPresence.objects.all()
    context = {'queryset': queryset, 'time': time}
    return render(request, 'accounts/Attendance/studentattendance.html', context)


################################################
#         SINGLE STUDENT INFORMATION               #
################################################
@login_required
def singlestudentdetails(request, pk):
    all_info = DataStudent.objects.filter(id=pk)
    context = {'all_info': all_info}
    return render(request, 'accounts/Students/singlestudentdetails.html', context)

@login_required
def guardianofstudentdetails(request, pk):
    all_info = DataStudent.objects.filter(id=pk)
    context = {'all_info': all_info}
    return render(request, 'accounts/Students/guardianofstudentdetails.html', context)

@login_required
def parentofstudentdetails(request, pk):
    all_info = DataStudent.objects.filter(id=pk)
    context = {'all_info': all_info}
    return render(request, 'accounts/Students/parentofstudentdetails.html', context)

    ################################################
    #     STUDENT  VIEWING HIS OR HER CLASS           #
    ################################################

@login_required
def studentsinaclass1(request):
    all_classes = Classinformation.objects.all()
    all_info = DataStudent.objects.filter(Class=all_classes[0])
    context = {'all_info': all_info, 'all_classes': all_classes}
    return render(request, 'accounts/StudentClass/view_form_one_students.html', context)

@login_required
def studentsinaclass2(request):
    all_classes = Classinformation.objects.all()
    all_info = DataStudent.objects.filter(Class=all_classes[1])
    context = {'all_info': all_info}
    return render(request, 'accounts/StudentClass/view_form_two_students.html', context)

@login_required
def studentsinaclass3(request):
    all_classes = Classinformation.objects.all()
    all_info = DataStudent.objects.filter(Class=all_classes[2])
    context = {'all_info': all_info}
    return render(request, 'accounts/StudentClass/view_form_three_students.html', context)

@login_required
def studentsinaclass4(request):
    all_classes = Classinformation.objects.all()
    all_info = DataStudent.objects.filter(Class=all_classes[3])
    context = {'all_info': all_info}
    return render(request, 'accounts/StudentClass/view_form_four_students.html', context)

@login_required
def studentsinaclass5(request):
    all_classes = Classinformation.objects.all()
    all_info = DataStudent.objects.filter(Class=all_classes[4])
    context = {'all_info': all_info}
    return render(request, 'accounts/StudentClass/view_form_five_students.html', context)

@login_required
def studentsinaclass6(request):
    all_classes = Classinformation.objects.all()
    all_info = DataStudent.objects.filter(Class=all_classes[5])
    context = {'all_info': all_info}
    return render(request, 'accounts/StudentClass/view_form_six_students.html', context)

    ################################################
    #     STUDENT  VIEWING HIS OR HER CLASS SUBJECTS   #
    ################################################

@login_required
def subjectsinaclass1(request):
    all_classes = Classinformation.objects.all()
    all_subjects = Subjects.objects.filter(Class=all_classes[0])
    context = {'all_subjects': all_subjects, 'all_classes': all_classes}
    return render(request, 'accounts/Subject/view_form_one_subjects.html', context)

@login_required
def subjectsinaclass2(request):
    all_classes = Classinformation.objects.all()
    all_subjects = Subjects.objects.filter(Class=all_classes[1])
    context = {'all_subjects': all_subjects, 'all_classes': all_classes}
    return render(request, 'accounts/Subject/view_form_two_subjects.html', context)

@login_required
def subjectsinaclass3(request):
    all_classes = Classinformation.objects.all()
    all_subjects = Subjects.objects.filter(Class=all_classes[2])
    context = {'all_subjects': all_subjects, 'all_classes': all_classes}
    return render(request, 'accounts/Subject/view_form_three_subjects.html', context)

@login_required
def subjectsinaclass4(request):
    all_classes = Classinformation.objects.all()
    all_subjects = Subjects.objects.filter(Class=all_classes[3])
    context = {'all_subjects': all_subjects, 'all_classes': all_classes}
    return render(request, 'accounts/Subject/view_form_four_subjects.html', context)

@login_required
def subjectsinaclass5(request):
    all_classes = Classinformation.objects.all()
    all_subjects = Subjects.objects.filter(Class=all_classes[4])
    context = {'all_subjects': all_subjects, 'all_classes': all_classes}
    return render(request, 'accounts/Subject/view_form_five_subjects.html', context)

@login_required
def subjectsinaclass6(request):
    all_classes = Classinformation.objects.all()
    all_subjects = Subjects.objects.filter(Class=all_classes[5])
    context = {'all_subjects': all_subjects, 'all_classes': all_classes}
    return render(request, 'accounts/Subject/view_form_six_subjects.html', context)

@login_required
def viewsinglesubjectsinclassdetails(request, pk):
    all_info = Subjects.objects.filter(id=pk)
    context = {'all_info': all_info}
    return render(request, 'accounts/Subject/viewsinglesubjectsinclassdetails.html', context)
