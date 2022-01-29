import responses
from fetchmseval import fetchmseval
from unittest import TestCase


class FetchmsevalTests(TestCase):
    @responses.activate
    def test_fetch_products(self):
        success_body = """
        <div id="evaluateTopNav">
            <div class="menuContainer">
                <ul>
                    <li>
                        <a data-bind="evaluateSubNavClick.bind($data,1234," aria-label="Fetch Server 2022"></a>
                    </li>
                </ul>
            </div>
        </div>
        """

        responses.add(
            method=responses.GET, url=fetchmseval.ROOT_URL, status=200, body=success_body)

        products = fetchmseval.fetch_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].id, 1234)
        self.assertEqual(products[0].name, 'Fetch Server 2022')

    def test_fetch_product_downloads(self):
        self.skipTest("not implemented yet")
