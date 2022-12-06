from django.urls import path
from .import views

app_name = "js"

urlpatterns = [
    path('largest',views.js_largest, name="largest"),
    path('secondlg',views.js_secondlg, name="secondlg"),
    path('search1',views.js_search1, name="search1"),
    path('howtimes',views.js_howtimes, name="howtimes"),
    path('palindrome',views.js_palindrome, name="palindrome"),
   
 
    


]  