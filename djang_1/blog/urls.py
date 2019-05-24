from django.conf.urls import url
from django.urls import path

import blog.views

urlpatterns = [
    # url(r"^$", view.hello3)
    # path['hello', blog.views.hello]
    path("hello", blog.views.hello),
    path("content", blog.views.article_content),
    path("index", blog.views.get_index_page),
    # url("detail", blog.views.get_detail_page),
    path('detail/<int:article_id>', blog.views.get_detail_page)

]
