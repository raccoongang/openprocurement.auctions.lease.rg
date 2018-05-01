# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.lease.views.other.cancellation import (
    AuctionCancellationResource,
)


@opresource(name='leaseFinancial:Auction Cancellations',
            collection_path='/auctions/{auction_id}/cancellations',
            path='/auctions/{auction_id}/cancellations/{cancellation_id}',
            auctionsprocurementMethodType="leaseFinancial",
            description="Financial auction cancellations")
class FinancialAuctionCancellationResource(AuctionCancellationResource):
    pass
