# -*- coding: utf-8 -*-
from copy import deepcopy

from openprocurement.auctions.core.tests.base import JSON_RENDERER_ERROR

from openprocurement.auctions.lease.tests.base import test_financial_organization


# AuctionBidderResourceTest

def create_auction_bidder_invalid(self):
    response = self.app.post_json('/auctions/some_id/bids', {
        'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True}}, status=404)
    self.assertEqual(response.status, '404 Not Found')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Not Found', u'location':
            u'url', u'name': u'auction_id'}
    ])

    request_path = '/auctions/{}/bids'.format(self.auction_id)
    response = self.app.post(request_path, 'data', status=415)
    self.assertEqual(response.status, '415 Unsupported Media Type')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description':
             u"Content-Type header should be one of ['application/json']", u'location': u'header',
         u'name': u'Content-Type'}
    ])

    response = self.app.post(
        request_path, 'data', content_type='application/json', status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        JSON_RENDERER_ERROR
    ])

    response = self.app.post_json(request_path, 'data', status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Data not available',
         u'location': u'body', u'name': u'data'}
    ])

    response = self.app.post_json(
        request_path, {'not_data': {}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Data not available',
         u'location': u'body', u'name': u'data'}
    ])

    response = self.app.post_json(request_path, {'data': {
        'invalid_field': 'invalid_value'}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Rogue field', u'location':
            u'body', u'name': u'invalid_field'}
    ])

    response = self.app.post_json(request_path, {
        'data': {'tenderers': [{'identifier': 'invalid_value'}]}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': {u'identifier': [
            u'Please use a mapping for this field or Identifier instance instead of unicode.']}, u'location': u'body',
            u'name': u'tenderers'}
    ])

    response = self.app.post_json(request_path, {
        'data': {'tenderers': [{'identifier': {}}]}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertIn({u"location": u"body", u"name": u"qualified", u"description": [u"This field is required."]},
                  response.json['errors'])
    if self.initial_organization == test_financial_organization:
        self.assertIn({u'description': [u'This field is required.'], u'location': u'body', u'name': u'eligible'},
                      response.json['errors'])
        self.assertIn({u'description': [
            {u'additionalIdentifiers': [u'This field is required.'], u'contactPoint': [u'This field is required.'],
             u'identifier': {u'scheme': [u'This field is required.'], u'id': [u'This field is required.']},
             u'name': [u'This field is required.'], u'address': [u'This field is required.']}], u'location': u'body',
                       u'name': u'tenderers'}, response.json['errors'])
    else:
        self.assertIn({u'description': [{u'contactPoint': [u'This field is required.'],
                                         u'identifier': {u'scheme': [u'This field is required.'],
                                                         u'id': [u'This field is required.']},
                                         u'name': [u'This field is required.'],
                                         u'address': [u'This field is required.']}], u'location': u'body',
                       u'name': u'tenderers'}, response.json['errors'])

    response = self.app.post_json(request_path, {'data': {'tenderers': [{
        'name': 'name', 'identifier': {'uri': 'invalid_value'}}]}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertIn({u"location": u"body", u"name": u"qualified", u"description": [u"This field is required."]},
                  response.json['errors'])
    if self.initial_organization == test_financial_organization:
        self.assertIn({u'description': [u'This field is required.'], u'location': u'body', u'name': u'eligible'},
                      response.json['errors'])
        self.assertIn({u'description': [
            {u'additionalIdentifiers': [u'This field is required.'], u'contactPoint': [u'This field is required.'],
             u'identifier': {u'scheme': [u'This field is required.'], u'id': [u'This field is required.'],
                             u'uri': [u'Not a well formed URL.']}, u'address': [u'This field is required.']}],
                       u'location': u'body', u'name': u'tenderers'}, response.json['errors'])
    else:
        self.assertIn({u'description': [{u'contactPoint': [u'This field is required.'],
                                         u'identifier': {u'scheme': [u'This field is required.'],
                                                         u'id': [u'This field is required.'],
                                                         u'uri': [u'Not a well formed URL.']},
                                         u'address': [u'This field is required.']}], u'location': u'body',
                       u'name': u'tenderers'}, response.json['errors'])

    if self.initial_organization == test_financial_organization:
        response = self.app.post_json(request_path, {
            'data': {'tenderers': [self.initial_organization], 'qualified': True, 'eligible': True}}, status=422)
    else:
        response = self.app.post_json(request_path,
                                      {'data': {'tenderers': [self.initial_organization], 'qualified': True}},
                                      status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertIn({u'description': [u'This field is required.'], u'location': u'body', u'name': u'value'},
                  response.json['errors'])

    if self.initial_organization == test_financial_organization:
        response = self.app.post_json(request_path, {
            'data': {'tenderers': [self.initial_organization], "value": {"amount": 500, 'valueAddedTaxIncluded': False},
                     'qualified': True, 'eligible': True}}, status=422)
    else:
        response = self.app.post_json(request_path, {
            'data': {'tenderers': [self.initial_organization], "value": {"amount": 500, 'valueAddedTaxIncluded': False},
                     'qualified': True}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertIn({u'description': [
        u'valueAddedTaxIncluded of bid should be identical to valueAddedTaxIncluded of value of auction'],
                   u'location': u'body', u'name': u'value'}, response.json['errors'])

    if self.initial_organization == test_financial_organization:
        response = self.app.post_json(request_path, {
            'data': {'tenderers': [self.initial_organization], "value": {"amount": 500, 'currency': "USD"},
                     'qualified': True, 'eligible': True}}, status=422)
    else:
        response = self.app.post_json(request_path, {
            'data': {'tenderers': [self.initial_organization], "value": {"amount": 500, 'currency': "USD"},
                     'qualified': True}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertIn(
        {u'description': [u'currency of bid should be identical to currency of value of auction'], u'location': u'body',
         u'name': u'value'}, response.json['errors'])

    if self.initial_organization == test_financial_organization:
        response = self.app.post_json(request_path, {
            'data': {'tenderers': self.initial_organization, "value": {"amount": 500}, 'qualified': True,
                     'eligible': True}}, status=422)
    else:
        response = self.app.post_json(request_path, {
            'data': {'tenderers': self.initial_organization, "value": {"amount": 500}, 'qualified': True}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    if self.initial_organization == test_financial_organization:
        self.assertIn(
            {u'description': u"invalid literal for int() with base 10: 'additionalIdentifiers'", u'location': u'body',
             u'name': u'data'}, response.json['errors'])
    else:
        self.assertIn({u'description': u"invalid literal for int() with base 10: 'contactPoint'", u'location': u'body',
                       u'name': u'data'}, response.json['errors'])

    if self.initial_organization == test_financial_organization:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}}},
            status=422)
    else:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}}},
            status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertIn({u'description': [u'This field is required.'], u'location': u'body', u'name': u'qualified'},
                  response.json['errors'])


def patch_auction_bidder(self):
    if self.initial_organization == test_financial_organization:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "status": "draft", "value": {"amount": 500}, 'qualified': True, 'eligible': True}})
    else:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "status": "draft", "value": {"amount": 500}, 'qualified': True}})
    self.assertEqual(response.status, '201 Created')
    self.assertEqual(response.content_type, 'application/json')
    bidder = response.json['data']
    response = self.app.patch_json('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), {"data": {"status": "active", "value": {"amount": 60}}}, status=422)
    self.assertEqual(response.status, '422 Unprocessable Entity')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': [u'value of bid should be greater than value of auction'], u'location': u'body', u'name': u'value'}
    ])

    response = self.app.patch_json('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), {"data": {'tenderers': [{"name": u"Державне управління управлінням справами"}]}})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['data']['date'], bidder['date'])
    self.assertNotEqual(response.json['data']['tenderers'][0]['name'], bidder['tenderers'][0]['name'])

    response = self.app.patch_json('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), {"data": {"value": {"amount": 500}, 'tenderers': [self.initial_organization]}})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['data']['date'], bidder['date'])
    self.assertEqual(response.json['data']['tenderers'][0]['name'], bidder['tenderers'][0]['name'])

    response = self.app.patch_json('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), {"data": {"value": {"amount": 400}}})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['data']["value"]["amount"], 400)
    self.assertNotEqual(response.json['data']['date'], bidder['date'])

    response = self.app.patch_json('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), {"data": {"status": "active"}})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['data']["status"], "active")
    self.assertNotEqual(response.json['data']['date'], bidder['date'])

    response = self.app.patch_json('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), {"data": {"status": "draft"}}, status=403)
    self.assertEqual(response.status, '403 Forbidden')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['errors'][0]["description"], "Can\'t update bid to (draft) status")

    response = self.app.patch_json('/auctions/{}/bids/some_id'.format(self.auction_id), {"data": {"value": {"amount": 400}}}, status=404)
    self.assertEqual(response.status, '404 Not Found')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Not Found', u'location':
            u'url', u'name': u'bid_id'}
    ])

    response = self.app.patch_json('/auctions/some_id/bids/some_id', {"data": {"value": {"amount": 400}}}, status=404)
    self.assertEqual(response.status, '404 Not Found')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Not Found', u'location':
            u'url', u'name': u'auction_id'}
    ])

    self.set_status('complete')

    response = self.app.get('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']))
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['data']["value"]["amount"], 400)

    response = self.app.patch_json('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), {"data": {"value": {"amount": 400}}}, status=403)
    self.assertEqual(response.status, '403 Forbidden')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['errors'][0]["description"], "Can't update bid in current (complete) auction status")


