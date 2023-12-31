from django.urls import path
from home.views import home, user_home
from home.views import logout_user, login_user
from home.views import register, show_review_page
from home.views import register
from userprofile.views import show_userprofile
from bookrequest.views import show_request_page
from loans.views import show_loans_page
from collection.views import show_collection

urlpatterns = [
    path('', home, name='home'),
    path('user-page/', user_home, name='user_home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('userprofile/', show_userprofile, name='userprofile'),
    path('book-review/', show_review_page, name='show_review_page'),
    path('../book-request/', show_request_page, name='show_request_page'),
    path('../show_loans/', show_loans_page, name='show_loans_page'),
    path('../show_collection/', show_collection, name='show_collection'),
]