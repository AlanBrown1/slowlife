"""slowlife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

# 引入whole这个app的views.py
from whole import views as whole_views

urlpatterns = [
    # 返回首页
    url(r'^$', whole_views.home),
	url(r'^home$', whole_views.home, name='home'),
    # 返回主导航栏对应的页面
	url(r'^mainpage/([-a-zA-Z\_]+)/($|p[0-9]+)/', whole_views.mainpage, name='mainpage'),
    # 返回次导航栏对应的页面
    url(r'^subpage/([-a-zA-Z\_]+)/($|p[0-9]+)/', whole_views.subpage, name='subpage'),
    #  返回关于我们的页面
    url(r'^aboutus/([-a-zA-Z\_]+)/', whole_views.aboutus, name='aboutus'),
    # 返回某篇文章的页面
    url(r'^article/([-a-zA-Z\_]+)/([0-9]+)/' ,whole_views.article, name='article'),
    # 返回慢推荐(发现美)页面
    url(r'^manrecommend/', whole_views.manrecommend, name='manrecommend'),
    # 点赞功能(没有页面,使用的ajax)
    url(r'^zan/', whole_views.zan, name='zan'),
    # 主导航栏对应页面的分页功能（没有页面，使用的ajax把跳转地址传到前端
    url(r'#gemaintpage/', whole_views.getMainPage, name='getmainpage'),
    # 次导航栏对应页面的分页功能（没有页面，使用的ajax把跳转地址传到前端
    url(r'#gesubtpage/', whole_views.getSubPage, name='getsubpage'),
    # 处理意见反馈
    url(r'^advise/', whole_views.advise),

    url(r'^admin/', admin.site.urls),
]


# 如果是DEBUG状态，就加上媒体路径
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )

# 在whole这个app的views.py里面定义了返回404页面的page_not_found函数
# handler404 = whole_views.page_not_found