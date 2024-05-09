from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('dashboard', views.dashboard, name='student_dashboard'),  # Home page with list of courses
    path('course-details', views.course_detail, name='course_detail'),
    path('course-details-2', views.course_detail2, name='course_detail2'),
    path('course-details-3', views.course_detail3, name='course_detail3'),
    # path('course/<int:id>/', views.course_detail, name='course_detail'),  # Course detail page
    path('lesson', views.lesson_detail, name='lesson_detail'),
    path('lesson-react', views.lesson_detail2, name='lesson_detail2'),
    path('lesson-nodejs', views.lesson_detail3, name='lesson_detail3'),
    path('lesson-quiz', views.lesson_quiz, name='lesson_quiz'),
    path('lesson-quiz-result', views.lesson_quiz_result, name='lesson_quiz_result'),
    # path('lesson-assign', views.lesson_assign, name='lesson_assign'),
    # path('lesson-assign-submit', views.lesson_assign_submit, name='lesson_assign_submit'),
    path('lesson-intro', views.lesson_intro, name='lesson_intro'),
    path('student-course', views.student_course, name='student_course'),
    path('student-quiz', views.student_quiz, name='student_quiz'),
]