from django.conf.urls import url

from . import db, views
from .views import *

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^tables/create/?$', db.create_tables, name='create_tables'),
  url(r'^tables/drop/?$', db.drop_tables, name='drop_tables'),
  url(r'^tables/load/?$', db.initiate_insert_into_tables, name='load_tables'),

  url(r'^camera/create/?$', db.create_camera, name='camera_create'),
  url(r'^camera/load/?$', db.initiate_insert_into_camera, name='camera_insert'),
  # url(r'^camera/list/all/?$', db.select_all_camera, name='camera_select_all'),
  url(r'^camera/list/filter/$', FilterCameraListView.as_view(),
      name='camera_list_filter'),

  url(r'^photographer/create/?$', db.create_photographer,
      name='photographer_create'),
  url(r'^photographer/load/?$', db.initiate_insert_into_photographer,
      name='photographer_insert'),
  # url(r'^photographer/list/all/?$', db.select_all_photographer,
  #     name='photographer_select_all'),
  url(r'^photographer/list/filter/$', FilterPhotographerListView.as_view(),
      name='photographer_list_filter'),

  url(r'^location/create/?$', db.create_location, name='location_create'),
  url(r'^location/load/?$', db.initiate_insert_into_location,
      name='location_insert'),
  # url(r'^location/list/all/?$', db.select_all_location,
  #     name='location_select_all'),
  url(r'^location/list/filter/$', FilterLocationListView.as_view(),
      name='location_list_filter'),

  url(r'^photographer_camera/create/?$', db.create_photographer_camera,
      name='photographer_camera_create'),
  url(r'^photographer_camera/load/?$',
      db.initiate_insert_into_photographer_camera,
      name='photographer_camera_insert'),

  url(r'^photographer_location/create/?$', db.create_photographer_location,
      name='photographer_location_create'),
  url(r'^photographer_location/load/?$',
      db.initiate_insert_into_photographer_location,
      name='photographer_location_insert'),

  url(r'^photo/create/?$', db.create_photo, name='photo_create'),
  url(r'^photo/clicked/?$', views.on_click_photo, name='on_click_photo'),
  url(r'^photo/new/$', views.new_photo, name='new_photo'),
  url(r'^photo/edit/(?P<photo_id>[0-9]+)/$', views.edit_photo,
      name='edit_photo'),
  url(r'^photo/delete/(?P<photo_id>[0-9]+)/$', views.delete_photo,
      name='delete_photo'),
  url(r'^photo/list/all/?$', PhotoListView.as_view(), name='photo_list'),
  url(r'^photo/list/filter/?$', FilterPhotoListView.as_view(),
      name='photo_list_filter'),
]