def get_auction_bidder(self):
    if self.initial_organization == test_financial_organization:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True, 'eligible': True}})
    else:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True}})
    self.assertEqual(response.status, '201 Created')
    self.assertEqual(response.content_type, 'application/json')
    bidder = response.json['data']
    bid_token = response.json['access']['token']

    response = self.app.get('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), status=403)
    self.assertEqual(response.status, '403 Forbidden')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['errors'][0]["description"], "Can't view bid in current (active.tendering) auction status")

    response = self.app.get('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bidder['id'], bid_token))
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['data'], bidder)

    self.set_status('active.qualification')

    response = self.app.get('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']))
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    bidder_data = response.json['data']
    #self.assertIn(u'participationUrl', bidder_data)
    #bidder_data.pop(u'participationUrl')
    self.assertEqual(bidder_data, bidder)

    response = self.app.get('/auctions/{}/bids/some_id'.format(self.auction_id), status=404)
    self.assertEqual(response.status, '404 Not Found')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Not Found', u'location':
            u'url', u'name': u'bid_id'}
    ])

    response = self.app.get('/auctions/some_id/bids/some_id', status=404)
    self.assertEqual(response.status, '404 Not Found')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Not Found', u'location':
            u'url', u'name': u'auction_id'}
    ])

    response = self.app.delete('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), status=403)
    self.assertEqual(response.status, '403 Forbidden')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['errors'][0]["description"], "Can't delete bid in current (active.qualification) auction status")


