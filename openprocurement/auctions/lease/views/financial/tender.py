# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.lease.views.other.tender import (
    AuctionResource,
)


@opresource(name='leaseFinancial:Auction',
            path='/auctions/{auction_id}',
            auctionsprocurementMethodType="leaseFinancial",
            description="Open Contracting compatible data exchange format. See http://ocds.open-contracting.org/standard/r/master/#auction for more info")
class FinancialAuctionResource(AuctionResource):
    pass
