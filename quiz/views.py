from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from quiz import models,forms


# Create your views here.

def home(request):  # sourcery skip: extract-method, remove-unnecessary-else
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method=="POST":
        print(request.POST)
        questions = models.QuestionsModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        
        total = 0
        
        for q in questions:
            total+=1
            
            # print(request.POST.get(q.question))
            # print(q.ans)
            # print()
            lookup={"option1":"op1","option2":"op2","option3":"op3","option4":"op4"}
            
            answer = lookup[request.POST.get(q.question)]
            items = vars(q)
            
            if q.ans == items[answer]:
                correct+=1
                score+=10
            else:
                wrong +=1
        
        percent = score/(total*10) *100
        
        context = {
            'score' : score,
            'correct' : correct,
            'wrong' : wrong,
            'total' : total,
            'percent' : percent,
            'time' : request.POST.get('timer')
        }
        
        return render(request, "result.html", context)
    
    else:
        questions = models.QuestionsModel.objects.all()
        context ={
            'questions' : questions
        }
        
        return render(request, "home.html", context)


def addQuestion(request):
    if not request.user.is_staff:
        return redirect("home")
    
    form = forms.addQuestionForm()
    if request.method == "POST":
        form = forms.addQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request, "addQuestion.html", context)
        
        
def registerPage(request):
    if request.user.is_authenticated:
        redirect("home")
    else:
        form = forms.createUserForm()
        if request.method=="POST":
            form = forms.createUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("login")
        
        context = {'form':form}
        
        return render(request, "registerPage.html", context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
        context ={}
        return render(request,"login.html", context)
                
            

def logoutUser(request):
    logout(request)
    return redirect("/")