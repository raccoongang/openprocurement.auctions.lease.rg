# -*- coding: utf-8 -*-

from openprocurement.auctions.core.utils import (
    opresource,
)
from openprocurement.auctions.lease.views.other.complaint_document import (
    AuctionComplaintDocumentResource,
)


@opresource(name='leaseFinancial:Auction Complaint Documents',
            collection_path='/auctions/{auction_id}/complaints/{complaint_id}/documents',
            path='/auctions/{auction_id}/complaints/{complaint_id}/documents/{document_id}',
            auctionsprocurementMethodType="leaseFinancial",
            description="Financial auction complaint documents")
class FinancialComplaintDocumentResource(AuctionComplaintDocumentResource):
    pass
