# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from igvf_client.models.publication_results import PublicationResults

class TestPublicationResults(unittest.TestCase):
    """PublicationResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicationResults:
        """Test PublicationResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicationResults`
        """
        model = PublicationResults()
        if include_optional:
            return PublicationResults(
                graph = [
                    {
                        'key' : null
                        }
                    ],
                id = '',
                type = [
                    ''
                    ],
                total = 56,
                facets = [
                    igvf_client.models.search_facet.SearchFacet(
                        field = '', 
                        title = '', 
                        terms = [
                            igvf_client.models.search_facet_term_value.SearchFacetTermValue()
                            ], )
                    ]
            )
        else:
            return PublicationResults(
        )
        """

    def testPublicationResults(self):
        """Test PublicationResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
