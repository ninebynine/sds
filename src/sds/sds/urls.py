"""
Annalist application URL definitions
"""

__author__      = "Graham Klyne (GK@ACM.ORG)"
__copyright__   = "Copyright 2014, G. Klyne"
__license__     = "MIT (http://opensource.org/licenses/MIT)"

from django.conf.urls           import patterns, url

from sds.views                  import SdsHomeView

urlpatterns = patterns('',
    url(r'^$',              SdsHomeView.as_view(), name='SdsHomeView'),
    )

# End.
