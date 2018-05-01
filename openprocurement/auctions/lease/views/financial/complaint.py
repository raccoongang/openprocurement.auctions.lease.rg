# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.lease.views.other.complaint import (
    AuctionComplaintResource,
)


@opresource(name='leaseFinancial:Auction Complaints',
            collection_path='/auctions/{auction_id}/complaints',
            path='/auctions/{auction_id}/complaints/{complaint_id}',
            auctionsprocurementMethodType="leaseFinancial",
            description="Financial auction complaints")
class FinancialAuctionComplaintResource(AuctionComplaintResource):
    pass
