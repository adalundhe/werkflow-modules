from werkflow_aws.models.elb import (
    ELBv2AddListenerCertificatesRequest,
    ELBv2AddListenerCertificatesResponse,
    ELBv2AddTagsRequest,
    ELBv2AddTagsResponse,
    ELBv2AddTrustStoreRevocationsRequest,
    ELBv2AddTrustStoreRevocationsResponse,
    ELBv2CreateListenerRequest,
    ELBv2CreateListenerResponse,
    ELBv2CreateLoadBalancerRequest,
    ELBv2CreateLoadBalancerResponse,
    ELBv2CreateRuleRequest,
    ELBv2CreateRuleResponse,
    ELBv2CreateTargetGroupRequest,
    ELBv2CreateTargetGroupResponse,
    ELBv2CreateTrustStoreRequest,
    ELBv2CreateTrustStoreResponse,
    ELBv2DeleteListenerRequest,
    ELBv2DeleteListenerResponse,
    ELBv2DeleteLoadBalancerRequest,
    ELBv2DeleteLoadBalancerResponse,
    ELBv2DeleteRuleRequest,
    ELBv2DeleteRuleResponse,
    ELBv2DeleteSharedTrustStoreAssociationRequest,
    ELBv2DeleteSharedTrustStoreAssociationResponse,
    ELBv2DeleteTargetGroupRequest,
    ELBv2DeleteTargetGroupResponse,
    ELBv2DeleteTrustStoreRequest,
    ELBv2DeleteTrustStoreResponse,
    ELBv2DeregisterTargetsRequest,
    ELBv2DeregisterTargetsResponse,
    ELBv2DescribeAccountLimitsRequest,
    ELBv2DescribeAccountLimitsResponse,
    ELBv2DescribeCapacityReservationRequest,
    ELBv2DescribeCapacityReservationResponse,
    ELBv2DescribeListenerAttributesRequest,
    ELBv2DescribeListenerAttributesResponse,
    ELBv2DescribeListenerCertificatesRequest,
    ELBv2DescribeListenerCertificatesResponse,
    ELBv2DescribeListenersRequest,
    ELBv2DescribeListenersResponse,
    ELBv2DescribeLoadBalancerAttributesRequest,
    ELBv2DescribeLoadBalancerAttributesResponse,
    ELBv2DescribeLoadBalancersRequest,
    ELBv2DescribeLoadBalancersResponse,
    ELBv2DescribeRulesRequest,
    ELBv2DescribeRulesResponse,
    ELBv2DescribeSSLPoliciesRequest,
    ELBv2DescribeSSLPoliciesResponse,
    ELBv2DescribeTagsRequest,
    ELBv2DescribeTagsResponse,
    ELBv2DescribeTargetGroupAttributesRequest,
    ELBv2DescribeTargetGroupAttributesResponse,
    ELBv2DescribeTargetGroupsRequest,
    ELBv2DescribeTargetGroupsResponse,
    ELBv2DescribeTargetHealthRequest,
    ELBv2DescribeTargetHealthResponse,
    ELBv2DescribeTrustStoreAssociationsRequest,
    ELBv2DescribeTrustStoreAssociationsResponse,
    ELBv2DescribeTrustStoreRevocationsRequest,
    ELBv2DescribeTrustStoreRevocationsResponse,
    ELBv2DescribeTrustStoresRequest,
    ELBv2DescribeTrustStoresResponse,
    ELBv2GetResourcePolicyRequest,
    ELBv2GetResourcePolicyResponse,
    ELBv2GetTrustStoreCaCertificatesBundleRequest,
    ELBv2GetTrustStoreCaCertificatesBundleResponse,
    ELBv2GetTrustStoreRevocationContentRequest,
    ELBv2GetTrustStoreRevocationContentResponse,
    ELBv2ModifyCapacityReservationRequest,
    ELBv2ModifyCapacityReservationResponse,
    ELBv2ModifyIpPoolsRequest,
    ELBv2ModifyIpPoolsResponse,
    ELBv2ModifyListenerAttributesRequest,
    ELBv2ModifyListenerAttributesResponse,
    ELBv2ModifyListenerRequest,
    ELBv2ModifyListenerResponse,
    ELBv2ModifyLoadBalancerAttributesRequest,
    ELBv2ModifyLoadBalancerAttributesResponse,
    ELBv2ModifyRuleRequest,
    ELBv2ModifyRuleResponse,
    ELBv2ModifyTargetGroupAttributesRequest,
    ELBv2ModifyTargetGroupAttributesResponse,
    ELBv2ModifyTargetGroupRequest,
    ELBv2ModifyTargetGroupResponse,
    ELBv2ModifyTrustStoreRequest,
    ELBv2ModifyTrustStoreResponse,
    ELBv2RegisterTargetsRequest,
    ELBv2RegisterTargetsResponse,
    ELBv2RemoveListenerCertificatesRequest,
    ELBv2RemoveListenerCertificatesResponse,
    ELBv2RemoveTagsRequest,
    ELBv2RemoveTagsResponse,
    ELBv2RemoveTrustStoreRevocationsRequest,
    ELBv2RemoveTrustStoreRevocationsResponse,
    ELBv2SetIpAddressTypeRequest,
    ELBv2SetIpAddressTypeResponse,
    ELBv2SetRulePrioritiesRequest,
    ELBv2SetRulePrioritiesResponse,
    ELBv2SetSecurityGroupsRequest,
    ELBv2SetSecurityGroupsResponse,
    ELBv2SetSubnetsRequest,
    ELBv2SetSubnetsResponse,
)
from werkflow_aws.types.elb_client import ELBv2Client
from .base import AWSBaseService


