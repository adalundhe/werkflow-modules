from werkflow_aws.models.cloudwatch_events import (
    EventBridgeActivateEventSourceRequest,
    EventBridgeActivateEventSourceResponse,
    EventBridgeCancelReplayRequest,
    EventBridgeCancelReplayResponse,
    EventBridgeCreateApiDestinationRequest,
    EventBridgeCreateApiDestinationResponse,
    EventBridgeCreateArchiveRequest,
    EventBridgeCreateArchiveResponse,
    EventBridgeCreateConnectionRequest,
    EventBridgeCreateConnectionResponse,
    EventBridgeCreateEndpointRequest,
    EventBridgeCreateEndpointResponse,
    EventBridgeCreateEventBusRequest,
    EventBridgeCreateEventBusResponse,
    EventBridgeCreatePartnerEventSourceRequest,
    EventBridgeCreatePartnerEventSourceResponse,
    EventBridgeDeactivateEventSourceRequest,
    EventBridgeDeactivateEventSourceResponse,
    EventBridgeDeauthorizeConnectionRequest,
    EventBridgeDeauthorizeConnectionResponse,
    EventBridgeDeleteApiDestinationRequest,
    EventBridgeDeleteApiDestinationResponse,
    EventBridgeDeleteArchiveRequest,
    EventBridgeDeleteArchiveResponse,
    EventBridgeDeleteConnectionRequest,
    EventBridgeDeleteConnectionResponse,
    EventBridgeDeleteEndpointRequest,
    EventBridgeDeleteEndpointResponse,
    EventBridgeDeleteEventBusRequest,
    EventBridgeDeleteEventBusResponse,
    EventBridgeDeletePartnerEventSourceRequest,
    EventBridgeDeletePartnerEventSourceResponse,
    EventBridgeDeleteRuleRequest,
    EventBridgeDeleteRuleResponse,
    EventBridgeDescribeApiDestinationRequest,
    EventBridgeDescribeApiDestinationResponse,
    EventBridgeDescribeArchiveRequest,
    EventBridgeDescribeArchiveResponse,
    EventBridgeDescribeConnectionRequest,
    EventBridgeDescribeConnectionResponse,
    EventBridgeDescribeEndpointRequest,
    EventBridgeDescribeEndpointResponse,
    EventBridgeDescribeEventBusRequest,
    EventBridgeDescribeEventBusResponse,
    EventBridgeDescribeEventSourceRequest,
    EventBridgeDescribeEventSourceResponse,
    EventBridgeDescribePartnerEventSourceRequest,
    EventBridgeDescribePartnerEventSourceResponse,
    EventBridgeDescribeReplayRequest,
    EventBridgeDescribeReplayResponse,
    EventBridgeDescribeRuleRequest,
    EventBridgeDescribeRuleResponse,
    EventBridgeDisableRuleRequest,
    EventBridgeDisableRuleResponse,
    EventBridgeEnableRuleRequest,
    EventBridgeEnableRuleResponse,
    EventBridgeListApiDestinationsRequest,
    EventBridgeListApiDestinationsResponse,
    EventBridgeListArchivesRequest,
    EventBridgeListArchivesResponse,
    EventBridgeListConnectionsRequest,
    EventBridgeListConnectionsResponse,
    EventBridgeListEndpointsRequest,
    EventBridgeListEndpointsResponse,
    EventBridgeListEventBusesRequest,
    EventBridgeListEventBusesResponse,
    EventBridgeListEventSourcesRequest,
    EventBridgeListEventSourcesResponse,
    EventBridgeListPartnerEventSourceAccountsRequest,
    EventBridgeListPartnerEventSourceAccountsResponse,
    EventBridgeListPartnerEventSourcesRequest,
    EventBridgeListPartnerEventSourcesResponse,
    EventBridgeListReplaysRequest,
    EventBridgeListReplaysResponse,
    EventBridgeListRuleNamesByTargetRequest,
    EventBridgeListRuleNamesByTargetResponse,
    EventBridgeListRulesRequest,
    EventBridgeListRulesResponse,
    EventBridgeListTagsForResourceRequest,
    EventBridgeListTagsForResourceResponse,
    EventBridgeListTargetsByRuleRequest,
    EventBridgeListTargetsByRuleResponse,
    EventBridgePutEventsRequest,
    EventBridgePutEventsResponse,
    EventBridgePutPartnerEventsRequest,
    EventBridgePutPartnerEventsResponse,
    EventBridgePutPermissionRequest,
    EventBridgePutPermissionResponse,
    EventBridgePutRuleRequest,
    EventBridgePutRuleResponse,
    EventBridgePutTargetsRequest,
    EventBridgePutTargetsResponse,
    EventBridgeRemovePermissionRequest,
    EventBridgeRemovePermissionResponse,
    EventBridgeRemoveTargetsRequest,
    EventBridgeRemoveTargetsResponse,
    EventBridgeStartReplayRequest,
    EventBridgeStartReplayResponse,
    EventBridgeTagResourceRequest,
    EventBridgeTagResourceResponse,
    EventBridgeTestEventPatternRequest,
    EventBridgeTestEventPatternResponse,
    EventBridgeUntagResourceRequest,
    EventBridgeUntagResourceResponse,
    EventBridgeUpdateApiDestinationRequest,
    EventBridgeUpdateApiDestinationResponse,
    EventBridgeUpdateArchiveRequest,
    EventBridgeUpdateArchiveResponse,
    EventBridgeUpdateConnectionRequest,
    EventBridgeUpdateConnectionResponse,
    EventBridgeUpdateEndpointRequest,
    EventBridgeUpdateEndpointResponse,
    EventBridgeUpdateEventBusRequest,
    EventBridgeUpdateEventBusResponse,
)
from werkflow_aws.types.cloudwatch_events_client import EventBridgeClient
from .base import AWSBaseService


