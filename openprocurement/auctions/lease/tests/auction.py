# -*- coding: utf-8 -*-
import unittest

from openprocurement.auctions.core.tests.auctions import (
    AuctionAuctionResourceTestMixin,
    AuctionLotAuctionResourceTestMixin,
    AuctionMultipleLotAuctionResourceTestMixin
)
from openprocurement.auctions.core.tests.base import snitch
from openprocurement.auctions.core.tests.blanks.auction_blanks import (
    # AuctionSameValueAuctionResourceTest
    post_auction_auction_not_changed,
    post_auction_auction_reversed,
    # AuctionFeaturesAuctionResourceTest
    get_auction_features_auction
)

from openprocurement.auctions.lease.tests.base import (
    BaseAuctionWebTest, test_bids, test_lots, test_organization, test_features_auction_data,
)
from openprocurement.auctions.lease.tests.blanks.auction_blanks import (
    # AuctionAuctionResourceTest
    post_auction_auction,
    # AuctionLotAuctionResourceTest
    post_auction_auction_lot,
    # AuctionMultipleLotAuctionResourceTest
    post_auction_auction_2_lots,
)


class AuctionAuctionResourceTest(BaseAuctionWebTest, AuctionAuctionResourceTestMixin):
    #initial_data = auction_data
    initial_status = 'active.tendering'
    initial_bids = test_bids

    test_post_auction_auction = snitch(post_auction_auction)


class AuctionSameValueAuctionResourceTest(BaseAuctionWebTest):
    initial_status = 'active.auction'
    initial_bids = [
        {
            "tenderers": [
                test_organization
            ],
            "value": {
                "amount": 469,
                "currency": "UAH",
                "valueAddedTaxIncluded": True
            },
            'qualified': True
        }
        for i in range(3)
    ]
    test_post_auction_auction_not_changed = snitch(post_auction_auction_not_changed)
    test_post_auction_auction_reversed = snitch(post_auction_auction_reversed)


@unittest.skip("option not available")
class AuctionLotAuctionResourceTest(BaseAuctionWebTest, AuctionLotAuctionResourceTestMixin):
    initial_lots = test_lots

    test_post_auction_auction_lots = snitch(post_auction_auction_lot)



@unittest.skip("option not available")
class AuctionMultipleLotAuctionResourceTest(BaseAuctionWebTest, AuctionMultipleLotAuctionResourceTestMixin):
    initial_lots = 2 * test_lots
    test_post_auction_auction_2_lots = snitch(post_auction_auction_2_lots)


@unittest.skip("option not available")
class AuctionFeaturesAuctionResourceTest(BaseAuctionWebTest):
    initial_data = test_features_auction_data
    initial_status = 'active.auction'
    initial_bids = [
        {
            "parameters": [
                {
                    "code": i["code"],
                    "value": 0.1,
                }
                for i in test_features_auction_data['features']
            ],
            "tenderers": [
                test_organization
            ],
            "value": {
                "amount": 469,
                "currency": "UAH",
                "valueAddedTaxIncluded": True
            },
            'qualified': True
        },
        {
            "parameters": [
                {
                    "code": i["code"],
                    "value": 0.15,
                }
                for i in test_features_auction_data['features']
            ],
            "tenderers": [
                test_organization
            ],
            "value": {
                "amount": 479,
                "currency": "UAH",
                "valueAddedTaxIncluded": True
            }
        }
    ]

    test_get_auction_features_auction = snitch(get_auction_features_auction)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AuctionAuctionResourceTest))
    suite.addTest(unittest.makeSuite(AuctionSameValueAuctionResourceTest))
    suite.addTest(unittest.makeSuite(AuctionFeaturesAuctionResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
