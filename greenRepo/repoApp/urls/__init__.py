from django.urls import path, include
from django.conf.urls import url
from repoApp.views.populate import PopulateView, PopulateDummyTest, PopulationReset
from repoApp.views.appRelated import ImportListView
from repoApp.views.views import AllMetricsListView
from repoApp.views.devices import DeviceStateView
from django.views.generic import TemplateView

from repoApp.views.register_views import RegisterView, VerifyEmailView
from repoApp.views.login_view import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = [
	path('projects/', include('repoApp.urls.projects')),
    path('results/', include('repoApp.urls.results')),
    path('tests/', include('repoApp.urls.tests')),
    path('devices/', include('repoApp.urls.devices')),
    path('devicestate/', DeviceStateView.as_view(), name='devstate'),
    path('apps/', include('repoApp.urls.apps')),
    path('methods/', include('repoApp.urls.methods')),
    path('classes/', include('repoApp.urls.classes')),
    path('resetpopulation/', PopulationReset.as_view(), name='populatereset'),
    path('populate/', PopulateView.as_view(), name='populate'),
    path('populateTest/', PopulateDummyTest.as_view(), name='pop'),
    path('imports/', ImportListView.as_view(), name='imports'),
    path('metrics/', AllMetricsListView.as_view(), name='metrics'),

    url(r'^password/reset/$', PasswordResetView.as_view(),name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),name='rest_password_reset_confirm'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),name='rest_password_change'),
    url(r'^register/$', RegisterView.as_view(), name='rest_register'),
    url(r'^register/verify-email/$', VerifyEmailView.as_view(), name='rest_verify_email'),

    # This url is used by django-allauth and empty TemplateView is
    # defined just to allow reverse() call inside app, for example when email
    # with verification link is being sent, then it's required to render email
    # content.

    # account_confirm_email - You should override this view to handle it in
    # your API client somehow and then, send post to /verify-email/ endpoint
    # with proper key.
    # If you don't want to use API on that step, then just use ConfirmEmailView
    # view from:
    # django-allauth https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py
    url(r'^register/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email'),
]