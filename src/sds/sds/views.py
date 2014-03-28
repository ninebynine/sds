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

from sds.models                     import resource_ids, resource_data

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
        # log.info("SdsHomeView.get: site_data %r"%(self.site_data()))
        render_context = { "files": [f for f in resource_ids(settings.DATA_DIR)] }
        return (
            # self.authenticate() or 
            # self.authorize("VIEW") or 
            self.render_html(render_context, 'sds_home.html') or 
            self.error(self.error406values())
            )


class SdsSheetView(SdsGenericView):
    """
    View class for spreadsheet view
    """
    def __init__(self):
        super(SdsSheetView, self).__init__()
        return

    def get(self, request, sheet_id=None):
        """
        Create a rendering of an entire spreadsheet ... display 1st 10 rows
        """
        # log.info("SdsSheetView.get: site_data %r"%(self.site_data()))
        (spath, stype, sgrid) = resource_data(settings.DATA_DIR, self.get_request_uri(), sheet_id)
        log.info("resource_data %s, %s"%(spath, stype))
        render_context = (
            { "filepath": spath
            , "filetype": stype
            , "gridhead": sgrid[0]
            , "griddata": sgrid.rows(1,20000)
            })
        log.info("render_context %s, %s"%(spath, stype))
        return (
            # self.authenticate() or 
            # self.authorize("VIEW") or 
            self.render_html(render_context, 'sds_sheet.html') or 
            self.render_csv(render_context, 'sds_sheet.html') or 
            self.render_json(render_context, 'sds_sheet.html') or 
            self.error(self.error406values())
            )


class SdsRowView(SdsGenericView):
    """
    View class for spreadsheet view
    """
    def __init__(self):
        super(SdsRowView, self).__init__()
        return

    def get(self, request, sheet_id=None):
        """
        Create a rendering of an entire spreadsheet ... display 1st 10 rows
        """
        # log.info("SdsRowView.get: site_data %r"%(self.site_data()))
        render_context = (
            { "filepath": spath
            , "filetype": stype
            , "griddata":  [ [ c for c in r] for r in sgrid]
            })
        return (
            # self.authenticate() or 
            # self.authorize("VIEW") or 
            self.render_html(render_context, 'sds_sheet.html') or 
            self.error(self.error406values())
            )




# End.
