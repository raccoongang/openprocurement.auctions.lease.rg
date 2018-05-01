# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.lease.views.other.bid import (
    AuctionBidResource,
)


@opresource(name='leaseFinancial:Auction Bids',
            collection_path='/auctions/{auction_id}/bids',
            path='/auctions/{auction_id}/bids/{bid_id}',
            auctionsprocurementMethodType="leaseFinancial",
            description="Financial auction bids")
class FinancialAuctionBidResource(AuctionBidResource):
    pass
