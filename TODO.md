# TODO.md


##Goal

A web service to present data from local spreadsheet files.


## Implementation

Implemented in Python, using Django and other libraries.

https://github.com/ninebynine/sds


## Demo sequence

1. Show spreadsheet data in file system

2. Point browser at running web service

3. Show list of data shown in browser

4. Go to examples, show data  (avoid full affymetrix data)

5. Go to console window and use CURL to pull content negotiated data


## Steps to do

/ Create github repo
/ Create python environment
/ Install Django
/ Create Django project
/ Find example spreadsheet(s), copy into project
/ Locate existing software, copy into project
/ Create URI disptach file(s)
* Step goals:
  0. / "Hello world" server
  1. / Display list of available data files
  2. / Display data as HTML in browser
  4. / Content negotiate for CSV and JSON
  5. extract and return rows
* Initial row reader
  - URI design
* ...


## Problems encountered

1. Reproducing Django application environment from Annalist for new application tool longer than expected - took 1.5 hours to working "Hello World".  The directory structure should probably be reviewed and rationalized.

2. Ran into some problems with the Grid abstraction and iterating over data:  the end of data detection wasn't working properly which led to non-terminating loops.  I think this has now been fixed by creating explicit iterators over columns an d rows that catch exceptions to terminate the iteration.

3. Speed: large spreadsheets (e.g,. full 14-18K rows of Affymeytrix microarray data) can be very slow to process.  Probably need to create some kind of cacheing for web service use.


## Further work

* For Excel spreadsheet access, provide for proper selection of worksheet (currently hardwired to select main data from example file)
* Tests!
* Row ranges
* Selected columns
* Configuration file to tailor presented model/API
* Serve spreadsheet as RO
* Spreadsheet upload page
* Annalist integration
* Updates through web page? (not sure if easy or desirable)

