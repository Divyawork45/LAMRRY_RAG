from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'student-dashboard.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'main.html', {'courses': courses})

@login_required(login_url='/login/')
def course_detail(request):
    # course = get_object_or_404(Course)
    return render(request, 'course-details.html')

@login_required(login_url='/login/')
def course_detail2(request):
    # course = get_object_or_404(Course)
    return render(request, 'course-details-2.html')

@login_required(login_url='/login/')
def course_detail3(request):
    # course = get_object_or_404(Course)
    return render(request, 'course-details-3.html')

@login_required(login_url='/login/')
def lesson_detail(request):
    # lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'lesson.html', {'course': 'Python'})

@login_required(login_url='/login/')
def lesson_detail2(request):
    # lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'lesson2.html', {'course': 'React'})

@login_required(login_url='/login/')
def lesson_detail3(request):
    # lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'lesson3.html', {'course': 'NodeJS'})

@login_required(login_url='/login/')
def lesson_quiz(request):
    previous_url = request.META.get('HTTP_REFERER', None)
    previous_url = previous_url.split('/')[-1] if previous_url else None
    get_course = {'lesson': 'Python', 'lesson-react': 'React', 'lesson-nodejs': 'Nodejs'}
    course_name = get_course.get(previous_url, 'Unknown')
    if course_name != "Unknown":
        request.session['course'] = course_name 
    return render(request, 'lesson-quiz.html', {'course': request.session.get('course')})

@login_required(login_url='/login/')
def lesson_quiz_result(request):
    # lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'lesson-quiz-result.html', {'course': request.session.get('course')})

@login_required(login_url='/login/')
def lesson_intro(request):
    # lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'lesson-intro.html')

@login_required(login_url='/login/')
def student_course(request):
    # lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'student-enrolled-courses.html')

@login_required(login_url='/login/')
def student_quiz(request):
    # lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'student-my-quiz-attempts.html')
