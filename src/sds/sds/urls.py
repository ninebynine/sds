"""
Annalist application URL definitions
"""

__author__      = "Graham Klyne (GK@ACM.ORG)"
__copyright__   = "Copyright 2014, G. Klyne"
__license__     = "MIT (http://opensource.org/licenses/MIT)"

from django.conf.urls           import patterns, url

from sds.views                  import SdsHomeView, SdsSheetView, SdsRowView

urlpatterns = patterns('',
    url(r'^$',      SdsHomeView.as_view(),  name='SdsHomeView'),
    url(r'^(?P<sheet_id>\w{0,32})/$',
                    SdsSheetView.as_view(), name='SdsSheetView'),
    url(r'^(?P<sheet_id>\w{0,32})/(?P<row_id>\w{0,32})/$',
                    SdsRowView.as_view(), name='SdsRowView'),
    )

# End.
