from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

from .forms import *
from .models import *


def index(request):
  return HttpResponseRedirect('/photo/list')


def on_click_photo(request):
  if request.method == 'POST':
    if 'editbtn' in request.POST:
      url = reverse('edit_photo', kwargs={'photo_id':
                                            request.POST['tableradio']})
      return HttpResponseRedirect(url)
    if 'deletebtn' in request.POST:
      url = reverse('delete_photo', kwargs={'photo_id':
                                              request.POST['tableradio']})
      return HttpResponseRedirect(url)
  return HttpResponseBadRequest()


class PhotoController:
  @staticmethod
  def create(request):
    if request.method == 'GET':
      form = PhotoForm()
    elif request.method == 'POST':
      form = PhotoForm(request.POST)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/photo/list/')
    return render(request, 'photo/form.html', {'form': form})

  @staticmethod
  def update(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    if request.method == 'GET':
      form = PhotoForm(instance=photo)
    elif request.method == 'POST':
      form = PhotoForm(request.POST, instance=photo)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/photo/list/')
    return render(request, 'photo/form.html', {'form': form})

  @staticmethod
  def delete(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    messages.add_message(request, messages.WARNING, )
    photo.delete()
    return HttpResponseRedirect('/photo/list/')


class PhotoListView(ListView):
  template_name = 'photo/list.html'
  model = Photo

  def get_context_data(self, **kwargs):
    context = super(PhotoListView, self).get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context


class FormListView(FormMixin, ListView):
  def get(self, request, *args, **kwargs):
    # From ProcessFormMixin
    form_class = self.get_form_class()
    self.form = self.get_form(form_class)

    # From BaseListView
    self.object_list = self.get_queryset()
    allow_empty = self.get_allow_empty()
    if not allow_empty and len(self.object_list) == 0:
      raise Http404(u"Empty list and '%(class_name)s.allow_empty' is False."
                    % {'class_name': self.__class__.__name__})

    context = self.get_context_data(object_list=self.object_list,
                                    form=self.form)
    return self.render_to_response(context)

  def post(self, request):
    # From ProcessFormMixin
    self.form = self.get_form_class()(request.POST)
    if self.form.is_valid():
      self.cleaned_data = self.form.cleaned_data

    # From BaseListView
    self.object_list = self.get_queryset()
    allow_empty = self.get_allow_empty()
    if not allow_empty and len(self.object_list) == 0:
      raise Http404(u"Empty list and '%(class_name)s.allow_empty' is False."
                    % {'class_name': self.__class__.__name__})

    context = self.get_context_data(object_list=self.object_list,
                                    form=self.form)
    return self.render_to_response(context)


class FilterCameraListView(FormListView):
  form_class = CameraAttributesForm
  template_name = 'camera/list_filtered.html'

  def get_context_data(self, **kwargs):
    context = super(FilterCameraListView, self).get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context

  def get_queryset(self):
    if hasattr(self, 'cleaned_data'):
      date_created_from = self.cleaned_data.get('date_created_from')
      date_created_to = self.cleaned_data.get('date_created_to')
      version = self.cleaned_data.get('version')
      q = Q()
      if date_created_from is not None:
        q = q | Q(year_created__gte=date_created_from)
      if date_created_to is not None:
        q = q | Q(year_created__lte=date_created_to)
      if version is not None:
        q = q | Q(version=version)
      return Camera.objects.filter(q)
    return Camera.objects.all()


class FilterLocationListView(FormListView):
  form_class = LocationAttributesForm
  template_name = 'location/list_filtered.html'

  def get_context_data(self, **kwargs):
    context = super(FilterLocationListView, self).get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context

  def get_queryset(self):
    if hasattr(self, 'cleaned_data'):
      return Location.objects.filter(self.cleaned_data)
    return Location.objects.all()


class FilterPhotographerListView(FormListView):
  form_class = PhotographerAttributesForm
  template_name = 'photographer/list_filtered.html'

  def get_context_data(self, **kwargs):
    context = super(FilterPhotographerListView, self).get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context

  def get_queryset(self):
    if hasattr(self, 'cleaned_data'):
      print self.cleaned_data
      return Photographer.objects.filter(self.cleaned_data)
    return Photographer.objects.all()


class FilterPhotoListView(FormListView):
  form_class = PhotoSearchForm
  template_name = 'photo/list_filtered.html'

  def get_context_data(self, **kwargs):
    context = super(FilterPhotoListView, self).get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context

  def get_queryset(self):
    if hasattr(self, 'cleaned_data'):
      return Photo.objects.filter(self.cleaned_data)
    return Photo.objects.get()
