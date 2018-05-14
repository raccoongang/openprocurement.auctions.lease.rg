.. include:: defs.hrst

.. index:: Auction, Auction
.. _auction:

Auction
=======

Schema
------

:title:
   string, multilingual, read-only, editable during enquiryPeriod

   Auction number in the Deposit Guarantee Fund.

:description:
   string, multilingual, editable during enquiryPeriod

   Detailed auction description.

:auctionID:
   string, auto-generated, read-only

   The auction identifier to refer auction to in "paper" documentation. 

   |ocdsDescription|
   AuctionID should always be the same as the OCID. It is included to make the flattened data structure more convenient.
   
:dgfID:
    string, editable during enquiryPeriod
    
    Identification number of the auction (also referred to as `lot`) in the XLS of Deposit Guarantee Fund.

   
:procuringEntity:
   :ref:`ProcuringEntity`, required

   Organization conducting the auction.
   

   |ocdsDescription|
   The entity managing the procurement, which may be different from the buyer who is paying / using the items being procured.

   
:value:
   :ref:`value`, required, editable during enquiryPeriod

   Total available auction budget. Bids lower than ``value`` will be rejected.

   |ocdsDescription|
   The total estimated value of the procurement.

:guarantee:
    :ref:`Guarantee`, editable during enquiryPeriod

    Bid guarantee

:items:
   list of :ref:`item` objects, required, editable during enquiryPeriod

   List that contains single item being sold. 

   |ocdsDescription|
   The goods and services to be purchased, broken into line items wherever possible. Items should not be duplicated, but a quantity of 2 specified instead.

:features:
   list of :ref:`Feature` objects

   Features of auction.

:documents:
   List of :ref:`document` objects
 
   |ocdsDescription|
   All documents and attachments related to the auction.

:questions:
   List of :ref:`question` objects

   Questions to ``procuringEntity`` and answers to them.

:complaints:
   List of :ref:`complaint` objects

   Complaints to auction conditions and their resolutions.

:bids:
   List of :ref:`bid` objects

   A list of all bids placed in the auction with information about participants, their proposals and other qualification documentation.

   |ocdsDescription|
   A list of all the companies who entered submissions for the auction.

:minNumberOfQualifiedBids:
   integer, optional
   
   The field that indicates the minimal number of qualified bids. The possible values for the field are 1 or 2.
   
   In case of the field has been remained blank, the workflow will be similar to the auction with 2 bids.
   
   You can also fill in the field, assigning the value "1". This will show that the only one bidder is needed 
   for the procedure to be successful. Therewith the auction is omitted and that bid turns to a qualified award.
   
:minimalStep:
   :ref:`value`, required, editable during enquiryPeriod

   The minimal step of auction. Validation rules:

   * `amount` should be greater than `Auction.value.amount`
   * `currency` should either be absent or match `Auction.value.currency`
   * `valueAddedTaxIncluded` should either be absent or match `Auction.value.valueAddedTaxIncluded`

:awards:
    List of :ref:`award` objects

    All qualifications (disqualifications and awards).

:contracts:
    List of :ref:`Contract` objects

:enquiryPeriod:
   :ref:`period`

   Period when questions are allowed.

   |ocdsDescription|
   The period during which enquiries may be made and will be answered.

:tenderPeriod:
   :ref:`period`

   Period when bids can be submitted.

   |ocdsDescription|
   The period when the auction is open for submissions. The end date is the closing date for auction submissions.

:auctionPeriod:
   :ref:`period`, required

   Period when Auction is conducted. `startDate` should be provided.

:auctionUrl:
    url

    A web address where auction is accessible for view.

:awardPeriod:
   :ref:`period`, read-only

   Awarding process period.

   |ocdsDescription|
   The date or period on which an award is anticipated to be made.

:status:
   string

   :`active.tendering`:
       Tendering period (tendering)
   :`active.auction`:
       Auction period (auction)
   :`active.qualification`:
       Winner qualification (qualification)
   :`active.awarded`:
       Standstill period (standstill)
   :`unsuccessful`:
       Unsuccessful auction (unsuccessful)
   :`complete`:
       Complete auction (complete)
   :`cancelled`:
       Cancelled auction (cancelled)

   Auction status.

:eligibilityCriteria:
    string, read-only
    
    Required for `dgfFinancialAssets` procedure.
    
    This field is multilingual: 
    
    * Ukrainian by default - До участі допускаються лише ліцензовані фінансові установи.
    
    * ``eligibilityCriteria_ru`` (Russian) - К участию допускаются только лицензированные финансовые учреждения.
    
    * ``eligibilityCriteria_en`` (English) - Only licensed financial institutions are eligible to participate.
    
.. :lots:
   List of :ref:`lot` objects.

   Contains all auction lots.

:cancellations:
   List of :ref:`cancellation` objects.

   Contains 1 object with `active` status in case of cancelled Auction.

   The :ref:`cancellation` object describes the reason of auction cancellation and contains accompanying
   documents  if there are any.

:revisions:
   List of :ref:`revision` objects, auto-generated

   Historical changes to `Auction` object properties.