class AWSEventBridge(AWSBaseService[EventBridgeClient]):
    service_name = 'cloudwatch-events'
    boto3_service_name = 'events'

    def __init__(self) -> None:
        super().__init__(service_name='cloudwatch-events', boto3_service_name='events')

    async def activate_event_source(
        self,
        request: EventBridgeActivateEventSourceRequest,
    ) -> EventBridgeActivateEventSourceResponse:
        client = self._require_client()
        return await self._execute(client.activate_event_source, request, EventBridgeActivateEventSourceResponse)

    async def cancel_replay(
        self,
        request: EventBridgeCancelReplayRequest,
    ) -> EventBridgeCancelReplayResponse:
        client = self._require_client()
        return await self._execute(client.cancel_replay, request, EventBridgeCancelReplayResponse)

    async def create_api_destination(
        self,
        request: EventBridgeCreateApiDestinationRequest,
    ) -> EventBridgeCreateApiDestinationResponse:
        client = self._require_client()
        return await self._execute(client.create_api_destination, request, EventBridgeCreateApiDestinationResponse)

    async def create_archive(
        self,
        request: EventBridgeCreateArchiveRequest,
    ) -> EventBridgeCreateArchiveResponse:
        client = self._require_client()
        return await self._execute(client.create_archive, request, EventBridgeCreateArchiveResponse)

    async def create_connection(
        self,
        request: EventBridgeCreateConnectionRequest,
    ) -> EventBridgeCreateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_connection, request, EventBridgeCreateConnectionResponse)

    async def create_endpoint(
        self,
        request: EventBridgeCreateEndpointRequest,
    ) -> EventBridgeCreateEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_endpoint, request, EventBridgeCreateEndpointResponse)

    async def create_event_bus(
        self,
        request: EventBridgeCreateEventBusRequest,
    ) -> EventBridgeCreateEventBusResponse:
        client = self._require_client()
        return await self._execute(client.create_event_bus, request, EventBridgeCreateEventBusResponse)

    async def create_partner_event_source(
        self,
        request: EventBridgeCreatePartnerEventSourceRequest,
    ) -> EventBridgeCreatePartnerEventSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_partner_event_source, request, EventBridgeCreatePartnerEventSourceResponse)

    async def deactivate_event_source(
        self,
        request: EventBridgeDeactivateEventSourceRequest,
    ) -> EventBridgeDeactivateEventSourceResponse:
        client = self._require_client()
        return await self._execute(client.deactivate_event_source, request, EventBridgeDeactivateEventSourceResponse)

    async def deauthorize_connection(
        self,
        request: EventBridgeDeauthorizeConnectionRequest,
    ) -> EventBridgeDeauthorizeConnectionResponse:
        client = self._require_client()
        return await self._execute(client.deauthorize_connection, request, EventBridgeDeauthorizeConnectionResponse)

    async def delete_api_destination(
        self,
        request: EventBridgeDeleteApiDestinationRequest,
    ) -> EventBridgeDeleteApiDestinationResponse:
        client = self._require_client()
        return await self._execute(client.delete_api_destination, request, EventBridgeDeleteApiDestinationResponse)

    async def delete_archive(
        self,
        request: EventBridgeDeleteArchiveRequest,
    ) -> EventBridgeDeleteArchiveResponse:
        client = self._require_client()
        return await self._execute(client.delete_archive, request, EventBridgeDeleteArchiveResponse)

    async def delete_connection(
        self,
        request: EventBridgeDeleteConnectionRequest,
    ) -> EventBridgeDeleteConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection, request, EventBridgeDeleteConnectionResponse)

    async def delete_endpoint(
        self,
        request: EventBridgeDeleteEndpointRequest,
    ) -> EventBridgeDeleteEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_endpoint, request, EventBridgeDeleteEndpointResponse)

    async def delete_event_bus(
        self,
        request: EventBridgeDeleteEventBusRequest,
    ) -> EventBridgeDeleteEventBusResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_bus, request, EventBridgeDeleteEventBusResponse)

    async def delete_partner_event_source(
        self,
        request: EventBridgeDeletePartnerEventSourceRequest,
    ) -> EventBridgeDeletePartnerEventSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_partner_event_source, request, EventBridgeDeletePartnerEventSourceResponse)

    async def delete_rule(
        self,
        request: EventBridgeDeleteRuleRequest,
    ) -> EventBridgeDeleteRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_rule, request, EventBridgeDeleteRuleResponse)

    async def describe_api_destination(
        self,
        request: EventBridgeDescribeApiDestinationRequest,
    ) -> EventBridgeDescribeApiDestinationResponse:
        client = self._require_client()
        return await self._execute(client.describe_api_destination, request, EventBridgeDescribeApiDestinationResponse)

    async def describe_archive(
        self,
        request: EventBridgeDescribeArchiveRequest,
    ) -> EventBridgeDescribeArchiveResponse:
        client = self._require_client()
        return await self._execute(client.describe_archive, request, EventBridgeDescribeArchiveResponse)

    async def describe_connection(
        self,
        request: EventBridgeDescribeConnectionRequest,
    ) -> EventBridgeDescribeConnectionResponse:
        client = self._require_client()
        return await self._execute(client.describe_connection, request, EventBridgeDescribeConnectionResponse)

    async def describe_endpoint(
        self,
        request: EventBridgeDescribeEndpointRequest,
    ) -> EventBridgeDescribeEndpointResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoint, request, EventBridgeDescribeEndpointResponse)

    async def describe_event_bus(
        self,
        request: EventBridgeDescribeEventBusRequest | None = None,
    ) -> EventBridgeDescribeEventBusResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_bus, request, EventBridgeDescribeEventBusResponse)

    async def describe_event_source(
        self,
        request: EventBridgeDescribeEventSourceRequest,
    ) -> EventBridgeDescribeEventSourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_source, request, EventBridgeDescribeEventSourceResponse)

    async def describe_partner_event_source(
        self,
        request: EventBridgeDescribePartnerEventSourceRequest,
    ) -> EventBridgeDescribePartnerEventSourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_partner_event_source, request, EventBridgeDescribePartnerEventSourceResponse)

    async def describe_replay(
        self,
        request: EventBridgeDescribeReplayRequest,
    ) -> EventBridgeDescribeReplayResponse:
        client = self._require_client()
        return await self._execute(client.describe_replay, request, EventBridgeDescribeReplayResponse)

    async def describe_rule(
        self,
        request: EventBridgeDescribeRuleRequest,
    ) -> EventBridgeDescribeRuleResponse:
        client = self._require_client()
        return await self._execute(client.describe_rule, request, EventBridgeDescribeRuleResponse)

    async def disable_rule(
        self,
        request: EventBridgeDisableRuleRequest,
    ) -> EventBridgeDisableRuleResponse:
        client = self._require_client()
        return await self._execute(client.disable_rule, request, EventBridgeDisableRuleResponse)

    async def enable_rule(
        self,
        request: EventBridgeEnableRuleRequest,
    ) -> EventBridgeEnableRuleResponse:
        client = self._require_client()
        return await self._execute(client.enable_rule, request, EventBridgeEnableRuleResponse)

    async def list_api_destinations(
        self,
        request: EventBridgeListApiDestinationsRequest | None = None,
    ) -> EventBridgeListApiDestinationsResponse:
        client = self._require_client()
        return await self._execute(client.list_api_destinations, request, EventBridgeListApiDestinationsResponse)

    async def list_archives(
        self,
        request: EventBridgeListArchivesRequest | None = None,
    ) -> EventBridgeListArchivesResponse:
        client = self._require_client()
        return await self._execute(client.list_archives, request, EventBridgeListArchivesResponse)

    async def list_connections(
        self,
        request: EventBridgeListConnectionsRequest | None = None,
    ) -> EventBridgeListConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_connections, request, EventBridgeListConnectionsResponse)

    async def list_endpoints(
        self,
        request: EventBridgeListEndpointsRequest | None = None,
    ) -> EventBridgeListEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.list_endpoints, request, EventBridgeListEndpointsResponse)

    async def list_event_buses(
        self,
        request: EventBridgeListEventBusesRequest | None = None,
    ) -> EventBridgeListEventBusesResponse:
        client = self._require_client()
        return await self._execute(client.list_event_buses, request, EventBridgeListEventBusesResponse)

    async def list_event_sources(
        self,
        request: EventBridgeListEventSourcesRequest | None = None,
    ) -> EventBridgeListEventSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_event_sources, request, EventBridgeListEventSourcesResponse)

    async def list_partner_event_source_accounts(
        self,
        request: EventBridgeListPartnerEventSourceAccountsRequest,
    ) -> EventBridgeListPartnerEventSourceAccountsResponse:
        client = self._require_client()
        return await self._execute(client.list_partner_event_source_accounts, request, EventBridgeListPartnerEventSourceAccountsResponse)

    async def list_partner_event_sources(
        self,
        request: EventBridgeListPartnerEventSourcesRequest,
    ) -> EventBridgeListPartnerEventSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_partner_event_sources, request, EventBridgeListPartnerEventSourcesResponse)

    async def list_replays(
        self,
        request: EventBridgeListReplaysRequest | None = None,
    ) -> EventBridgeListReplaysResponse:
        client = self._require_client()
        return await self._execute(client.list_replays, request, EventBridgeListReplaysResponse)

    async def list_rule_names_by_target(
        self,
        request: EventBridgeListRuleNamesByTargetRequest,
    ) -> EventBridgeListRuleNamesByTargetResponse:
        client = self._require_client()
        return await self._execute(client.list_rule_names_by_target, request, EventBridgeListRuleNamesByTargetResponse)

    async def list_rule_names_by_target_paginated(
        self,
        request: EventBridgeListRuleNamesByTargetRequest,
    ) -> list[EventBridgeListRuleNamesByTargetResponse]:
        return await self._paginate('list_rule_names_by_target', request, EventBridgeListRuleNamesByTargetResponse)

    async def list_rules(
        self,
        request: EventBridgeListRulesRequest | None = None,
    ) -> EventBridgeListRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_rules, request, EventBridgeListRulesResponse)

    async def list_rules_paginated(
        self,
        request: EventBridgeListRulesRequest | None = None,
    ) -> list[EventBridgeListRulesResponse]:
        return await self._paginate('list_rules', request, EventBridgeListRulesResponse)

    async def list_tags_for_resource(
        self,
        request: EventBridgeListTagsForResourceRequest,
    ) -> EventBridgeListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, EventBridgeListTagsForResourceResponse)

    async def list_targets_by_rule(
        self,
        request: EventBridgeListTargetsByRuleRequest,
    ) -> EventBridgeListTargetsByRuleResponse:
        client = self._require_client()
        return await self._execute(client.list_targets_by_rule, request, EventBridgeListTargetsByRuleResponse)

    async def list_targets_by_rule_paginated(
        self,
        request: EventBridgeListTargetsByRuleRequest,
    ) -> list[EventBridgeListTargetsByRuleResponse]:
        return await self._paginate('list_targets_by_rule', request, EventBridgeListTargetsByRuleResponse)

    async def put_events(
        self,
        request: EventBridgePutEventsRequest,
    ) -> EventBridgePutEventsResponse:
        client = self._require_client()
        return await self._execute(client.put_events, request, EventBridgePutEventsResponse)

    async def put_partner_events(
        self,
        request: EventBridgePutPartnerEventsRequest,
    ) -> EventBridgePutPartnerEventsResponse:
        client = self._require_client()
        return await self._execute(client.put_partner_events, request, EventBridgePutPartnerEventsResponse)

    async def put_permission(
        self,
        request: EventBridgePutPermissionRequest | None = None,
    ) -> EventBridgePutPermissionResponse:
        client = self._require_client()
        return await self._execute(client.put_permission, request, EventBridgePutPermissionResponse)

    async def put_rule(
        self,
        request: EventBridgePutRuleRequest,
    ) -> EventBridgePutRuleResponse:
        client = self._require_client()
        return await self._execute(client.put_rule, request, EventBridgePutRuleResponse)

    async def put_targets(
        self,
        request: EventBridgePutTargetsRequest,
    ) -> EventBridgePutTargetsResponse:
        client = self._require_client()
        return await self._execute(client.put_targets, request, EventBridgePutTargetsResponse)

    async def remove_permission(
        self,
        request: EventBridgeRemovePermissionRequest | None = None,
    ) -> EventBridgeRemovePermissionResponse:
        client = self._require_client()
        return await self._execute(client.remove_permission, request, EventBridgeRemovePermissionResponse)

    async def remove_targets(
        self,
        request: EventBridgeRemoveTargetsRequest,
    ) -> EventBridgeRemoveTargetsResponse:
        client = self._require_client()
        return await self._execute(client.remove_targets, request, EventBridgeRemoveTargetsResponse)

    async def start_replay(
        self,
        request: EventBridgeStartReplayRequest,
    ) -> EventBridgeStartReplayResponse:
        client = self._require_client()
        return await self._execute(client.start_replay, request, EventBridgeStartReplayResponse)

    async def tag_resource(
        self,
        request: EventBridgeTagResourceRequest,
    ) -> EventBridgeTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, EventBridgeTagResourceResponse)

    async def test_event_pattern(
        self,
        request: EventBridgeTestEventPatternRequest,
    ) -> EventBridgeTestEventPatternResponse:
        client = self._require_client()
        return await self._execute(client.test_event_pattern, request, EventBridgeTestEventPatternResponse)

    async def untag_resource(
        self,
        request: EventBridgeUntagResourceRequest,
    ) -> EventBridgeUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, EventBridgeUntagResourceResponse)

    async def update_api_destination(
        self,
        request: EventBridgeUpdateApiDestinationRequest,
    ) -> EventBridgeUpdateApiDestinationResponse:
        client = self._require_client()
        return await self._execute(client.update_api_destination, request, EventBridgeUpdateApiDestinationResponse)

    async def update_archive(
        self,
        request: EventBridgeUpdateArchiveRequest,
    ) -> EventBridgeUpdateArchiveResponse:
        client = self._require_client()
        return await self._execute(client.update_archive, request, EventBridgeUpdateArchiveResponse)

    async def update_connection(
        self,
        request: EventBridgeUpdateConnectionRequest,
    ) -> EventBridgeUpdateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.update_connection, request, EventBridgeUpdateConnectionResponse)

    async def update_endpoint(
        self,
        request: EventBridgeUpdateEndpointRequest,
    ) -> EventBridgeUpdateEndpointResponse:
        client = self._require_client()
        return await self._execute(client.update_endpoint, request, EventBridgeUpdateEndpointResponse)

    async def update_event_bus(
        self,
        request: EventBridgeUpdateEventBusRequest | None = None,
    ) -> EventBridgeUpdateEventBusResponse:
        client = self._require_client()
        return await self._execute(client.update_event_bus, request, EventBridgeUpdateEventBusResponse)
