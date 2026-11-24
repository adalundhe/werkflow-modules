from werkflow_aws.models.waf import (
    WAFv2AssociateWebACLRequest,
    WAFv2AssociateWebACLResponse,
    WAFv2CheckCapacityRequest,
    WAFv2CheckCapacityResponse,
    WAFv2CreateAPIKeyRequest,
    WAFv2CreateAPIKeyResponse,
    WAFv2CreateIPSetRequest,
    WAFv2CreateIPSetResponse,
    WAFv2CreateRegexPatternSetRequest,
    WAFv2CreateRegexPatternSetResponse,
    WAFv2CreateRuleGroupRequest,
    WAFv2CreateRuleGroupResponse,
    WAFv2CreateWebACLRequest,
    WAFv2CreateWebACLResponse,
    WAFv2DeleteAPIKeyRequest,
    WAFv2DeleteAPIKeyResponse,
    WAFv2DeleteFirewallManagerRuleGroupsRequest,
    WAFv2DeleteFirewallManagerRuleGroupsResponse,
    WAFv2DeleteIPSetRequest,
    WAFv2DeleteIPSetResponse,
    WAFv2DeleteLoggingConfigurationRequest,
    WAFv2DeleteLoggingConfigurationResponse,
    WAFv2DeletePermissionPolicyRequest,
    WAFv2DeletePermissionPolicyResponse,
    WAFv2DeleteRegexPatternSetRequest,
    WAFv2DeleteRegexPatternSetResponse,
    WAFv2DeleteRuleGroupRequest,
    WAFv2DeleteRuleGroupResponse,
    WAFv2DeleteWebACLRequest,
    WAFv2DeleteWebACLResponse,
    WAFv2DescribeAllManagedProductsRequest,
    WAFv2DescribeAllManagedProductsResponse,
    WAFv2DescribeManagedProductsByVendorRequest,
    WAFv2DescribeManagedProductsByVendorResponse,
    WAFv2DescribeManagedRuleGroupRequest,
    WAFv2DescribeManagedRuleGroupResponse,
    WAFv2DisassociateWebACLRequest,
    WAFv2DisassociateWebACLResponse,
    WAFv2GenerateMobileSdkReleaseUrlRequest,
    WAFv2GenerateMobileSdkReleaseUrlResponse,
    WAFv2GetDecryptedAPIKeyRequest,
    WAFv2GetDecryptedAPIKeyResponse,
    WAFv2GetEventActorRequest,
    WAFv2GetEventActorResponse,
    WAFv2GetEventRequest,
    WAFv2GetEventResponse,
    WAFv2GetIPSetRequest,
    WAFv2GetIPSetResponse,
    WAFv2GetLoggingConfigurationRequest,
    WAFv2GetLoggingConfigurationResponse,
    WAFv2GetManagedRuleSetRequest,
    WAFv2GetManagedRuleSetResponse,
    WAFv2GetMobileSdkReleaseRequest,
    WAFv2GetMobileSdkReleaseResponse,
    WAFv2GetPermissionPolicyRequest,
    WAFv2GetPermissionPolicyResponse,
    WAFv2GetRateBasedStatementManagedKeysRequest,
    WAFv2GetRateBasedStatementManagedKeysResponse,
    WAFv2GetRegexPatternSetRequest,
    WAFv2GetRegexPatternSetResponse,
    WAFv2GetRevenueStatisticsRequest,
    WAFv2GetRevenueStatisticsResponse,
    WAFv2GetRevenueStatisticsSummaryRequest,
    WAFv2GetRevenueStatisticsSummaryResponse,
    WAFv2GetRevenueStatisticsTimeSeriesRequest,
    WAFv2GetRevenueStatisticsTimeSeriesResponse,
    WAFv2GetRuleGroupRequest,
    WAFv2GetRuleGroupResponse,
    WAFv2GetSampledRequestsRequest,
    WAFv2GetSampledRequestsResponse,
    WAFv2GetTopPathStatisticsByTrafficRequest,
    WAFv2GetTopPathStatisticsByTrafficResponse,
    WAFv2GetWebACLForResourceRequest,
    WAFv2GetWebACLForResourceResponse,
    WAFv2GetWebACLRequest,
    WAFv2GetWebACLResponse,
    WAFv2ListAPIKeysRequest,
    WAFv2ListAPIKeysResponse,
    WAFv2ListAvailableManagedRuleGroupVersionsRequest,
    WAFv2ListAvailableManagedRuleGroupVersionsResponse,
    WAFv2ListAvailableManagedRuleGroupsRequest,
    WAFv2ListAvailableManagedRuleGroupsResponse,
    WAFv2ListEventActorsRequest,
    WAFv2ListEventActorsResponse,
    WAFv2ListEventsByWebACLRequest,
    WAFv2ListEventsByWebACLResponse,
    WAFv2ListEventsRequest,
    WAFv2ListEventsResponse,
    WAFv2ListIPSetsRequest,
    WAFv2ListIPSetsResponse,
    WAFv2ListLoggingConfigurationsRequest,
    WAFv2ListLoggingConfigurationsResponse,
    WAFv2ListManagedRuleSetsRequest,
    WAFv2ListManagedRuleSetsResponse,
    WAFv2ListMobileSdkReleasesRequest,
    WAFv2ListMobileSdkReleasesResponse,
    WAFv2ListRegexPatternSetsRequest,
    WAFv2ListRegexPatternSetsResponse,
    WAFv2ListResourcesForWebACLRequest,
    WAFv2ListResourcesForWebACLResponse,
    WAFv2ListRuleGroupsRequest,
    WAFv2ListRuleGroupsResponse,
    WAFv2ListSettlementRecordsRequest,
    WAFv2ListSettlementRecordsResponse,
    WAFv2ListTagsForResourceRequest,
    WAFv2ListTagsForResourceResponse,
    WAFv2ListWebACLsRequest,
    WAFv2ListWebACLsResponse,
    WAFv2PutLoggingConfigurationRequest,
    WAFv2PutLoggingConfigurationResponse,
    WAFv2PutManagedRuleSetVersionsRequest,
    WAFv2PutManagedRuleSetVersionsResponse,
    WAFv2PutPermissionPolicyRequest,
    WAFv2PutPermissionPolicyResponse,
    WAFv2TagResourceRequest,
    WAFv2TagResourceResponse,
    WAFv2UntagResourceRequest,
    WAFv2UntagResourceResponse,
    WAFv2UpdateIPSetRequest,
    WAFv2UpdateIPSetResponse,
    WAFv2UpdateManagedRuleSetVersionExpiryDateRequest,
    WAFv2UpdateManagedRuleSetVersionExpiryDateResponse,
    WAFv2UpdateRegexPatternSetRequest,
    WAFv2UpdateRegexPatternSetResponse,
    WAFv2UpdateRuleGroupRequest,
    WAFv2UpdateRuleGroupResponse,
    WAFv2UpdateWebACLRequest,
    WAFv2UpdateWebACLResponse,
)
from werkflow_aws.types.waf_client import WAFv2Client
from .base import AWSBaseService


