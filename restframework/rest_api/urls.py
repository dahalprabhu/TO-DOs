from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from django.urls import include
from . views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('post', PostViewSet, basename='post') --> viewset
# router.register('post', GenericPostViewSet, basename='post') --> GenericViewset
router.register('post', ModelPostViewSet, basename='post')  # --> ModelViewset

urlpatterns = [

    # Router
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # Generic
    # path('generic/post/<int:id>/', GenericPostView.as_view())

    # Class based
    # path('post/', PostView.as_view()),
    # path('post/<int:id>/', PostDetail.as_view())

    # Function based
    # path('post/', post_list, name='post'),
    # path('detail/<int:pk>/', post_detail),
]