def delete_auction_bidder(self):
    if self.initial_organization == test_financial_organization:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True, 'eligible': True}})
    else:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True}})
    self.assertEqual(response.status, '201 Created')
    self.assertEqual(response.content_type, 'application/json')
    bidder = response.json['data']

    response = self.app.delete('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']))
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['data'], bidder)

    revisions = self.db.get(self.auction_id).get('revisions')
    self.assertTrue(any([i for i in revisions[-2][u'changes'] if i['op'] == u'remove' and i['path'] == u'/bids']))
    self.assertTrue(any([i for i in revisions[-1][u'changes'] if i['op'] == u'add' and i['path'] == u'/bids']))

    response = self.app.delete('/auctions/{}/bids/some_id'.format(self.auction_id), status=404)
    self.assertEqual(response.status, '404 Not Found')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Not Found', u'location':
            u'url', u'name': u'bid_id'}
    ])

    response = self.app.delete('/auctions/some_id/bids/some_id', status=404)
    self.assertEqual(response.status, '404 Not Found')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Not Found', u'location':
            u'url', u'name': u'auction_id'}
    ])


def get_auction_auctioners(self):
    if self.initial_organization == test_financial_organization:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True, 'eligible': True}})
    else:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True}})
    self.assertEqual(response.status, '201 Created')
    self.assertEqual(response.content_type, 'application/json')
    bidder = response.json['data']

    response = self.app.get('/auctions/{}/bids'.format(self.auction_id), status=403)
    self.assertEqual(response.status, '403 Forbidden')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['errors'][0]["description"], "Can't view bids in current (active.tendering) auction status")

    self.set_status('active.qualification')

    response = self.app.get('/auctions/{}/bids'.format(self.auction_id))
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['data'][0], bidder)

    response = self.app.get('/auctions/some_id/bids', status=404)
    self.assertEqual(response.status, '404 Not Found')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['status'], 'error')
    self.assertEqual(response.json['errors'], [
        {u'description': u'Not Found', u'location':
            u'url', u'name': u'auction_id'}
    ])


