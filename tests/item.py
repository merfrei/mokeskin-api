import unittest
import requests
from tests import API_HOST
from urllib.parse import urljoin


def get_api_url(url, qry):
    return (url + '?{}'.format(qry))


class TestItemAPI(unittest.TestCase):

    ITEM_URL = '/items'
    TTL_URL = '/ttl'

    ITEM_KEY = 'item-example-key'
    ITEM_DATA = {
        'item_name': 'Item',
        'item_data': {
            'data1': 'value1',
            'data2': 'value2',
            'data_int': 4,
        },
        'item_number': 4.18,
    }
    ITEM_TTL = 3600
    ITEM_TAG = 'test-items'


    def test_item_api(self):
        item_qry = 'tag={}'.format(self.ITEM_TAG)
        item_url = urljoin(API_HOST, self.ITEM_URL)
        ttl_url = urljoin(API_HOST, self.TTL_URL)

        # Test POST
        post_data = {}
        post_data['key'] = self.ITEM_KEY
        post_data['data'] = self.ITEM_DATA.copy()
        post_data['exp'] = self.ITEM_TTL
        resp = requests.post(get_api_url(item_url, item_qry), json=post_data)
        self.assertEqual(resp.status_code, 201)

        # Test GET
        url = urljoin(item_url + '/', self.ITEM_KEY)
        resp = requests.get(get_api_url(url, item_qry))
        self.assertEqual(resp.status_code, 200)
        item_data = resp.json()['data']
        for k in self.ITEM_DATA.keys():
            self.assertEqual(item_data[k], self.ITEM_DATA[k])

        # Test UPDATE
        put_data = {}
        put_data['key'] = self.ITEM_KEY
        new_name = 'Item Name Updated'
        put_data['data'] = {'item_name': new_name}
        resp = requests.put(get_api_url(item_url, item_qry), json=put_data)
        self.assertEqual(resp.status_code, 200)
        item_data = resp.json()['data']
        self.assertEqual(item_data['item_name'], new_name)

        # Test TTL
        url = urljoin(ttl_url + '/', self.ITEM_KEY)
        resp = requests.get(get_api_url(url, item_qry))
        self.assertEqual(resp.status_code, 200)
        ttl = resp.json()['data']['ttl']
        self.assertTrue(int(ttl) <= int(self.ITEM_TTL))


if __name__ == '__main__':
    unittest.main()
