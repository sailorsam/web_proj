from qa.views import test
from django.conf.urls import patterns, url

urlpatterns = patterns('qa.views',
    url(r'^$', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<num>\d+)/', test),
    url(r'^ask', test),
    url(r'^popular/', test),
    url(r'^new/', test),
)

