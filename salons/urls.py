from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from . import views 

urlpatterns = [
     path('', views.temp, name='temp'),
     path('home/', views.home, name='home'),
     path('salon/<int:id>', views.salon_details, name='salon_details'),
    #  path('user_home', views.user_home, name='user_home'),
     path('login/', views.login_page, name='login_page'),
      path('change_password/', views.change_password, name='chnage_pass'),
     path('register/', views.registerPage, name='register_page'),
     path('addworker/<int:id>', views.worker_registerPage, name='worker_register_page'),
     path('addservice/<int:id>', views.service_registerPage, name='service_register_page'),
     path('workers&serivices/<int:id>', views.workers_services, name='all_sw'),
     path('business_register/', views.business_registerPage, name='busineess_register_page'),
     path('logout/', views.logoutuser, name='logoutuser'),
     path('selectoption/', views.register_option, name='resgisteroption'),
     
     path('controller_home/', views.admin_home, name='admin_home'),
      path('approved/<int:id>', views.approve_salon, name='approve_salon'),


     path('salon_admin/', views.salon_user_page, name='salon_user'), 
     path('salon_profile/', views.salon_user_setting, name='salon_settings'), 
     path('salon_page/<int:id>', views.salon_view, name='salon_page'),
     path('add_new_slot/<int:id>', views.add_slot, name='add_slot'), 
     path('edit_slot/<int:id>', views.edit_slot, name='edit_slot'), 

     path('add_new_worker/<int:id>', views.add_worker, name='new_worker'), 
     path('edit_worker/<int:id>', views.edit_worker, name='edit_worker'), 

     path('add_new_service/<int:id>', views.add_service, name='new_service'),
     path('edit_service/<int:id>', views.edit_service, name='edit_service'),

     path('add_product/<int:id>', views.add_new_product, name='add_product'),
     path('edit_product/<int:id>', views.edit_product, name='edit_product'),

     path('worker_slots/<int:id>', views.worker_slots, name='worker_slots'), 
     path('assign_worker/<int:id>', views.assign_worker, name='assign_worker'),
     path('complete_product_order/<int:id>', views.product_order_status, name='po_complete'),
     


      path('new_order/<int:id>', views.new_order, name='order'),
      path('cart/', views.cart, name='cart'),
      path('order_now/', views.order_now, name='order_now'),
      path('myappointments/', views.all_appointments, name='appointments'),
      path('order_status/<int:id>', views.change_order_status, name='complete_order_status'),
      path('cancel_order/<int:id>', views.cancel_order, name='cancel'),
       path('deleteproduct/<int:id>', views.removefromcart, name='removefc'),



     path('new_product_order/<int:id>', views.new_product_order, name='product_order'),
     path('change_quantity/<int:id>', views.changeorderquantity, name='change_quantity'),

     
     path('ask_an_expert/', views.all_queries, name='query_page'),
     path('new_query/', views.ask_question, name='quetion_page'),
     path('answer_query/<int:id>', views.answer_query, name='answer_page'),


     path('expert_dashboard/', views.expert_home, name='expert_home'),
   
    
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)