class AWSWAFv2(AWSBaseService[WAFv2Client]):
    service_name = 'waf'
    boto3_service_name = 'wafv2'

    def __init__(self) -> None:
        super().__init__(service_name='waf', boto3_service_name='wafv2')

    async def associate_web_acl(
        self,
        request: WAFv2AssociateWebACLRequest,
    ) -> WAFv2AssociateWebACLResponse:
        client = self._require_client()
        return await self._execute(client.associate_web_acl, request, WAFv2AssociateWebACLResponse)

    async def check_capacity(
        self,
        request: WAFv2CheckCapacityRequest,
    ) -> WAFv2CheckCapacityResponse:
        client = self._require_client()
        return await self._execute(client.check_capacity, request, WAFv2CheckCapacityResponse)

    async def create_api_key(
        self,
        request: WAFv2CreateAPIKeyRequest,
    ) -> WAFv2CreateAPIKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_api_key, request, WAFv2CreateAPIKeyResponse)

    async def create_ip_set(
        self,
        request: WAFv2CreateIPSetRequest,
    ) -> WAFv2CreateIPSetResponse:
        client = self._require_client()
        return await self._execute(client.create_ip_set, request, WAFv2CreateIPSetResponse)

    async def create_regex_pattern_set(
        self,
        request: WAFv2CreateRegexPatternSetRequest,
    ) -> WAFv2CreateRegexPatternSetResponse:
        client = self._require_client()
        return await self._execute(client.create_regex_pattern_set, request, WAFv2CreateRegexPatternSetResponse)

    async def create_rule_group(
        self,
        request: WAFv2CreateRuleGroupRequest,
    ) -> WAFv2CreateRuleGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_rule_group, request, WAFv2CreateRuleGroupResponse)

    async def create_web_acl(
        self,
        request: WAFv2CreateWebACLRequest,
    ) -> WAFv2CreateWebACLResponse:
        client = self._require_client()
        return await self._execute(client.create_web_acl, request, WAFv2CreateWebACLResponse)

    async def delete_api_key(
        self,
        request: WAFv2DeleteAPIKeyRequest,
    ) -> WAFv2DeleteAPIKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_api_key, request, WAFv2DeleteAPIKeyResponse)

    async def delete_firewall_manager_rule_groups(
        self,
        request: WAFv2DeleteFirewallManagerRuleGroupsRequest,
    ) -> WAFv2DeleteFirewallManagerRuleGroupsResponse:
        client = self._require_client()
        return await self._execute(client.delete_firewall_manager_rule_groups, request, WAFv2DeleteFirewallManagerRuleGroupsResponse)

    async def delete_ip_set(
        self,
        request: WAFv2DeleteIPSetRequest,
    ) -> WAFv2DeleteIPSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_ip_set, request, WAFv2DeleteIPSetResponse)

    async def delete_logging_configuration(
        self,
        request: WAFv2DeleteLoggingConfigurationRequest,
    ) -> WAFv2DeleteLoggingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_logging_configuration, request, WAFv2DeleteLoggingConfigurationResponse)

    async def delete_permission_policy(
        self,
        request: WAFv2DeletePermissionPolicyRequest,
    ) -> WAFv2DeletePermissionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_permission_policy, request, WAFv2DeletePermissionPolicyResponse)

    async def delete_regex_pattern_set(
        self,
        request: WAFv2DeleteRegexPatternSetRequest,
    ) -> WAFv2DeleteRegexPatternSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_regex_pattern_set, request, WAFv2DeleteRegexPatternSetResponse)

    async def delete_rule_group(
        self,
        request: WAFv2DeleteRuleGroupRequest,
    ) -> WAFv2DeleteRuleGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_rule_group, request, WAFv2DeleteRuleGroupResponse)

    async def delete_web_acl(
        self,
        request: WAFv2DeleteWebACLRequest,
    ) -> WAFv2DeleteWebACLResponse:
        client = self._require_client()
        return await self._execute(client.delete_web_acl, request, WAFv2DeleteWebACLResponse)

    async def describe_all_managed_products(
        self,
        request: WAFv2DescribeAllManagedProductsRequest,
    ) -> WAFv2DescribeAllManagedProductsResponse:
        client = self._require_client()
        return await self._execute(client.describe_all_managed_products, request, WAFv2DescribeAllManagedProductsResponse)

    async def describe_managed_products_by_vendor(
        self,
        request: WAFv2DescribeManagedProductsByVendorRequest,
    ) -> WAFv2DescribeManagedProductsByVendorResponse:
        client = self._require_client()
        return await self._execute(client.describe_managed_products_by_vendor, request, WAFv2DescribeManagedProductsByVendorResponse)

    async def describe_managed_rule_group(
        self,
        request: WAFv2DescribeManagedRuleGroupRequest,
    ) -> WAFv2DescribeManagedRuleGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_managed_rule_group, request, WAFv2DescribeManagedRuleGroupResponse)

    async def disassociate_web_acl(
        self,
        request: WAFv2DisassociateWebACLRequest,
    ) -> WAFv2DisassociateWebACLResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_web_acl, request, WAFv2DisassociateWebACLResponse)

    async def generate_mobile_sdk_release_url(
        self,
        request: WAFv2GenerateMobileSdkReleaseUrlRequest,
    ) -> WAFv2GenerateMobileSdkReleaseUrlResponse:
        client = self._require_client()
        return await self._execute(client.generate_mobile_sdk_release_url, request, WAFv2GenerateMobileSdkReleaseUrlResponse)

    async def get_decrypted_api_key(
        self,
        request: WAFv2GetDecryptedAPIKeyRequest,
    ) -> WAFv2GetDecryptedAPIKeyResponse:
        client = self._require_client()
        return await self._execute(client.get_decrypted_api_key, request, WAFv2GetDecryptedAPIKeyResponse)

    async def get_event(
        self,
        request: WAFv2GetEventRequest,
    ) -> WAFv2GetEventResponse:
        client = self._require_client()
        return await self._execute(client.get_event, request, WAFv2GetEventResponse)

    async def get_event_actor(
        self,
        request: WAFv2GetEventActorRequest,
    ) -> WAFv2GetEventActorResponse:
        client = self._require_client()
        return await self._execute(client.get_event_actor, request, WAFv2GetEventActorResponse)

    async def get_ip_set(
        self,
        request: WAFv2GetIPSetRequest,
    ) -> WAFv2GetIPSetResponse:
        client = self._require_client()
        return await self._execute(client.get_ip_set, request, WAFv2GetIPSetResponse)

    async def get_logging_configuration(
        self,
        request: WAFv2GetLoggingConfigurationRequest,
    ) -> WAFv2GetLoggingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_logging_configuration, request, WAFv2GetLoggingConfigurationResponse)

    async def get_managed_rule_set(
        self,
        request: WAFv2GetManagedRuleSetRequest,
    ) -> WAFv2GetManagedRuleSetResponse:
        client = self._require_client()
        return await self._execute(client.get_managed_rule_set, request, WAFv2GetManagedRuleSetResponse)

    async def get_mobile_sdk_release(
        self,
        request: WAFv2GetMobileSdkReleaseRequest,
    ) -> WAFv2GetMobileSdkReleaseResponse:
        client = self._require_client()
        return await self._execute(client.get_mobile_sdk_release, request, WAFv2GetMobileSdkReleaseResponse)

    async def get_permission_policy(
        self,
        request: WAFv2GetPermissionPolicyRequest,
    ) -> WAFv2GetPermissionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_permission_policy, request, WAFv2GetPermissionPolicyResponse)

    async def get_rate_based_statement_managed_keys(
        self,
        request: WAFv2GetRateBasedStatementManagedKeysRequest,
    ) -> WAFv2GetRateBasedStatementManagedKeysResponse:
        client = self._require_client()
        return await self._execute(client.get_rate_based_statement_managed_keys, request, WAFv2GetRateBasedStatementManagedKeysResponse)

    async def get_regex_pattern_set(
        self,
        request: WAFv2GetRegexPatternSetRequest,
    ) -> WAFv2GetRegexPatternSetResponse:
        client = self._require_client()
        return await self._execute(client.get_regex_pattern_set, request, WAFv2GetRegexPatternSetResponse)

    async def get_revenue_statistics(
        self,
        request: WAFv2GetRevenueStatisticsRequest,
    ) -> WAFv2GetRevenueStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.get_revenue_statistics, request, WAFv2GetRevenueStatisticsResponse)

    async def get_revenue_statistics_summary(
        self,
        request: WAFv2GetRevenueStatisticsSummaryRequest,
    ) -> WAFv2GetRevenueStatisticsSummaryResponse:
        client = self._require_client()
        return await self._execute(client.get_revenue_statistics_summary, request, WAFv2GetRevenueStatisticsSummaryResponse)

    async def get_revenue_statistics_time_series(
        self,
        request: WAFv2GetRevenueStatisticsTimeSeriesRequest,
    ) -> WAFv2GetRevenueStatisticsTimeSeriesResponse:
        client = self._require_client()
        return await self._execute(client.get_revenue_statistics_time_series, request, WAFv2GetRevenueStatisticsTimeSeriesResponse)

    async def get_rule_group(
        self,
        request: WAFv2GetRuleGroupRequest | None = None,
    ) -> WAFv2GetRuleGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_rule_group, request, WAFv2GetRuleGroupResponse)

    async def get_sampled_requests(
        self,
        request: WAFv2GetSampledRequestsRequest,
    ) -> WAFv2GetSampledRequestsResponse:
        client = self._require_client()
        return await self._execute(client.get_sampled_requests, request, WAFv2GetSampledRequestsResponse)

    async def get_top_path_statistics_by_traffic(
        self,
        request: WAFv2GetTopPathStatisticsByTrafficRequest,
    ) -> WAFv2GetTopPathStatisticsByTrafficResponse:
        client = self._require_client()
        return await self._execute(client.get_top_path_statistics_by_traffic, request, WAFv2GetTopPathStatisticsByTrafficResponse)

    async def get_web_acl(
        self,
        request: WAFv2GetWebACLRequest | None = None,
    ) -> WAFv2GetWebACLResponse:
        client = self._require_client()
        return await self._execute(client.get_web_acl, request, WAFv2GetWebACLResponse)

    async def get_web_acl_for_resource(
        self,
        request: WAFv2GetWebACLForResourceRequest,
    ) -> WAFv2GetWebACLForResourceResponse:
        client = self._require_client()
        return await self._execute(client.get_web_acl_for_resource, request, WAFv2GetWebACLForResourceResponse)

    async def list_api_keys(
        self,
        request: WAFv2ListAPIKeysRequest,
    ) -> WAFv2ListAPIKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_api_keys, request, WAFv2ListAPIKeysResponse)

    async def list_available_managed_rule_group_versions(
        self,
        request: WAFv2ListAvailableManagedRuleGroupVersionsRequest,
    ) -> WAFv2ListAvailableManagedRuleGroupVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_available_managed_rule_group_versions, request, WAFv2ListAvailableManagedRuleGroupVersionsResponse)

    async def list_available_managed_rule_groups(
        self,
        request: WAFv2ListAvailableManagedRuleGroupsRequest,
    ) -> WAFv2ListAvailableManagedRuleGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_available_managed_rule_groups, request, WAFv2ListAvailableManagedRuleGroupsResponse)

    async def list_event_actors(
        self,
        request: WAFv2ListEventActorsRequest,
    ) -> WAFv2ListEventActorsResponse:
        client = self._require_client()
        return await self._execute(client.list_event_actors, request, WAFv2ListEventActorsResponse)

    async def list_events(
        self,
        request: WAFv2ListEventsRequest,
    ) -> WAFv2ListEventsResponse:
        client = self._require_client()
        return await self._execute(client.list_events, request, WAFv2ListEventsResponse)

    async def list_events_by_web_acl(
        self,
        request: WAFv2ListEventsByWebACLRequest,
    ) -> WAFv2ListEventsByWebACLResponse:
        client = self._require_client()
        return await self._execute(client.list_events_by_web_acl, request, WAFv2ListEventsByWebACLResponse)

    async def list_ip_sets(
        self,
        request: WAFv2ListIPSetsRequest,
    ) -> WAFv2ListIPSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_ip_sets, request, WAFv2ListIPSetsResponse)

    async def list_logging_configurations(
        self,
        request: WAFv2ListLoggingConfigurationsRequest,
    ) -> WAFv2ListLoggingConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_logging_configurations, request, WAFv2ListLoggingConfigurationsResponse)

    async def list_managed_rule_sets(
        self,
        request: WAFv2ListManagedRuleSetsRequest,
    ) -> WAFv2ListManagedRuleSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_managed_rule_sets, request, WAFv2ListManagedRuleSetsResponse)

    async def list_mobile_sdk_releases(
        self,
        request: WAFv2ListMobileSdkReleasesRequest,
    ) -> WAFv2ListMobileSdkReleasesResponse:
        client = self._require_client()
        return await self._execute(client.list_mobile_sdk_releases, request, WAFv2ListMobileSdkReleasesResponse)

    async def list_regex_pattern_sets(
        self,
        request: WAFv2ListRegexPatternSetsRequest,
    ) -> WAFv2ListRegexPatternSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_regex_pattern_sets, request, WAFv2ListRegexPatternSetsResponse)

    async def list_resources_for_web_acl(
        self,
        request: WAFv2ListResourcesForWebACLRequest,
    ) -> WAFv2ListResourcesForWebACLResponse:
        client = self._require_client()
        return await self._execute(client.list_resources_for_web_acl, request, WAFv2ListResourcesForWebACLResponse)

    async def list_rule_groups(
        self,
        request: WAFv2ListRuleGroupsRequest,
    ) -> WAFv2ListRuleGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_rule_groups, request, WAFv2ListRuleGroupsResponse)

    async def list_settlement_records(
        self,
        request: WAFv2ListSettlementRecordsRequest,
    ) -> WAFv2ListSettlementRecordsResponse:
        client = self._require_client()
        return await self._execute(client.list_settlement_records, request, WAFv2ListSettlementRecordsResponse)

    async def list_tags_for_resource(
        self,
        request: WAFv2ListTagsForResourceRequest,
    ) -> WAFv2ListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, WAFv2ListTagsForResourceResponse)

    async def list_web_acls(
        self,
        request: WAFv2ListWebACLsRequest,
    ) -> WAFv2ListWebACLsResponse:
        client = self._require_client()
        return await self._execute(client.list_web_acls, request, WAFv2ListWebACLsResponse)

    async def put_logging_configuration(
        self,
        request: WAFv2PutLoggingConfigurationRequest,
    ) -> WAFv2PutLoggingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_logging_configuration, request, WAFv2PutLoggingConfigurationResponse)

    async def put_managed_rule_set_versions(
        self,
        request: WAFv2PutManagedRuleSetVersionsRequest,
    ) -> WAFv2PutManagedRuleSetVersionsResponse:
        client = self._require_client()
        return await self._execute(client.put_managed_rule_set_versions, request, WAFv2PutManagedRuleSetVersionsResponse)

    async def put_permission_policy(
        self,
        request: WAFv2PutPermissionPolicyRequest,
    ) -> WAFv2PutPermissionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_permission_policy, request, WAFv2PutPermissionPolicyResponse)

    async def tag_resource(
        self,
        request: WAFv2TagResourceRequest,
    ) -> WAFv2TagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, WAFv2TagResourceResponse)

    async def untag_resource(
        self,
        request: WAFv2UntagResourceRequest,
    ) -> WAFv2UntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, WAFv2UntagResourceResponse)

    async def update_ip_set(
        self,
        request: WAFv2UpdateIPSetRequest,
    ) -> WAFv2UpdateIPSetResponse:
        client = self._require_client()
        return await self._execute(client.update_ip_set, request, WAFv2UpdateIPSetResponse)

    async def update_managed_rule_set_version_expiry_date(
        self,
        request: WAFv2UpdateManagedRuleSetVersionExpiryDateRequest,
    ) -> WAFv2UpdateManagedRuleSetVersionExpiryDateResponse:
        client = self._require_client()
        return await self._execute(client.update_managed_rule_set_version_expiry_date, request, WAFv2UpdateManagedRuleSetVersionExpiryDateResponse)

    async def update_regex_pattern_set(
        self,
        request: WAFv2UpdateRegexPatternSetRequest,
    ) -> WAFv2UpdateRegexPatternSetResponse:
        client = self._require_client()
        return await self._execute(client.update_regex_pattern_set, request, WAFv2UpdateRegexPatternSetResponse)

    async def update_rule_group(
        self,
        request: WAFv2UpdateRuleGroupRequest,
    ) -> WAFv2UpdateRuleGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_rule_group, request, WAFv2UpdateRuleGroupResponse)

    async def update_web_acl(
        self,
        request: WAFv2UpdateWebACLRequest,
    ) -> WAFv2UpdateWebACLResponse:
        client = self._require_client()
        return await self._execute(client.update_web_acl, request, WAFv2UpdateWebACLResponse)
