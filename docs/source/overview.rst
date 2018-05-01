Overview
========

openprocurement.auctions.dgf contains documentaion for Deposit Guarantee Fund auctions.

There are two procedures:
 
 * dgfOtherAssets - sale of the insolvent bank property.
 
 * dgfFinancialAssets - sale of the creditor claim right.


Features
--------

* The only date Organizer has to provide is *Tender.auctionPeriod.startDate*, the rest will be calculated automatically.
* Optionally Organizer can set *enquiryPeriod.endDate*.
* If *enquiryPeriod.endDate* is not provided it will be calculated automatically.
* Organizer can both increase and decrease `value.amount`, `guarantee.amount`, `minimalStep.amount`.
* `tenderPeriod` must be at least 7 calendar days.
* Organizer can edit procedure only during *rectificationPeriod*.
* Organizer can add and edit documents only during *rectificationPeriod*.
* As soon as the action is edited, the status of all of the submitted bids will be switched to `invalid`.
* Procedure can be switched from *draft* status to *active.tendering*.
* During *active.tendering* period participants can ask questions, submit proposals, and upload documents.
* There is obligatory participant qualification (*Bid.selfQualified*) via guarantee payment.
* The only currency (*Value.currency*) for this procedure is hryvnia (UAH).
* The items within an auction are allowed to be from different CAV groups.

Conventions
-----------

API accepts `JSON <http://json.org/>`_ or form-encoded content in
requests.  It returns JSON content in all of its responses, including
errors.  Only the UTF-8 character encoding is supported for both requests
and responses.

All API POST and PUT requests expect a top-level object with a single
element in it named `data`.  Successful responses will mirror this format. 
The data element should itself be an object, containing the parameters for
the request.  In the case of creating a new auction, these are the fields we
want to set on the auction itself.

If the request was successful, we will get a response code of `201`
indicating the object was created.  That response will have a data field at
its top level, which will contain complete information on the new auction,
including its ID.

If something went wrong during the request, we'll get a different status
code and the JSON returned will have an `errors` field at the top level
containing a list of problems.  We look at the first one and print out its
message.

Main responsibilities
---------------------

Business logic
--------------

Project status
--------------

The project has pre alpha status.

The source repository for this project is on GitHub: https://github.com/openprocurement/openprocurement.auctions.dgf

You can leave feedback by raising a new issue on the `issue tracker
<https://github.com/openprocurement/openprocurement.auctions.dgf/issues>`_ (GitHub
registration necessary).  

Documentation of related packages
---------------------------------

* `OpenProcurement API <http://api-docs.openprocurement.org/en/latest/>`_

API stability
-------------

API is highly unstable, and while API endpoints are expected to remain
relatively stable the data exchange formats are expected to be changed a
lot.  The changes in the API are communicated via `Open Procurement API
<https://groups.google.com/group/open-procurement-api>`_ maillist.

Change log
----------

0.1
~~~

Released: not released


Next steps
----------
You might find it helpful to look at the :ref:`tutorial`.
