from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView

from anaruiz.apps.blog import models
from anaruiz.apps.blog import forms


class Single(DetailView):
    model = models.Post
    template_name = 'blog/single.html'


def index(request):
    post_list = models.Post.objects.filter(
        date__lte=timezone.now()
    ).order_by('-date')

    random_list = models.Post.objects.order_by('?')[:4]
    random_mini_list = models.Post.objects.order_by('?')[:4]

    template = loader.get_template('blog/index.html')

    context = {
        'post_list': post_list,
        'random_list': random_list,
        'random_mini_list': random_mini_list,
    }

    return HttpResponse(template.render(context, request))


def member(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newPic = models.Imagen(imgFile=request.FILES['imgFile'])
            newPic.save()

            return HttpResponseRedirect(reverse('member'))
    else:
        form = forms.ImageForm()

    images = models.Imagen.objects.all()

    return render(request, 'blog/member.html', {'images': images, 'form': form})
