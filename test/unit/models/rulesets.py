# Copyright (c) PagerDuty.
# See LICENSE for details.

import json
import unittest
import os.path

import requests_mock

from pypd import Rulesets


class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://api.pagerduty.com'
        self.api_key = 'FAUX_API_KEY'
        self.limit = 25
        base_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'data')
        path = os.path.join(base_path, 'sample_rulesets.json')

        with open(path) as f:
            self.rulesets_data = json.load(f)

        self.rulesetid = "0e84de00-9511-4380-9f4f-a7b568bb49a0"

        self.rulesets = list(filter(
            lambda s: s['id'] == self.rulesetid,
            self.rulesets_data["rulesets"],
        ))[0]

        self.ruleset_data = {
            'ruleset': self.rulesets,
        }
        path = os.path.join(base_path, 'sample_rules.json')
        with open(path) as f:
            self.rules_data = json.load(f)

    @requests_mock.Mocker()
    def test_fetch_a_ruleset(self, m):
        # setup mocked request uris
        service_url = '{0}/rulesets/{1}'.format(
            self.base_url,
            self.rulesetid,
        )

        m.register_uri(
            'GET',
            service_url,
            json=self.ruleset_data,
            complete_qs=False
        )

        rulesets = Rulesets.fetch(self.rulesetid, api_key=self.api_key)
        data = rulesets.get_ruleset(self.rulesetid)
        self.assertEqual(len(data["routing_keys"]), 1)
        self.assertEqual(data["routing_keys"][0], "R0212P1QXGEIQE2NMTQ7L7WXD00DWHIN")

    @requests_mock.Mocker()
    def test_fetch_all_rulesets(self, m):
        # setup mocked request uris
        service_url = '{0}/rulesets'.format(
            self.base_url
        )

        m.register_uri(
            'GET',
            service_url,
            json=self.rulesets_data,
            complete_qs=False
        )

        rulesets = Rulesets._fetch_all(api_key=self.api_key)
        data = rulesets[0].get_rulesets()
        self.assertEqual(len(data[0]["routing_keys"]), 1)
        self.assertEqual(data[0]["routing_keys"][0], "R0212P1QXGEIQE2NMTQ7L7WXD00DWHIN")