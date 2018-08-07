from django.conf.urls import url
from api.views import course
urlpatterns = [
    url(r'DegreeCourseTeacher/$', course.DegreeCourseTeacherView.as_view()),
    url(r'DegreeCourseScholarshipr/$', course.DegreeCourseScholarshiprView.as_view()),
    url(r'Course/$', course.CourseView.as_view()),
    url(r'DegreeCourseTemplate/$', course.DegreeCourseTemplateView.as_view()),
    url(r'DegreeCourseDetaile/$', course.DegreeCourseDetaileView.as_view()),
    url(r'DegreeCourseOftenAskedQuestion/$', course.DegreeCourseOftenAskedQuestionView.as_view()),
    url(r'DegreeCourseCourseOutlinen/$', course.CoursesCourseoutlineView.as_view()),
    url(r'CoursesChapter/$', course.CoursesChapterView.as_view()),
    # url(r'courses/(?P<pk>\d+)/$',course.DegreeCourseScholarshiprView.as_view())
]