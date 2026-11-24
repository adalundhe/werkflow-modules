from werkflow_aws.models.route53 import (
    Route53ChangeResourceRecordSetsRequest,
    Route53ChangeResourceRecordSetsResponse,
    Route53ChangeTagsForResourceRequest,
    Route53ChangeTagsForResourceResponse,
    Route53CreateHealthCheckRequest,
    Route53CreateHealthCheckResponse,
    Route53CreateHostedZoneRequest,
    Route53CreateHostedZoneResponse,
    Route53DeleteHealthCheckRequest,
    Route53DeleteHealthCheckResponse,
    Route53DeleteHostedZoneRequest,
    Route53DeleteHostedZoneResponse,
    Route53GetChangeRequest,
    Route53GetChangeResponse,
    Route53GetHealthCheckRequest,
    Route53GetHealthCheckResponse,
    Route53GetHealthCheckStatusRequest,
    Route53GetHealthCheckStatusResponse,
    Route53GetHostedZoneRequest,
    Route53GetHostedZoneResponse,
    Route53ListHealthChecksRequest,
    Route53ListHealthChecksResponse,
    Route53ListHostedZonesByNameRequest,
    Route53ListHostedZonesByNameResponse,
    Route53ListHostedZonesRequest,
    Route53ListHostedZonesResponse,
    Route53ListResourceRecordSetsRequest,
    Route53ListResourceRecordSetsResponse,
    Route53ListTagsForResourceRequest,
    Route53ListTagsForResourceResponse,
)
from werkflow_aws.services.base import AWSBaseService
from werkflow_aws.types.route53_client import Route53Client
from werkflow_aws.models.route53 import (
    Route53ActivateKeySigningKeyRequest,
    Route53ActivateKeySigningKeyResponse,
    Route53AssociateVPCWithHostedZoneRequest,
    Route53AssociateVPCWithHostedZoneResponse,
    Route53ChangeCidrCollectionRequest,
    Route53ChangeCidrCollectionResponse,
    Route53CreateCidrCollectionRequest,
    Route53CreateCidrCollectionResponse,
    Route53CreateHealthCheckSourceRequest,
    Route53CreateHealthCheckSourceResponse,
    Route53CreateKeySigningKeyRequest,
    Route53CreateKeySigningKeyResponse,
    Route53CreateQueryLoggingConfigRequest,
    Route53CreateQueryLoggingConfigResponse,
    Route53CreateResourceRecordSetProtectionsRequest,
    Route53CreateResourceRecordSetProtectionsResponse,
    Route53CreateReusableDelegationSetRequest,
    Route53CreateReusableDelegationSetResponse,
    Route53CreateTrafficPolicyInstanceRequest,
    Route53CreateTrafficPolicyInstanceResponse,
    Route53CreateTrafficPolicyRequest,
    Route53CreateTrafficPolicyResponse,
    Route53CreateTrafficPolicyVersionRequest,
    Route53CreateTrafficPolicyVersionResponse,
    Route53CreateVPCAssociationAuthorizationRequest,
    Route53CreateVPCAssociationAuthorizationResponse,
    Route53DeactivateKeySigningKeyRequest,
    Route53DeactivateKeySigningKeyResponse,
    Route53DeleteCidrCollectionRequest,
    Route53DeleteCidrCollectionResponse,
    Route53DeleteHealthCheckSourceRequest,
    Route53DeleteHealthCheckSourceResponse,
    Route53DeleteKeySigningKeyRequest,
    Route53DeleteKeySigningKeyResponse,
    Route53DeleteQueryLoggingConfigRequest,
    Route53DeleteQueryLoggingConfigResponse,
    Route53DeleteResourceRecordSetProtectionsRequest,
    Route53DeleteResourceRecordSetProtectionsResponse,
    Route53DeleteReusableDelegationSetRequest,
    Route53DeleteReusableDelegationSetResponse,
    Route53DeleteTrafficPolicyInstanceRequest,
    Route53DeleteTrafficPolicyInstanceResponse,
    Route53DeleteTrafficPolicyRequest,
    Route53DeleteTrafficPolicyResponse,
    Route53DeleteVPCAssociationAuthorizationRequest,
    Route53DeleteVPCAssociationAuthorizationResponse,
    Route53DisableHostedZoneDNSSECRequest,
    Route53DisableHostedZoneDNSSECResponse,
    Route53DisassociateVPCFromHostedZoneRequest,
    Route53DisassociateVPCFromHostedZoneResponse,
    Route53EnableHostedZoneDNSSECRequest,
    Route53EnableHostedZoneDNSSECResponse,
    Route53GetAccountLimitRequest,
    Route53GetAccountLimitResponse,
    Route53GetCheckerIpRangesRequest,
    Route53GetCheckerIpRangesResponse,
    Route53GetDNSSECRequest,
    Route53GetDNSSECResponse,
    Route53GetGeoLocationRequest,
    Route53GetGeoLocationResponse,
    Route53GetHealthCheckCountRequest,
    Route53GetHealthCheckCountResponse,
    Route53GetHealthCheckLastFailureReasonRequest,
    Route53GetHealthCheckLastFailureReasonResponse,
    Route53GetHealthCheckSourceRequest,
    Route53GetHealthCheckSourceResponse,
    Route53GetHostedZoneChangeBatchRequest,
    Route53GetHostedZoneChangeBatchResponse,
    Route53GetHostedZoneCountRequest,
    Route53GetHostedZoneCountResponse,
    Route53GetHostedZoneLimitRequest,
    Route53GetHostedZoneLimitResponse,
    Route53GetQueryLoggingConfigRequest,
    Route53GetQueryLoggingConfigResponse,
    Route53GetReusableDelegationSetLimitRequest,
    Route53GetReusableDelegationSetLimitResponse,
    Route53GetReusableDelegationSetRequest,
    Route53GetReusableDelegationSetResponse,
    Route53GetTrafficPolicyInstanceCountRequest,
    Route53GetTrafficPolicyInstanceCountResponse,
    Route53GetTrafficPolicyInstanceRequest,
    Route53GetTrafficPolicyInstanceResponse,
    Route53GetTrafficPolicyRequest,
    Route53GetTrafficPolicyResponse,
    Route53ListCidrBlocksRequest,
    Route53ListCidrBlocksResponse,
    Route53ListCidrCollectionsRequest,
    Route53ListCidrCollectionsResponse,
    Route53ListCidrLocationsRequest,
    Route53ListCidrLocationsResponse,
    Route53ListGeoLocationsRequest,
    Route53ListGeoLocationsResponse,
    Route53ListHealthCheckSourcesRequest,
    Route53ListHealthCheckSourcesResponse,
    Route53ListHealthChecksBySourceRequest,
    Route53ListHealthChecksBySourceResponse,
    Route53ListHostedZoneChangeBatchesRequest,
    Route53ListHostedZoneChangeBatchesResponse,
    Route53ListHostedZonesByVPCRequest,
    Route53ListHostedZonesByVPCResponse,
    Route53ListQueryLoggingConfigsRequest,
    Route53ListQueryLoggingConfigsResponse,
    Route53ListResourceRecordSetChangesRequest,
    Route53ListResourceRecordSetChangesResponse,
    Route53ListResourceRecordSetProtectionsRequest,
    Route53ListResourceRecordSetProtectionsResponse,
    Route53ListReusableDelegationSetsRequest,
    Route53ListReusableDelegationSetsResponse,
    Route53ListTagsForResourcesRequest,
    Route53ListTagsForResourcesResponse,
    Route53ListTrafficPoliciesRequest,
    Route53ListTrafficPoliciesResponse,
    Route53ListTrafficPolicyInstancesByHostedZoneRequest,
    Route53ListTrafficPolicyInstancesByHostedZoneResponse,
    Route53ListTrafficPolicyInstancesByPolicyRequest,
    Route53ListTrafficPolicyInstancesByPolicyResponse,
    Route53ListTrafficPolicyInstancesRequest,
    Route53ListTrafficPolicyInstancesResponse,
    Route53ListTrafficPolicyVersionsRequest,
    Route53ListTrafficPolicyVersionsResponse,
    Route53ListVPCAssociationAuthorizationsRequest,
    Route53ListVPCAssociationAuthorizationsResponse,
    Route53TestDNSAnswerRequest,
    Route53TestDNSAnswerResponse,
    Route53UpdateHealthCheckRequest,
    Route53UpdateHealthCheckResponse,
    Route53UpdateHostedZoneCommentRequest,
    Route53UpdateHostedZoneCommentResponse,
    Route53UpdateHostedZoneFeaturesRequest,
    Route53UpdateHostedZoneFeaturesResponse,
    Route53UpdateHostedZoneTierRequest,
    Route53UpdateHostedZoneTierResponse,
    Route53UpdateTrafficPolicyCommentRequest,
    Route53UpdateTrafficPolicyCommentResponse,
    Route53UpdateTrafficPolicyInstanceRequest,
    Route53UpdateTrafficPolicyInstanceResponse,
)


