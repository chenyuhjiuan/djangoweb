from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = patterns('',
                        url(r'^$', ListView.as_view(
                            queryset=Post.objects.all().order_by("-date")[:7],
                            template_name="home.html")),
                       
                        url(r'^blog/$', ListView.as_view(
                            queryset=Post.objects.all().order_by("-date")[:6],
                            template_name="blog.html")),

			url(r'^blog/(?P<pk>\d+)/$', DetailView.as_view(
			    model = Post,
			    template_name="post.html")),
					
			url(r'^blog/archieves/$', ListView.as_view(
			    queryset=Post.objects.all().order_by("-date"),
			    template_name="posttitleslist.html")),
					
					
			#url(r'^latestnews/$', ListView.as_view(
			#	queryset=Post.objects.all().order_by("-date")[:10],
			#	template_name="posttitleslist.html")),
	    )