def bid_Administrator_change(self):
    if self.initial_organization == test_financial_organization:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True, 'eligible': True}})
    else:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True}})
    self.assertEqual(response.status, '201 Created')
    self.assertEqual(response.content_type, 'application/json')
    bidder = response.json['data']

    self.app.authorization = ('Basic', ('administrator', ''))
    response = self.app.patch_json('/auctions/{}/bids/{}'.format(self.auction_id, bidder['id']), {"data": {
        'tenderers': [{"identifier": {"id": "00000000"}}],
        "value": {"amount": 400}
    }})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    self.assertNotEqual(response.json['data']["value"]["amount"], 400)
    self.assertEqual(response.json['data']["tenderers"][0]["identifier"]["id"], "00000000")


# AuctionBidInvalidationAuctionResourceTest


def post_auction_all_invalid_bids(self):
    self.app.authorization = ('Basic', ('auction', ''))

    response = self.app.post_json('/auctions/{}/auction'.format(self.auction_id),
                                  {'data': {'bids': self.initial_bids}})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    auction = response.json['data']

    self.assertEqual(auction["bids"][0]['value']['amount'], self.initial_bids[0]['value']['amount'])
    self.assertEqual(auction["bids"][1]['value']['amount'], self.initial_bids[1]['value']['amount'])
    self.assertEqual(auction["bids"][2]['value']['amount'], self.initial_bids[2]['value']['amount'])

    value_threshold = auction['value']['amount'] + auction['minimalStep']['amount']
    self.assertLess(auction["bids"][0]['value']['amount'], value_threshold)
    self.assertLess(auction["bids"][1]['value']['amount'], value_threshold)
    self.assertLess(auction["bids"][2]['value']['amount'], value_threshold)
    self.assertEqual(auction["bids"][0]['status'], 'invalid')
    self.assertEqual(auction["bids"][1]['status'], 'invalid')
    self.assertEqual(auction["bids"][2]['status'], 'invalid')
    self.assertEqual('unsuccessful', auction["status"])


def post_auction_one_invalid_bid(self):
    self.app.authorization = ('Basic', ('auction', ''))

    bids = deepcopy(self.initial_bids)
    bids[0]['value']['amount'] = bids[0]['value']['amount'] * 3
    bids[1]['value']['amount'] = bids[1]['value']['amount'] * 2
    response = self.app.post_json('/auctions/{}/auction'.format(self.auction_id), {'data': {'bids': bids}})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    auction = response.json['data']

    self.assertEqual(auction["bids"][0]['value']['amount'], bids[0]['value']['amount'])
    self.assertEqual(auction["bids"][1]['value']['amount'], bids[1]['value']['amount'])
    self.assertEqual(auction["bids"][2]['value']['amount'], bids[2]['value']['amount'])

    value_threshold = auction['value']['amount'] + auction['minimalStep']['amount']

    self.assertGreater(auction["bids"][0]['value']['amount'], value_threshold)
    self.assertGreater(auction["bids"][1]['value']['amount'], value_threshold)
    self.assertLess(auction["bids"][2]['value']['amount'], value_threshold)

    self.assertEqual(auction["bids"][0]['status'], 'active')
    self.assertEqual(auction["bids"][1]['status'], 'active')
    self.assertEqual(auction["bids"][2]['status'], 'invalid')

    self.assertEqual('active.qualification', auction["status"])

    for i, status in enumerate(['pending.verification', 'pending.waiting']):
        self.assertIn("tenderers", auction["bids"][i])
        self.assertIn("name", auction["bids"][i]["tenderers"][0])
        # self.assertIn(auction["awards"][0]["id"], response.headers['Location'])
        self.assertEqual(auction["awards"][i]['bid_id'], bids[i]['id'])
        self.assertEqual(auction["awards"][i]['value']['amount'], bids[i]['value']['amount'])
        self.assertEqual(auction["awards"][i]['suppliers'], bids[i]['tenderers'])
        self.assertEqual(auction["awards"][i]['status'], status)
        if status == 'pending.verification':
            self.assertIn("verificationPeriod", auction["awards"][i])


