# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.lease.views.other.cancellation_document import (
    AuctionCancellationDocumentResource,
)


@opresource(name='leaseFinancial:Auction Cancellation Documents',
            collection_path='/auctions/{auction_id}/cancellations/{cancellation_id}/documents',
            path='/auctions/{auction_id}/cancellations/{cancellation_id}/documents/{document_id}',
            auctionsprocurementMethodType="leaseFinancial",
            description="Financial auction cancellation documents")
class FinancialAuctionCancellationDocumentResource(AuctionCancellationDocumentResource):
    pass
