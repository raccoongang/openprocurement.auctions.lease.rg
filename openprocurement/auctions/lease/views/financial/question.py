# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.lease.views.other.question import (
    AuctionQuestionResource,
)


@opresource(name='leaseFinancial:Auction Questions',
            collection_path='/auctions/{auction_id}/questions',
            path='/auctions/{auction_id}/questions/{question_id}',
            auctionsprocurementMethodType="leaseFinancial",
            description="leaseFinancial:Auction questions")
class FinancialAuctionQuestionResource(AuctionQuestionResource):
    pass
