"""
SDS home page view definition
"""

__author__      = "Graham Klyne (GK@ACM.ORG)"
__copyright__   = "Copyright 2014, G. Klyne"
__license__     = "MIT (http://opensource.org/licenses/MIT)"

import logging
log = logging.getLogger(__name__)

from django.conf                    import settings
from django.http                    import HttpResponse
from django.http                    import HttpResponseRedirect

from sds.GenericView                import SdsGenericView

class SdsHomeView(SdsGenericView):
    """
    View class for home view
    """
    def __init__(self):
        super(SdsHomeView, self).__init__()
        return

    def get(self, request):
        """
        Create a rendering of the SDS site home page, containing (among other things)
        a list of defined collections.
        """
        # log.info("SiteView.get: site_data %r"%(self.site_data()))
        return (
            # self.authenticate() or 
            # self.authorize("VIEW") or 
            self.render_html({}, 'sds_home.html') or 
            self.error(self.error406values())
            )

# End.
