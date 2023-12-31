from django.urls import path
from bookrequest.views import show_json, show_json_all, show_request_page, create_request, remove_request, update_request, create_request_flutter
from bookrequest.views import get_request_item_json
from home.views import logout_user

app_name = 'bookrequest'

urlpatterns = [
    path('', show_request_page, name='show_request_page'),
    path('../logout/', logout_user, name='logout'),
    path('get-request-item/', get_request_item_json, name='get_request_item_json'),
    path('create-request/', create_request, name='create_request'),
    path('remove-request/<int:id>/', remove_request, name='remove_request'),
    path('update-request/<int:id>/', update_request, name='update_request'),
    path('create-flutter/', create_request_flutter, name='create_product_flutter'),
    path('json/', show_json, name='show_json'),
    path('json-all/', show_json_all, name='show_json_all'),
    ]