# coding: utf-8

"""
    Traction Guest API

    The Traction Guest API is currently under limited release to select customers as we gather and iterate on feedback.  # Getting Started If you are interested in getting early access to the API, please send us an email to [support@tractionguest.com](mailto:support@tractionguest.com).  We will also add you to our Slack channel where you can ask questions and get further help.  # Terms and Conditions Please visit: [https://tractionguest.com/tos/api/](https://tractionguest.com/tos/api/)  # Versioning This API follows [semantic versioning](https://semver.org/), which follows the `Major`.`Minor`.`Patch` format.  * The `Major` number increments when potentially incompatible changes are made. * The `Minor` number increments when backwards-compatible additions are made. * The `Patch` number increments when backwards-compatible bug-fixes are made.   # noqa: E501

    The version of the OpenAPI document: 0.14.1
    Contact: support@tractionguest.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import TractionGuest
from TractionGuest.models.invite_watchlist import InviteWatchlist  # noqa: E501
from TractionGuest.rest import ApiException

class TestInviteWatchlist(unittest.TestCase):
    """InviteWatchlist unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InviteWatchlist
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = TractionGuest.models.invite_watchlist.InviteWatchlist()  # noqa: E501
        if include_optional :
            return InviteWatchlist(
                id = 56, 
                internal = [
                    TractionGuest.models.internal_watchlist_result.InternalWatchlistResult(
                        id = 56, 
                        email = '0', 
                        colour = '0', 
                        last_name = '0', 
                        first_name = '0', )
                    ], 
                external = [
                    TractionGuest.models.external_watchlist_result.ExternalWatchlistResult(
                        matches = [
                            TractionGuest.models.watchlist_match.WatchlistMatch(
                                id = '0', 
                                alt_names = [
                                    '0'
                                    ], 
                                federal_register_notice = '0', 
                                name = '0', 
                                source_information_url = '0', 
                                source_list_url = '0', 
                                list = '0', 
                                type = '0', 
                                category = '0', 
                                street1 = '0', 
                                street2 = '0', 
                                city = '0', 
                                state = '0', 
                                country = '0', 
                                notes = '0', 
                                frc = '0', 
                                start = '0', 
                                end = '0', 
                                frserve = '0', 
                                optional_id = '0', 
                                alert_type = '0', 
                                pair_status = '0', 
                                pair_reason = '0', 
                                pair_comments = '0', 
                                application_display_name = '0', 
                                application_id = '0', 
                                client_id = '0', 
                                client_key = '0', 
                                client_full_name = '0', 
                                list_key = '0', 
                                list_name = '0', 
                                list_id = '0', 
                                list_version = '0', 
                                list_modify_date = '0', 
                                list_profile_id = '0', 
                                list_profile_key = '0', 
                                link_single_string_name = '0', 
                                list_parent_single_string_name = '0', 
                                list_category = '0', 
                                list_pep_category = '0', 
                                list_do_bs = '0', 
                                list_countries = '0', 
                                rank_string = '0', 
                                ranktype = '0', 
                                rankweight = '0', 
                                pair_load_date = '0', 
                                e_address_to = '0', 
                                e_address_cc = '0', 
                                origin = '0', 
                                secondsviewed = '0', 
                                initial_user = '0', 
                                is_pair_parent_flag = '0', 
                                pair_met_search_criteria_flag = '0', 
                                editable_due_to_assignment_flag = '0', 
                                modify_date = '0', 
                                modified_by_user = '0', 
                                pair_report_type = '0', 
                                finscan_category = '0', 
                                wrapper_status = '0', 
                                source_lists = '0', )
                            ], 
                        colour = 'RED', 
                        integration = '0', 
                        search_terms = TractionGuest.models.watchlist_search.WatchlistSearch(
                            name = '0', 
                            company = '0', 
                            city = '0', 
                            country = '0', 
                            state = '0', ), )
                    ], 
                internal_colours = [
                    '0'
                    ], 
                external_colours = [
                    '0'
                    ]
            )
        else :
            return InviteWatchlist(
                id = 56,
        )

    def testInviteWatchlist(self):
        """Test InviteWatchlist"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