class AWSELBv2(AWSBaseService[ELBv2Client]):
    service_name = 'elb'
    boto3_service_name = 'elbv2'

    def __init__(self) -> None:
        super().__init__(service_name='elb', boto3_service_name='elbv2')

    async def add_listener_certificates(
        self,
        request: ELBv2AddListenerCertificatesRequest,
    ) -> ELBv2AddListenerCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.add_listener_certificates, request, ELBv2AddListenerCertificatesResponse)

    async def add_tags(
        self,
        request: ELBv2AddTagsRequest,
    ) -> ELBv2AddTagsResponse:
        client = self._require_client()
        return await self._execute(client.add_tags, request, ELBv2AddTagsResponse)

    async def add_trust_store_revocations(
        self,
        request: ELBv2AddTrustStoreRevocationsRequest,
    ) -> ELBv2AddTrustStoreRevocationsResponse:
        client = self._require_client()
        return await self._execute(client.add_trust_store_revocations, request, ELBv2AddTrustStoreRevocationsResponse)

    async def create_listener(
        self,
        request: ELBv2CreateListenerRequest,
    ) -> ELBv2CreateListenerResponse:
        client = self._require_client()
        return await self._execute(client.create_listener, request, ELBv2CreateListenerResponse)

    async def create_load_balancer(
        self,
        request: ELBv2CreateLoadBalancerRequest,
    ) -> ELBv2CreateLoadBalancerResponse:
        client = self._require_client()
        return await self._execute(client.create_load_balancer, request, ELBv2CreateLoadBalancerResponse)

    async def create_rule(
        self,
        request: ELBv2CreateRuleRequest,
    ) -> ELBv2CreateRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_rule, request, ELBv2CreateRuleResponse)

    async def create_target_group(
        self,
        request: ELBv2CreateTargetGroupRequest,
    ) -> ELBv2CreateTargetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_target_group, request, ELBv2CreateTargetGroupResponse)

    async def create_trust_store(
        self,
        request: ELBv2CreateTrustStoreRequest,
    ) -> ELBv2CreateTrustStoreResponse:
        client = self._require_client()
        return await self._execute(client.create_trust_store, request, ELBv2CreateTrustStoreResponse)

    async def delete_listener(
        self,
        request: ELBv2DeleteListenerRequest,
    ) -> ELBv2DeleteListenerResponse:
        client = self._require_client()
        return await self._execute(client.delete_listener, request, ELBv2DeleteListenerResponse)

    async def delete_load_balancer(
        self,
        request: ELBv2DeleteLoadBalancerRequest,
    ) -> ELBv2DeleteLoadBalancerResponse:
        client = self._require_client()
        return await self._execute(client.delete_load_balancer, request, ELBv2DeleteLoadBalancerResponse)

    async def delete_rule(
        self,
        request: ELBv2DeleteRuleRequest,
    ) -> ELBv2DeleteRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_rule, request, ELBv2DeleteRuleResponse)

    async def delete_shared_trust_store_association(
        self,
        request: ELBv2DeleteSharedTrustStoreAssociationRequest,
    ) -> ELBv2DeleteSharedTrustStoreAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_shared_trust_store_association, request, ELBv2DeleteSharedTrustStoreAssociationResponse)

    async def delete_target_group(
        self,
        request: ELBv2DeleteTargetGroupRequest,
    ) -> ELBv2DeleteTargetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_target_group, request, ELBv2DeleteTargetGroupResponse)

    async def delete_trust_store(
        self,
        request: ELBv2DeleteTrustStoreRequest,
    ) -> ELBv2DeleteTrustStoreResponse:
        client = self._require_client()
        return await self._execute(client.delete_trust_store, request, ELBv2DeleteTrustStoreResponse)

    async def deregister_targets(
        self,
        request: ELBv2DeregisterTargetsRequest,
    ) -> ELBv2DeregisterTargetsResponse:
        client = self._require_client()
        return await self._execute(client.deregister_targets, request, ELBv2DeregisterTargetsResponse)

    async def describe_account_limits(
        self,
        request: ELBv2DescribeAccountLimitsRequest | None = None,
    ) -> ELBv2DescribeAccountLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_limits, request, ELBv2DescribeAccountLimitsResponse)

    async def describe_account_limits_paginated(
        self,
        request: ELBv2DescribeAccountLimitsRequest | None = None,
    ) -> list[ELBv2DescribeAccountLimitsResponse]:
        return await self._paginate('describe_account_limits', request, ELBv2DescribeAccountLimitsResponse)

    async def describe_capacity_reservation(
        self,
        request: ELBv2DescribeCapacityReservationRequest,
    ) -> ELBv2DescribeCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_reservation, request, ELBv2DescribeCapacityReservationResponse)

    async def describe_listener_attributes(
        self,
        request: ELBv2DescribeListenerAttributesRequest,
    ) -> ELBv2DescribeListenerAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_listener_attributes, request, ELBv2DescribeListenerAttributesResponse)

    async def describe_listener_certificates(
        self,
        request: ELBv2DescribeListenerCertificatesRequest,
    ) -> ELBv2DescribeListenerCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_listener_certificates, request, ELBv2DescribeListenerCertificatesResponse)

    async def describe_listener_certificates_paginated(
        self,
        request: ELBv2DescribeListenerCertificatesRequest,
    ) -> list[ELBv2DescribeListenerCertificatesResponse]:
        return await self._paginate('describe_listener_certificates', request, ELBv2DescribeListenerCertificatesResponse)

    async def describe_listeners(
        self,
        request: ELBv2DescribeListenersRequest | None = None,
    ) -> ELBv2DescribeListenersResponse:
        client = self._require_client()
        return await self._execute(client.describe_listeners, request, ELBv2DescribeListenersResponse)

    async def describe_listeners_paginated(
        self,
        request: ELBv2DescribeListenersRequest | None = None,
    ) -> list[ELBv2DescribeListenersResponse]:
        return await self._paginate('describe_listeners', request, ELBv2DescribeListenersResponse)

    async def describe_load_balancer_attributes(
        self,
        request: ELBv2DescribeLoadBalancerAttributesRequest,
    ) -> ELBv2DescribeLoadBalancerAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_load_balancer_attributes, request, ELBv2DescribeLoadBalancerAttributesResponse)

    async def describe_load_balancers(
        self,
        request: ELBv2DescribeLoadBalancersRequest | None = None,
    ) -> ELBv2DescribeLoadBalancersResponse:
        client = self._require_client()
        return await self._execute(client.describe_load_balancers, request, ELBv2DescribeLoadBalancersResponse)

    async def describe_load_balancers_paginated(
        self,
        request: ELBv2DescribeLoadBalancersRequest | None = None,
    ) -> list[ELBv2DescribeLoadBalancersResponse]:
        return await self._paginate('describe_load_balancers', request, ELBv2DescribeLoadBalancersResponse)

    async def describe_rules(
        self,
        request: ELBv2DescribeRulesRequest | None = None,
    ) -> ELBv2DescribeRulesResponse:
        client = self._require_client()
        return await self._execute(client.describe_rules, request, ELBv2DescribeRulesResponse)

    async def describe_rules_paginated(
        self,
        request: ELBv2DescribeRulesRequest | None = None,
    ) -> list[ELBv2DescribeRulesResponse]:
        return await self._paginate('describe_rules', request, ELBv2DescribeRulesResponse)

    async def describe_ssl_policies(
        self,
        request: ELBv2DescribeSSLPoliciesRequest | None = None,
    ) -> ELBv2DescribeSSLPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_ssl_policies, request, ELBv2DescribeSSLPoliciesResponse)

    async def describe_ssl_policies_paginated(
        self,
        request: ELBv2DescribeSSLPoliciesRequest | None = None,
    ) -> list[ELBv2DescribeSSLPoliciesResponse]:
        return await self._paginate('describe_ssl_policies', request, ELBv2DescribeSSLPoliciesResponse)

    async def describe_tags(
        self,
        request: ELBv2DescribeTagsRequest,
    ) -> ELBv2DescribeTagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_tags, request, ELBv2DescribeTagsResponse)

    async def describe_target_group_attributes(
        self,
        request: ELBv2DescribeTargetGroupAttributesRequest,
    ) -> ELBv2DescribeTargetGroupAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_target_group_attributes, request, ELBv2DescribeTargetGroupAttributesResponse)

    async def describe_target_groups(
        self,
        request: ELBv2DescribeTargetGroupsRequest | None = None,
    ) -> ELBv2DescribeTargetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_target_groups, request, ELBv2DescribeTargetGroupsResponse)

    async def describe_target_groups_paginated(
        self,
        request: ELBv2DescribeTargetGroupsRequest | None = None,
    ) -> list[ELBv2DescribeTargetGroupsResponse]:
        return await self._paginate('describe_target_groups', request, ELBv2DescribeTargetGroupsResponse)

    async def describe_target_health(
        self,
        request: ELBv2DescribeTargetHealthRequest,
    ) -> ELBv2DescribeTargetHealthResponse:
        client = self._require_client()
        return await self._execute(client.describe_target_health, request, ELBv2DescribeTargetHealthResponse)

    async def describe_trust_store_associations(
        self,
        request: ELBv2DescribeTrustStoreAssociationsRequest,
    ) -> ELBv2DescribeTrustStoreAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_trust_store_associations, request, ELBv2DescribeTrustStoreAssociationsResponse)

    async def describe_trust_store_associations_paginated(
        self,
        request: ELBv2DescribeTrustStoreAssociationsRequest,
    ) -> list[ELBv2DescribeTrustStoreAssociationsResponse]:
        return await self._paginate('describe_trust_store_associations', request, ELBv2DescribeTrustStoreAssociationsResponse)

    async def describe_trust_store_revocations(
        self,
        request: ELBv2DescribeTrustStoreRevocationsRequest,
    ) -> ELBv2DescribeTrustStoreRevocationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_trust_store_revocations, request, ELBv2DescribeTrustStoreRevocationsResponse)

    async def describe_trust_store_revocations_paginated(
        self,
        request: ELBv2DescribeTrustStoreRevocationsRequest,
    ) -> list[ELBv2DescribeTrustStoreRevocationsResponse]:
        return await self._paginate('describe_trust_store_revocations', request, ELBv2DescribeTrustStoreRevocationsResponse)

    async def describe_trust_stores(
        self,
        request: ELBv2DescribeTrustStoresRequest | None = None,
    ) -> ELBv2DescribeTrustStoresResponse:
        client = self._require_client()
        return await self._execute(client.describe_trust_stores, request, ELBv2DescribeTrustStoresResponse)

    async def describe_trust_stores_paginated(
        self,
        request: ELBv2DescribeTrustStoresRequest | None = None,
    ) -> list[ELBv2DescribeTrustStoresResponse]:
        return await self._paginate('describe_trust_stores', request, ELBv2DescribeTrustStoresResponse)

    async def get_resource_policy(
        self,
        request: ELBv2GetResourcePolicyRequest,
    ) -> ELBv2GetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, ELBv2GetResourcePolicyResponse)

    async def get_trust_store_ca_certificates_bundle(
        self,
        request: ELBv2GetTrustStoreCaCertificatesBundleRequest,
    ) -> ELBv2GetTrustStoreCaCertificatesBundleResponse:
        client = self._require_client()
        return await self._execute(client.get_trust_store_ca_certificates_bundle, request, ELBv2GetTrustStoreCaCertificatesBundleResponse)

    async def get_trust_store_revocation_content(
        self,
        request: ELBv2GetTrustStoreRevocationContentRequest,
    ) -> ELBv2GetTrustStoreRevocationContentResponse:
        client = self._require_client()
        return await self._execute(client.get_trust_store_revocation_content, request, ELBv2GetTrustStoreRevocationContentResponse)

    async def modify_capacity_reservation(
        self,
        request: ELBv2ModifyCapacityReservationRequest,
    ) -> ELBv2ModifyCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.modify_capacity_reservation, request, ELBv2ModifyCapacityReservationResponse)

    async def modify_ip_pools(
        self,
        request: ELBv2ModifyIpPoolsRequest,
    ) -> ELBv2ModifyIpPoolsResponse:
        client = self._require_client()
        return await self._execute(client.modify_ip_pools, request, ELBv2ModifyIpPoolsResponse)

    async def modify_listener(
        self,
        request: ELBv2ModifyListenerRequest,
    ) -> ELBv2ModifyListenerResponse:
        client = self._require_client()
        return await self._execute(client.modify_listener, request, ELBv2ModifyListenerResponse)

    async def modify_listener_attributes(
        self,
        request: ELBv2ModifyListenerAttributesRequest,
    ) -> ELBv2ModifyListenerAttributesResponse:
        client = self._require_client()
        return await self._execute(client.modify_listener_attributes, request, ELBv2ModifyListenerAttributesResponse)

    async def modify_load_balancer_attributes(
        self,
        request: ELBv2ModifyLoadBalancerAttributesRequest,
    ) -> ELBv2ModifyLoadBalancerAttributesResponse:
        client = self._require_client()
        return await self._execute(client.modify_load_balancer_attributes, request, ELBv2ModifyLoadBalancerAttributesResponse)

    async def modify_rule(
        self,
        request: ELBv2ModifyRuleRequest,
    ) -> ELBv2ModifyRuleResponse:
        client = self._require_client()
        return await self._execute(client.modify_rule, request, ELBv2ModifyRuleResponse)

    async def modify_target_group(
        self,
        request: ELBv2ModifyTargetGroupRequest,
    ) -> ELBv2ModifyTargetGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_target_group, request, ELBv2ModifyTargetGroupResponse)

    async def modify_target_group_attributes(
        self,
        request: ELBv2ModifyTargetGroupAttributesRequest,
    ) -> ELBv2ModifyTargetGroupAttributesResponse:
        client = self._require_client()
        return await self._execute(client.modify_target_group_attributes, request, ELBv2ModifyTargetGroupAttributesResponse)

    async def modify_trust_store(
        self,
        request: ELBv2ModifyTrustStoreRequest,
    ) -> ELBv2ModifyTrustStoreResponse:
        client = self._require_client()
        return await self._execute(client.modify_trust_store, request, ELBv2ModifyTrustStoreResponse)

    async def register_targets(
        self,
        request: ELBv2RegisterTargetsRequest,
    ) -> ELBv2RegisterTargetsResponse:
        client = self._require_client()
        return await self._execute(client.register_targets, request, ELBv2RegisterTargetsResponse)

    async def remove_listener_certificates(
        self,
        request: ELBv2RemoveListenerCertificatesRequest,
    ) -> ELBv2RemoveListenerCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.remove_listener_certificates, request, ELBv2RemoveListenerCertificatesResponse)

    async def remove_tags(
        self,
        request: ELBv2RemoveTagsRequest,
    ) -> ELBv2RemoveTagsResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags, request, ELBv2RemoveTagsResponse)

    async def remove_trust_store_revocations(
        self,
        request: ELBv2RemoveTrustStoreRevocationsRequest,
    ) -> ELBv2RemoveTrustStoreRevocationsResponse:
        client = self._require_client()
        return await self._execute(client.remove_trust_store_revocations, request, ELBv2RemoveTrustStoreRevocationsResponse)

    async def set_ip_address_type(
        self,
        request: ELBv2SetIpAddressTypeRequest,
    ) -> ELBv2SetIpAddressTypeResponse:
        client = self._require_client()
        return await self._execute(client.set_ip_address_type, request, ELBv2SetIpAddressTypeResponse)

    async def set_rule_priorities(
        self,
        request: ELBv2SetRulePrioritiesRequest,
    ) -> ELBv2SetRulePrioritiesResponse:
        client = self._require_client()
        return await self._execute(client.set_rule_priorities, request, ELBv2SetRulePrioritiesResponse)

    async def set_security_groups(
        self,
        request: ELBv2SetSecurityGroupsRequest,
    ) -> ELBv2SetSecurityGroupsResponse:
        client = self._require_client()
        return await self._execute(client.set_security_groups, request, ELBv2SetSecurityGroupsResponse)

    async def set_subnets(
        self,
        request: ELBv2SetSubnetsRequest,
    ) -> ELBv2SetSubnetsResponse:
        client = self._require_client()
        return await self._execute(client.set_subnets, request, ELBv2SetSubnetsResponse)
