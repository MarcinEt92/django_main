from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="backend_index"),
    path("php_tutorial/", views.php_tutorial, name="php_tutorial"),
    path("php_tutorial/cookies/", views.cookies, name="cookies"),
    path("php_tutorial/cookies/process_order/", views.process_order, name="process_order"),
    path("php_tutorial/cookies/summary/<int:order_id>", views.summary, name="summary"),
    path("to_do_list/", views.to_do_list, name="to_do_list"),
    path("to_do_list/new_list/", views.new_list, name="new_list"),
    path("to_do_list/<int:list_id>", views.specific_list, name="specific_list"),
    # path("to_do_list/append_list/<int:list_id>", views.append_list, name="append_list"),
]