def post_auction_one_valid_bid(self):
    self.app.authorization = ('Basic', ('auction', ''))

    bids = deepcopy(self.initial_bids)
    bids[0]['value']['amount'] = bids[0]['value']['amount'] * 2
    response = self.app.post_json('/auctions/{}/auction'.format(self.auction_id), {'data': {'bids': bids}})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')
    auction = response.json['data']

    self.assertEqual(auction["bids"][0]['value']['amount'], bids[0]['value']['amount'])
    self.assertEqual(auction["bids"][1]['value']['amount'], bids[1]['value']['amount'])
    self.assertEqual(auction["bids"][2]['value']['amount'], bids[2]['value']['amount'])

    value_threshold = auction['value']['amount'] + auction['minimalStep']['amount']

    self.assertGreater(auction["bids"][0]['value']['amount'], value_threshold)
    self.assertLess(auction["bids"][1]['value']['amount'], value_threshold)
    self.assertLess(auction["bids"][2]['value']['amount'], value_threshold)

    self.assertEqual(auction["bids"][0]['status'], 'active')
    self.assertEqual(auction["bids"][1]['status'], 'invalid')
    self.assertEqual(auction["bids"][2]['status'], 'invalid')

    self.assertEqual('active.qualification', auction["status"])

    for i, status in enumerate(['pending.verification', 'unsuccessful']):
        self.assertIn("tenderers", auction["bids"][i])
        self.assertIn("name", auction["bids"][i]["tenderers"][0])
        # self.assertIn(auction["awards"][0]["id"], response.headers['Location'])
        self.assertEqual(auction["awards"][i]['bid_id'], bids[i]['id'])
        self.assertEqual(auction["awards"][i]['value']['amount'], bids[i]['value']['amount'])
        self.assertEqual(auction["awards"][i]['suppliers'], bids[i]['tenderers'])
        self.assertEqual(auction["awards"][i]['status'], status)
        if status == 'pending.verification':
            self.assertIn("verificationPeriod", auction["awards"][i])


# AuctionBidderProcessTest