class AWSRoute53(AWSBaseService[Route53Client]):
    service_name = 'Route53'
    boto3_service_name = 'route53'

    async def list_hosted_zones(
        self,
        request: Route53ListHostedZonesRequest | None = None,
    ) -> Route53ListHostedZonesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_hosted_zones,
            request,
            Route53ListHostedZonesResponse,
        )

    async def list_hosted_zones_paginated(
        self,
        request: Route53ListHostedZonesRequest | None = None,
    ) -> list[Route53ListHostedZonesResponse]:
        self._require_client()
        return await self._paginate(
            'list_hosted_zones',
            request,
            Route53ListHostedZonesResponse,
        )

    async def list_hosted_zones_by_name(
        self,
        request: Route53ListHostedZonesByNameRequest | None = None,
    ) -> Route53ListHostedZonesByNameResponse:
        client = self._require_client()
        return await self._execute(
            client.list_hosted_zones_by_name,
            request,
            Route53ListHostedZonesByNameResponse,
        )

    async def get_hosted_zone(
        self,
        request: Route53GetHostedZoneRequest,
    ) -> Route53GetHostedZoneResponse:
        client = self._require_client()
        return await self._execute(
            client.get_hosted_zone,
            request,
            Route53GetHostedZoneResponse,
        )

    async def create_hosted_zone(
        self,
        request: Route53CreateHostedZoneRequest,
    ) -> Route53CreateHostedZoneResponse:
        client = self._require_client()
        return await self._execute(
            client.create_hosted_zone,
            request,
            Route53CreateHostedZoneResponse,
        )

    async def delete_hosted_zone(
        self,
        request: Route53DeleteHostedZoneRequest,
    ) -> Route53DeleteHostedZoneResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_hosted_zone,
            request,
            Route53DeleteHostedZoneResponse,
        )

    async def list_resource_record_sets(
        self,
        request: Route53ListResourceRecordSetsRequest,
    ) -> Route53ListResourceRecordSetsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_resource_record_sets,
            request,
            Route53ListResourceRecordSetsResponse,
        )

    async def list_resource_record_sets_paginated(
        self,
        request: Route53ListResourceRecordSetsRequest,
    ) -> list[Route53ListResourceRecordSetsResponse]:
        self._require_client()
        return await self._paginate(
            'list_resource_record_sets',
            request,
            Route53ListResourceRecordSetsResponse,
        )

    async def change_resource_record_sets(
        self,
        request: Route53ChangeResourceRecordSetsRequest,
    ) -> Route53ChangeResourceRecordSetsResponse:
        client = self._require_client()
        return await self._execute(
            client.change_resource_record_sets,
            request,
            Route53ChangeResourceRecordSetsResponse,
        )

    async def get_change(
        self,
        request: Route53GetChangeRequest,
    ) -> Route53GetChangeResponse:
        client = self._require_client()
        return await self._execute(
            client.get_change,
            request,
            Route53GetChangeResponse,
        )

    async def list_health_checks(
        self,
        request: Route53ListHealthChecksRequest | None = None,
    ) -> Route53ListHealthChecksResponse:
        client = self._require_client()
        return await self._execute(
            client.list_health_checks,
            request,
            Route53ListHealthChecksResponse,
        )

    async def list_health_checks_paginated(
        self,
        request: Route53ListHealthChecksRequest | None = None,
    ) -> list[Route53ListHealthChecksResponse]:
        self._require_client()
        return await self._paginate(
            'list_health_checks',
            request,
            Route53ListHealthChecksResponse,
        )

    async def get_health_check(
        self,
        request: Route53GetHealthCheckRequest,
    ) -> Route53GetHealthCheckResponse:
        client = self._require_client()
        return await self._execute(
            client.get_health_check,
            request,
            Route53GetHealthCheckResponse,
        )

    async def get_health_check_status(
        self,
        request: Route53GetHealthCheckStatusRequest,
    ) -> Route53GetHealthCheckStatusResponse:
        client = self._require_client()
        return await self._execute(
            client.get_health_check_status,
            request,
            Route53GetHealthCheckStatusResponse,
        )

    async def create_health_check(
        self,
        request: Route53CreateHealthCheckRequest,
    ) -> Route53CreateHealthCheckResponse:
        client = self._require_client()
        return await self._execute(
            client.create_health_check,
            request,
            Route53CreateHealthCheckResponse,
        )

    async def delete_health_check(
        self,
        request: Route53DeleteHealthCheckRequest,
    ) -> Route53DeleteHealthCheckResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_health_check,
            request,
            Route53DeleteHealthCheckResponse,
        )

    async def list_tags_for_resource(
        self,
        request: Route53ListTagsForResourceRequest,
    ) -> Route53ListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tags_for_resource,
            request,
            Route53ListTagsForResourceResponse,
        )

    async def change_tags_for_resource(
        self,
        request: Route53ChangeTagsForResourceRequest,
    ) -> Route53ChangeTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.change_tags_for_resource,
            request,
            Route53ChangeTagsForResourceResponse,
        )

    async def activate_key_signing_key(
        self,
        request: Route53ActivateKeySigningKeyRequest,
    ) -> Route53ActivateKeySigningKeyResponse:
        client = self._require_client()
        return await self._execute(client.activate_key_signing_key, request, Route53ActivateKeySigningKeyResponse)

    async def associate_vpc_with_hosted_zone(
        self,
        request: Route53AssociateVPCWithHostedZoneRequest,
    ) -> Route53AssociateVPCWithHostedZoneResponse:
        client = self._require_client()
        return await self._execute(client.associate_vpc_with_hosted_zone, request, Route53AssociateVPCWithHostedZoneResponse)

    async def change_cidr_collection(
        self,
        request: Route53ChangeCidrCollectionRequest,
    ) -> Route53ChangeCidrCollectionResponse:
        client = self._require_client()
        return await self._execute(client.change_cidr_collection, request, Route53ChangeCidrCollectionResponse)

    async def create_cidr_collection(
        self,
        request: Route53CreateCidrCollectionRequest,
    ) -> Route53CreateCidrCollectionResponse:
        client = self._require_client()
        return await self._execute(client.create_cidr_collection, request, Route53CreateCidrCollectionResponse)

    async def create_health_check_source(
        self,
        request: Route53CreateHealthCheckSourceRequest,
    ) -> Route53CreateHealthCheckSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_health_check_source, request, Route53CreateHealthCheckSourceResponse)

    async def create_key_signing_key(
        self,
        request: Route53CreateKeySigningKeyRequest,
    ) -> Route53CreateKeySigningKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_key_signing_key, request, Route53CreateKeySigningKeyResponse)

    async def create_query_logging_config(
        self,
        request: Route53CreateQueryLoggingConfigRequest,
    ) -> Route53CreateQueryLoggingConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_query_logging_config, request, Route53CreateQueryLoggingConfigResponse)

    async def create_resource_record_set_protections(
        self,
        request: Route53CreateResourceRecordSetProtectionsRequest,
    ) -> Route53CreateResourceRecordSetProtectionsResponse:
        client = self._require_client()
        return await self._execute(client.create_resource_record_set_protections, request, Route53CreateResourceRecordSetProtectionsResponse)

    async def create_reusable_delegation_set(
        self,
        request: Route53CreateReusableDelegationSetRequest,
    ) -> Route53CreateReusableDelegationSetResponse:
        client = self._require_client()
        return await self._execute(client.create_reusable_delegation_set, request, Route53CreateReusableDelegationSetResponse)

    async def create_traffic_policy(
        self,
        request: Route53CreateTrafficPolicyRequest,
    ) -> Route53CreateTrafficPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_traffic_policy, request, Route53CreateTrafficPolicyResponse)

    async def create_traffic_policy_instance(
        self,
        request: Route53CreateTrafficPolicyInstanceRequest,
    ) -> Route53CreateTrafficPolicyInstanceResponse:
        client = self._require_client()
        return await self._execute(client.create_traffic_policy_instance, request, Route53CreateTrafficPolicyInstanceResponse)

    async def create_traffic_policy_version(
        self,
        request: Route53CreateTrafficPolicyVersionRequest,
    ) -> Route53CreateTrafficPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_traffic_policy_version, request, Route53CreateTrafficPolicyVersionResponse)

    async def create_vpc_association_authorization(
        self,
        request: Route53CreateVPCAssociationAuthorizationRequest,
    ) -> Route53CreateVPCAssociationAuthorizationResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_association_authorization, request, Route53CreateVPCAssociationAuthorizationResponse)

    async def deactivate_key_signing_key(
        self,
        request: Route53DeactivateKeySigningKeyRequest,
    ) -> Route53DeactivateKeySigningKeyResponse:
        client = self._require_client()
        return await self._execute(client.deactivate_key_signing_key, request, Route53DeactivateKeySigningKeyResponse)

    async def delete_cidr_collection(
        self,
        request: Route53DeleteCidrCollectionRequest,
    ) -> Route53DeleteCidrCollectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_cidr_collection, request, Route53DeleteCidrCollectionResponse)

    async def delete_health_check_source(
        self,
        request: Route53DeleteHealthCheckSourceRequest,
    ) -> Route53DeleteHealthCheckSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_health_check_source, request, Route53DeleteHealthCheckSourceResponse)

    async def delete_key_signing_key(
        self,
        request: Route53DeleteKeySigningKeyRequest,
    ) -> Route53DeleteKeySigningKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_key_signing_key, request, Route53DeleteKeySigningKeyResponse)

    async def delete_query_logging_config(
        self,
        request: Route53DeleteQueryLoggingConfigRequest,
    ) -> Route53DeleteQueryLoggingConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_query_logging_config, request, Route53DeleteQueryLoggingConfigResponse)

    async def delete_resource_record_set_protections(
        self,
        request: Route53DeleteResourceRecordSetProtectionsRequest,
    ) -> Route53DeleteResourceRecordSetProtectionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_record_set_protections, request, Route53DeleteResourceRecordSetProtectionsResponse)

    async def delete_reusable_delegation_set(
        self,
        request: Route53DeleteReusableDelegationSetRequest,
    ) -> Route53DeleteReusableDelegationSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_reusable_delegation_set, request, Route53DeleteReusableDelegationSetResponse)

    async def delete_traffic_policy(
        self,
        request: Route53DeleteTrafficPolicyRequest,
    ) -> Route53DeleteTrafficPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_traffic_policy, request, Route53DeleteTrafficPolicyResponse)

    async def delete_traffic_policy_instance(
        self,
        request: Route53DeleteTrafficPolicyInstanceRequest,
    ) -> Route53DeleteTrafficPolicyInstanceResponse:
        client = self._require_client()
        return await self._execute(client.delete_traffic_policy_instance, request, Route53DeleteTrafficPolicyInstanceResponse)

    async def delete_vpc_association_authorization(
        self,
        request: Route53DeleteVPCAssociationAuthorizationRequest,
    ) -> Route53DeleteVPCAssociationAuthorizationResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_association_authorization, request, Route53DeleteVPCAssociationAuthorizationResponse)

    async def disable_hosted_zone_dnssec(
        self,
        request: Route53DisableHostedZoneDNSSECRequest,
    ) -> Route53DisableHostedZoneDNSSECResponse:
        client = self._require_client()
        return await self._execute(client.disable_hosted_zone_dnssec, request, Route53DisableHostedZoneDNSSECResponse)

    async def disassociate_vpc_from_hosted_zone(
        self,
        request: Route53DisassociateVPCFromHostedZoneRequest,
    ) -> Route53DisassociateVPCFromHostedZoneResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_vpc_from_hosted_zone, request, Route53DisassociateVPCFromHostedZoneResponse)

    async def enable_hosted_zone_dnssec(
        self,
        request: Route53EnableHostedZoneDNSSECRequest,
    ) -> Route53EnableHostedZoneDNSSECResponse:
        client = self._require_client()
        return await self._execute(client.enable_hosted_zone_dnssec, request, Route53EnableHostedZoneDNSSECResponse)

    async def get_account_limit(
        self,
        request: Route53GetAccountLimitRequest,
    ) -> Route53GetAccountLimitResponse:
        client = self._require_client()
        return await self._execute(client.get_account_limit, request, Route53GetAccountLimitResponse)

    async def get_checker_ip_ranges(
        self,
        request: Route53GetCheckerIpRangesRequest | None = None,
    ) -> Route53GetCheckerIpRangesResponse:
        client = self._require_client()
        return await self._execute(client.get_checker_ip_ranges, request, Route53GetCheckerIpRangesResponse)

    async def get_dnssec(
        self,
        request: Route53GetDNSSECRequest,
    ) -> Route53GetDNSSECResponse:
        client = self._require_client()
        return await self._execute(client.get_dnssec, request, Route53GetDNSSECResponse)

    async def get_geo_location(
        self,
        request: Route53GetGeoLocationRequest | None = None,
    ) -> Route53GetGeoLocationResponse:
        client = self._require_client()
        return await self._execute(client.get_geo_location, request, Route53GetGeoLocationResponse)

    async def get_health_check_count(
        self,
        request: Route53GetHealthCheckCountRequest | None = None,
    ) -> Route53GetHealthCheckCountResponse:
        client = self._require_client()
        return await self._execute(client.get_health_check_count, request, Route53GetHealthCheckCountResponse)

    async def get_health_check_last_failure_reason(
        self,
        request: Route53GetHealthCheckLastFailureReasonRequest,
    ) -> Route53GetHealthCheckLastFailureReasonResponse:
        client = self._require_client()
        return await self._execute(client.get_health_check_last_failure_reason, request, Route53GetHealthCheckLastFailureReasonResponse)

    async def get_health_check_source(
        self,
        request: Route53GetHealthCheckSourceRequest,
    ) -> Route53GetHealthCheckSourceResponse:
        client = self._require_client()
        return await self._execute(client.get_health_check_source, request, Route53GetHealthCheckSourceResponse)

    async def get_hosted_zone_change_batch(
        self,
        request: Route53GetHostedZoneChangeBatchRequest,
    ) -> Route53GetHostedZoneChangeBatchResponse:
        client = self._require_client()
        return await self._execute(client.get_hosted_zone_change_batch, request, Route53GetHostedZoneChangeBatchResponse)

    async def get_hosted_zone_count(
        self,
        request: Route53GetHostedZoneCountRequest | None = None,
    ) -> Route53GetHostedZoneCountResponse:
        client = self._require_client()
        return await self._execute(client.get_hosted_zone_count, request, Route53GetHostedZoneCountResponse)

    async def get_hosted_zone_limit(
        self,
        request: Route53GetHostedZoneLimitRequest,
    ) -> Route53GetHostedZoneLimitResponse:
        client = self._require_client()
        return await self._execute(client.get_hosted_zone_limit, request, Route53GetHostedZoneLimitResponse)

    async def get_query_logging_config(
        self,
        request: Route53GetQueryLoggingConfigRequest,
    ) -> Route53GetQueryLoggingConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_query_logging_config, request, Route53GetQueryLoggingConfigResponse)

    async def get_reusable_delegation_set(
        self,
        request: Route53GetReusableDelegationSetRequest,
    ) -> Route53GetReusableDelegationSetResponse:
        client = self._require_client()
        return await self._execute(client.get_reusable_delegation_set, request, Route53GetReusableDelegationSetResponse)

    async def get_reusable_delegation_set_limit(
        self,
        request: Route53GetReusableDelegationSetLimitRequest,
    ) -> Route53GetReusableDelegationSetLimitResponse:
        client = self._require_client()
        return await self._execute(client.get_reusable_delegation_set_limit, request, Route53GetReusableDelegationSetLimitResponse)

    async def get_traffic_policy(
        self,
        request: Route53GetTrafficPolicyRequest,
    ) -> Route53GetTrafficPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_traffic_policy, request, Route53GetTrafficPolicyResponse)

    async def get_traffic_policy_instance(
        self,
        request: Route53GetTrafficPolicyInstanceRequest,
    ) -> Route53GetTrafficPolicyInstanceResponse:
        client = self._require_client()
        return await self._execute(client.get_traffic_policy_instance, request, Route53GetTrafficPolicyInstanceResponse)

    async def get_traffic_policy_instance_count(
        self,
        request: Route53GetTrafficPolicyInstanceCountRequest | None = None,
    ) -> Route53GetTrafficPolicyInstanceCountResponse:
        client = self._require_client()
        return await self._execute(client.get_traffic_policy_instance_count, request, Route53GetTrafficPolicyInstanceCountResponse)

    async def list_cidr_blocks(
        self,
        request: Route53ListCidrBlocksRequest,
    ) -> Route53ListCidrBlocksResponse:
        client = self._require_client()
        return await self._execute(client.list_cidr_blocks, request, Route53ListCidrBlocksResponse)

    async def list_cidr_blocks_paginated(
        self,
        request: Route53ListCidrBlocksRequest,
    ) -> list[Route53ListCidrBlocksResponse]:
        return await self._paginate('list_cidr_blocks', request, Route53ListCidrBlocksResponse)

    async def list_cidr_collections(
        self,
        request: Route53ListCidrCollectionsRequest | None = None,
    ) -> Route53ListCidrCollectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_cidr_collections, request, Route53ListCidrCollectionsResponse)

    async def list_cidr_collections_paginated(
        self,
        request: Route53ListCidrCollectionsRequest | None = None,
    ) -> list[Route53ListCidrCollectionsResponse]:
        return await self._paginate('list_cidr_collections', request, Route53ListCidrCollectionsResponse)

    async def list_cidr_locations(
        self,
        request: Route53ListCidrLocationsRequest,
    ) -> Route53ListCidrLocationsResponse:
        client = self._require_client()
        return await self._execute(client.list_cidr_locations, request, Route53ListCidrLocationsResponse)

    async def list_cidr_locations_paginated(
        self,
        request: Route53ListCidrLocationsRequest,
    ) -> list[Route53ListCidrLocationsResponse]:
        return await self._paginate('list_cidr_locations', request, Route53ListCidrLocationsResponse)

    async def list_geo_locations(
        self,
        request: Route53ListGeoLocationsRequest | None = None,
    ) -> Route53ListGeoLocationsResponse:
        client = self._require_client()
        return await self._execute(client.list_geo_locations, request, Route53ListGeoLocationsResponse)

    async def list_health_check_sources(
        self,
        request: Route53ListHealthCheckSourcesRequest | None = None,
    ) -> Route53ListHealthCheckSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_health_check_sources, request, Route53ListHealthCheckSourcesResponse)

    async def list_health_check_sources_paginated(
        self,
        request: Route53ListHealthCheckSourcesRequest | None = None,
    ) -> list[Route53ListHealthCheckSourcesResponse]:
        return await self._paginate('list_health_check_sources', request, Route53ListHealthCheckSourcesResponse)

    async def list_health_checks_by_source(
        self,
        request: Route53ListHealthChecksBySourceRequest,
    ) -> Route53ListHealthChecksBySourceResponse:
        client = self._require_client()
        return await self._execute(client.list_health_checks_by_source, request, Route53ListHealthChecksBySourceResponse)

    async def list_health_checks_by_source_paginated(
        self,
        request: Route53ListHealthChecksBySourceRequest,
    ) -> list[Route53ListHealthChecksBySourceResponse]:
        return await self._paginate('list_health_checks_by_source', request, Route53ListHealthChecksBySourceResponse)

    async def list_hosted_zone_change_batches(
        self,
        request: Route53ListHostedZoneChangeBatchesRequest,
    ) -> Route53ListHostedZoneChangeBatchesResponse:
        client = self._require_client()
        return await self._execute(client.list_hosted_zone_change_batches, request, Route53ListHostedZoneChangeBatchesResponse)

    async def list_hosted_zone_change_batches_paginated(
        self,
        request: Route53ListHostedZoneChangeBatchesRequest,
    ) -> list[Route53ListHostedZoneChangeBatchesResponse]:
        return await self._paginate('list_hosted_zone_change_batches', request, Route53ListHostedZoneChangeBatchesResponse)

    async def list_hosted_zones_by_vpc(
        self,
        request: Route53ListHostedZonesByVPCRequest,
    ) -> Route53ListHostedZonesByVPCResponse:
        client = self._require_client()
        return await self._execute(client.list_hosted_zones_by_vpc, request, Route53ListHostedZonesByVPCResponse)

    async def list_query_logging_configs(
        self,
        request: Route53ListQueryLoggingConfigsRequest | None = None,
    ) -> Route53ListQueryLoggingConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_query_logging_configs, request, Route53ListQueryLoggingConfigsResponse)

    async def list_query_logging_configs_paginated(
        self,
        request: Route53ListQueryLoggingConfigsRequest | None = None,
    ) -> list[Route53ListQueryLoggingConfigsResponse]:
        return await self._paginate('list_query_logging_configs', request, Route53ListQueryLoggingConfigsResponse)

    async def list_resource_record_set_changes(
        self,
        request: Route53ListResourceRecordSetChangesRequest,
    ) -> Route53ListResourceRecordSetChangesResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_record_set_changes, request, Route53ListResourceRecordSetChangesResponse)

    async def list_resource_record_set_changes_paginated(
        self,
        request: Route53ListResourceRecordSetChangesRequest,
    ) -> list[Route53ListResourceRecordSetChangesResponse]:
        return await self._paginate('list_resource_record_set_changes', request, Route53ListResourceRecordSetChangesResponse)

    async def list_resource_record_set_protections(
        self,
        request: Route53ListResourceRecordSetProtectionsRequest,
    ) -> Route53ListResourceRecordSetProtectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_record_set_protections, request, Route53ListResourceRecordSetProtectionsResponse)

    async def list_resource_record_set_protections_paginated(
        self,
        request: Route53ListResourceRecordSetProtectionsRequest,
    ) -> list[Route53ListResourceRecordSetProtectionsResponse]:
        return await self._paginate('list_resource_record_set_protections', request, Route53ListResourceRecordSetProtectionsResponse)

    async def list_reusable_delegation_sets(
        self,
        request: Route53ListReusableDelegationSetsRequest | None = None,
    ) -> Route53ListReusableDelegationSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_reusable_delegation_sets, request, Route53ListReusableDelegationSetsResponse)

    async def list_tags_for_resources(
        self,
        request: Route53ListTagsForResourcesRequest,
    ) -> Route53ListTagsForResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resources, request, Route53ListTagsForResourcesResponse)

    async def list_traffic_policies(
        self,
        request: Route53ListTrafficPoliciesRequest | None = None,
    ) -> Route53ListTrafficPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_traffic_policies, request, Route53ListTrafficPoliciesResponse)

    async def list_traffic_policy_instances(
        self,
        request: Route53ListTrafficPolicyInstancesRequest | None = None,
    ) -> Route53ListTrafficPolicyInstancesResponse:
        client = self._require_client()
        return await self._execute(client.list_traffic_policy_instances, request, Route53ListTrafficPolicyInstancesResponse)

    async def list_traffic_policy_instances_by_hosted_zone(
        self,
        request: Route53ListTrafficPolicyInstancesByHostedZoneRequest,
    ) -> Route53ListTrafficPolicyInstancesByHostedZoneResponse:
        client = self._require_client()
        return await self._execute(client.list_traffic_policy_instances_by_hosted_zone, request, Route53ListTrafficPolicyInstancesByHostedZoneResponse)

    async def list_traffic_policy_instances_by_policy(
        self,
        request: Route53ListTrafficPolicyInstancesByPolicyRequest,
    ) -> Route53ListTrafficPolicyInstancesByPolicyResponse:
        client = self._require_client()
        return await self._execute(client.list_traffic_policy_instances_by_policy, request, Route53ListTrafficPolicyInstancesByPolicyResponse)

    async def list_traffic_policy_versions(
        self,
        request: Route53ListTrafficPolicyVersionsRequest,
    ) -> Route53ListTrafficPolicyVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_traffic_policy_versions, request, Route53ListTrafficPolicyVersionsResponse)

    async def list_vpc_association_authorizations(
        self,
        request: Route53ListVPCAssociationAuthorizationsRequest,
    ) -> Route53ListVPCAssociationAuthorizationsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_association_authorizations, request, Route53ListVPCAssociationAuthorizationsResponse)

    async def list_vpc_association_authorizations_paginated(
        self,
        request: Route53ListVPCAssociationAuthorizationsRequest,
    ) -> list[Route53ListVPCAssociationAuthorizationsResponse]:
        return await self._paginate('list_vpc_association_authorizations', request, Route53ListVPCAssociationAuthorizationsResponse)

    async def test_dns_answer(
        self,
        request: Route53TestDNSAnswerRequest,
    ) -> Route53TestDNSAnswerResponse:
        client = self._require_client()
        return await self._execute(client.test_dns_answer, request, Route53TestDNSAnswerResponse)

    async def update_health_check(
        self,
        request: Route53UpdateHealthCheckRequest,
    ) -> Route53UpdateHealthCheckResponse:
        client = self._require_client()
        return await self._execute(client.update_health_check, request, Route53UpdateHealthCheckResponse)

    async def update_hosted_zone_comment(
        self,
        request: Route53UpdateHostedZoneCommentRequest,
    ) -> Route53UpdateHostedZoneCommentResponse:
        client = self._require_client()
        return await self._execute(client.update_hosted_zone_comment, request, Route53UpdateHostedZoneCommentResponse)

    async def update_hosted_zone_features(
        self,
        request: Route53UpdateHostedZoneFeaturesRequest,
    ) -> Route53UpdateHostedZoneFeaturesResponse:
        client = self._require_client()
        return await self._execute(client.update_hosted_zone_features, request, Route53UpdateHostedZoneFeaturesResponse)

    async def update_hosted_zone_tier(
        self,
        request: Route53UpdateHostedZoneTierRequest,
    ) -> Route53UpdateHostedZoneTierResponse:
        client = self._require_client()
        return await self._execute(client.update_hosted_zone_tier, request, Route53UpdateHostedZoneTierResponse)

    async def update_traffic_policy_comment(
        self,
        request: Route53UpdateTrafficPolicyCommentRequest,
    ) -> Route53UpdateTrafficPolicyCommentResponse:
        client = self._require_client()
        return await self._execute(client.update_traffic_policy_comment, request, Route53UpdateTrafficPolicyCommentResponse)

    async def update_traffic_policy_instance(
        self,
        request: Route53UpdateTrafficPolicyInstanceRequest,
    ) -> Route53UpdateTrafficPolicyInstanceResponse:
        client = self._require_client()
        return await self._execute(client.update_traffic_policy_instance, request, Route53UpdateTrafficPolicyInstanceResponse)

