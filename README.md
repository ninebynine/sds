# Spreadsheet data service - SDS

Spreadsheets as a data service

## Collaborative Idea team members

Nicolas Gruel

Michael Fischer

Graham Klyne

Kewei Duan

Dominic Orchard

## Hackday pitch leader

Graham Klyne

## Context and problem

Lots of researchers use spreadsheets to store and share data, and explore data relationships.

But spreadsheets are poor for sharing data and mixing with other data sources, and generally are not sustainable. They are also difficult for writing programs against. Yet, we do not see them going away anytime soon.

## Solution

SDS will be a system for p;resentinh spreadsheets as flexible data sources on the web, for sharing, mixing with other sources, and programming against.  This system has two phases:

1. create a web service that will provide a simple web API to access data in the spreadsheet. There is a Google-defined API for accessing spreadsheets [1]: one might try to replicate a subset of this interface. This would allow programmers in a range of languages to create tools to access and present the spreadsheet content in more accessible/sustainable formats, as well as use spreadsheets as data sources for models. Python already has some Excel support which is related to this goal [2].

2. create a tool using the API to re-present the data in some more sustainable self-describing format (e.g. XML, RDF, etc.).

Note: to keep things simple, the project will concentrate initially on the data and not the formulae or graphics. Also, initial implementation might concentrate on single-worksheet workbooks.

The service may be run on a localhost or remotely, providing URIs to the data, for example:

    http://localhost:8000/spreadsheetname?gid=n (nth worksheet, per Google API)
    http://spreadsheet.example.org/spreadsheetname/3/2 (e.g. 2nd row of third worksheet)

etc.

For phase 2, we might invoke content negotiation to access a different format, e.g.

    GET/spreadsheetname/3/2 HTTP/1.1
    host: spreadsheet.example.org
    accept: application/json

might return

    { “col1”: val1, “col2”: val2 }

Details to be finalized.

## Specific ideas/challenges:

* May create a configuration language to describe properties of the spreadsheet.
* Equations are commonin spreadsheets, these may be set as ‘read-only’ fields in the data source
sustainable format? Versioning should be include so new version of the format will not break the system or transform the data in an agnostic format (text)?
* Available libraries may be read-only access, not allowing updates to the spreadsheet.

## References

[1] https://developers.google.com/google-apps/spreadsheets/
[2] https://pypi.python.org/pypi/xlrd

Kenji provides pointers:

[3] http://escience.washington.edu/sqlshare
[4] http://fsharp.github.io/FSharp.Data/library/CsvProvider.html
[5] http://fsharp.org/webstacks/
[6] http://fsprojects.github.io/FSharp.Interop.PythonProvider/
[7] http://research.microsoft.com/apps/pubs/default.aspx?id=173076

