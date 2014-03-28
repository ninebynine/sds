"""
SDS models
"""

__author__      = "Graham Klyne (GK@ACM.ORG)"
__copyright__   = "Copyright 2014, G. Klyne"
__license__     = "MIT (http://opensource.org/licenses/MIT)"

import logging
log = logging.getLogger(__name__)

import os
import re

from django.db import models

from grid.grid import GridCSV, GridTSV, GridExcel

# Create your models here.

def valid_id(id):
    """
    Checks the supplied id is valid as a identifier.

    The main requirement is that it is valid as a URI path segment, so it can be used
    in the creation of URIs for resources.

    >>> valid_id("abcdef_1234")
    True
    >>> valid_id("abcdef/1234")
    False
    """
    reserved = ([])
    if id and re.match(r"\w+$", id):
        return id not in reserved
    return False

def resource_ids(dir):
    if os.path.isdir(dir):
        files = os.listdir(dir)
        for f in files:
            if valid_id(f):
                yield f
    return

def resource_data(basedir, baseuri, resource_id):
    """
    Get spreadsheet resource data.

    basedir     is the base directory containing the required data
    resource_id is the identifier of the required spreadsheet resource

    returns (spath, stype, sgrid), or None

    where sgrid is a grid object for accessing the data, 
    and stype is a string describibng the data file type
    """
    spreadsheet_types = (
        ("spreadsheet.xls", "Excel", GridExcel),
        ("spreadsheet.xlsx", "Excel", GridExcel),
        ("spreadsheet.csv", "CSV",   GridCSV),
        ("spreadsheet.tsv", "TSV",   GridTSV),
        )
    for (fn, ft, gridcls) in spreadsheet_types:
        filepath = os.path.join(basedir, resource_id, fn)
        if os.path.isfile(filepath):
            grid = gridcls(filepath, baseuri=baseuri)
            log.info("returning %s, %s"%(filepath, ft))
            return (filepath, ft, grid)
    raise ValueError("No spreadsheet file found at %s/%s"%(basedir, resource_id))