def reactivate_invalidated_bids(self):

    bid1_id = self.initial_bids[0]['id']
    bid2_id = self.initial_bids[1]['id']
    bid1_token = self.initial_bids_tokens[self.initial_bids[0]['id']]
    bid2_token = self.initial_bids_tokens[self.initial_bids[1]['id']]

    # patch

    response = self.app.patch_json('/auctions/{}?acc_token={}'.format(self.auction_id, self.auction_token), {'data': {'value': {'amount': 540}}})
    self.assertEqual(response.status, '200 OK')
    self.assertEqual(response.content_type, 'application/json')

    response = self.app.get('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bid1_id, bid1_token))
    self.assertEqual(response.json['data']["status"], "invalid")
    response = self.app.get('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bid2_id, bid2_token))
    self.assertEqual(response.json['data']["status"], "invalid")

    # reactivate bids invalid bid value.amount

    response = self.app.patch_json('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bid1_id, bid1_token),
                                   {'data': {"status": "active"}}, status=422)
    self.assertEqual(response.json['errors'], [
        {u'description': [u'value of bid should be greater than value of auction'], u'location': u'body', u'name': u'value'}
    ])
    response = self.app.patch_json('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bid2_id, bid2_token),
                                   {'data': {"status": "active"}}, status=422)
    self.assertEqual(response.json['errors'], [
        {u'description': [u'value of bid should be greater than value of auction'], u'location': u'body', u'name': u'value'}
    ])

    # set bid value.amount above auction value.amount

    response = self.app.patch_json('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bid1_id, bid1_token),
                                   {"data": {"value": {"amount": 800}}})
    response = self.app.patch_json('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bid2_id, bid2_token),
                                   {"data": {"value": {"amount": 900}}})

    # reactivate bids

    response = self.app.patch_json('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bid1_id, bid1_token),
                                   {'data': {"status": "active"}})
    self.assertEqual(response.json['data']["status"], "active")

    response = self.app.patch_json('/auctions/{}/bids/{}?acc_token={}'.format(self.auction_id, bid2_id, bid2_token),
                                   {'data': {"status": "active"}})
    self.assertEqual(response.json['data']["status"], "active")

# AuctionBidderFeaturesResourceTest


def features_bidder(self):
    test_features_bids = [
        {
            "parameters": [
                {
                    "code": i["code"],
                    "value": 0.1,
                }
                for i in self.initial_data['features']
            ],
            "status": "active",
            "tenderers": [
                self.initial_organization
            ],
            "value": {
                "amount": 469,
                "currency": "UAH",
                "valueAddedTaxIncluded": True
            }
        },
        {
            "parameters": [
                {
                    "code": i["code"],
                    "value": 0.15,
                }
                for i in self.initial_data['features']
            ],
            "tenderers": [
                self.initial_organization
            ],
            "status": "draft",
            "value": {
                "amount": 479,
                "currency": "UAH",
                "valueAddedTaxIncluded": True
            }
        }
    ]
    for i in test_features_bids:
        response = self.app.post_json('/auctions/{}/bids'.format(self.auction_id), {'data': i})
        self.assertEqual(response.status, '201 Created')
        self.assertEqual(response.content_type, 'application/json')
        bid = response.json['data']
        bid.pop(u'date')
        bid.pop(u'id')
        self.assertEqual(bid, i)

# AuctionBidderDocumentResourceTest


def create_auction_bidder_document_nopending(self):
    if self.initial_organization == test_financial_organization:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True, 'eligible': True}})
    else:
        response = self.app.post_json('/auctions/{}/bids'.format(
            self.auction_id), {'data': {'tenderers': [self.initial_organization], "value": {"amount": 500}, 'qualified': True}})
    bid = response.json['data']
    bid_id = bid['id']

    response = self.app.post('/auctions/{}/bids/{}/documents'.format(
        self.auction_id, bid_id), upload_files=[('file', 'name.doc', 'content')])
    self.assertEqual(response.status, '201 Created')
    self.assertEqual(response.content_type, 'application/json')
    doc_id = response.json["data"]['id']
    self.assertIn(doc_id, response.headers['Location'])

    self.set_status('active.qualification')

    response = self.app.patch_json('/auctions/{}/bids/{}/documents/{}'.format(
        self.auction_id, bid_id, doc_id), {"data": {"description": "document description"}}, status=403)
    self.assertEqual(response.status, '403 Forbidden')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['errors'][0]["description"], "Can't update document because award of bid is not in pending state")

    response = self.app.put('/auctions/{}/bids/{}/documents/{}'.format(
        self.auction_id, bid_id, doc_id), 'content3', content_type='application/msword', status=403)
    self.assertEqual(response.status, '403 Forbidden')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['errors'][0]["description"], "Can't update document because award of bid is not in pending state")

    response = self.app.post('/auctions/{}/bids/{}/documents'.format(
        self.auction_id, bid_id), upload_files=[('file', 'name.doc', 'content')], status=403)
    self.assertEqual(response.status, '403 Forbidden')
    self.assertEqual(response.content_type, 'application/json')
    self.assertEqual(response.json['errors'][0]["description"], "Can't add document because award of bid is not in pending state")
