from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogListView(ListView):
    model = Post
    template_name = 'blogging/post_list.html'
    queryset = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    # context = {'posts': Post.objects.all()}
    # template = loader.get_template('blogging/list.html')
    # body = template.render(context)

    # context = {"object": Post}

class BlogDetailView(DetailView):
    model = Post
    template = 'blogging/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        context = {"object": post}
        return render(request, self.template, context)
# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")
#
#
# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)
#
#
# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/post_detail.html', context)
