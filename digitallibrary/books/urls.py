from books import views
from django.urls import path

urlpatterns = [
    path('AddBooks/', views.addbooks,name='addbooks'),
    path('Checkout/', views.checkout,name='checkout'),
    path('remove/<book_num>',views.removebooks,name='removebooks'),
    path('checkedout/',views.checkout1,name='checkedout'),
    path('returnbooks/', views.returnbooks,name='returnbooks'),
    path('ViewBooks/',views.viewbooks,name='viewbooks'),
    path('returned/',views.returnbooks1,name='returned'),
    path('StudentView/',views.viewbooks2,name='viewbooks2'),
    

]
