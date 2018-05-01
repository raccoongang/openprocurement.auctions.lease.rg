# -*- coding: utf-8 -*-
from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.lease.views.other.auction import (
    AuctionAuctionResource,
)


@opresource(name='leaseFinancial:Auction Auction',
            collection_path='/auctions/{auction_id}/auction',
            path='/auctions/{auction_id}/auction/{auction_lot_id}',
            auctionsprocurementMethodType="leaseFinancial",
            description="Financial auction auction data")
class FinancialAuctionAuctionResource(AuctionAuctionResource):
    pass
