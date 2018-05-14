# -*- coding: utf-8 -*-
from openprocurement.auctions.core.utils import error_handler, get_now, TZ

from openprocurement.auctions.lease.utils import generate_rectificationPeriod


def validate_rectification_period_editing(request, **kwargs):
    if request.context.status == 'active.tendering' and request.authenticated_role not in ['chronograph', 'Administrator']:
        auction = request.validated['auction']
        rectificationPeriod = auction.rectificationPeriod or generate_rectificationPeriod(auction)
        if rectificationPeriod.endDate.astimezone(TZ) < get_now():
            request.errors.add('body', 'data', 'Auction can be edited only during the rectification period: from ({}) to ({}).'.format(rectificationPeriod.startDate.isoformat(), rectificationPeriod.endDate.isoformat()))
            request.errors.status = 403
            raise error_handler(request)
