from werkflow_aws.models.neptune import (
    NeptuneAddRoleToDBClusterRequest,
    NeptuneAddRoleToDBClusterResponse,
    NeptuneAddSourceIdentifierToSubscriptionRequest,
    NeptuneAddSourceIdentifierToSubscriptionResponse,
    NeptuneAddTagsToResourceRequest,
    NeptuneAddTagsToResourceResponse,
    NeptuneApplyPendingMaintenanceActionRequest,
    NeptuneApplyPendingMaintenanceActionResponse,
    NeptuneCopyDBClusterParameterGroupRequest,
    NeptuneCopyDBClusterParameterGroupResponse,
    NeptuneCopyDBClusterSnapshotRequest,
    NeptuneCopyDBClusterSnapshotResponse,
    NeptuneCopyDBParameterGroupRequest,
    NeptuneCopyDBParameterGroupResponse,
    NeptuneCreateDBClusterEndpointRequest,
    NeptuneCreateDBClusterEndpointResponse,
    NeptuneCreateDBClusterParameterGroupRequest,
    NeptuneCreateDBClusterParameterGroupResponse,
    NeptuneCreateDBClusterRequest,
    NeptuneCreateDBClusterResponse,
    NeptuneCreateDBClusterSnapshotRequest,
    NeptuneCreateDBClusterSnapshotResponse,
    NeptuneCreateDBInstanceRequest,
    NeptuneCreateDBInstanceResponse,
    NeptuneCreateDBParameterGroupRequest,
    NeptuneCreateDBParameterGroupResponse,
    NeptuneCreateDBSubnetGroupRequest,
    NeptuneCreateDBSubnetGroupResponse,
    NeptuneCreateEventSubscriptionRequest,
    NeptuneCreateEventSubscriptionResponse,
    NeptuneCreateGlobalClusterRequest,
    NeptuneCreateGlobalClusterResponse,
    NeptuneDeleteDBClusterEndpointRequest,
    NeptuneDeleteDBClusterEndpointResponse,
    NeptuneDeleteDBClusterParameterGroupRequest,
    NeptuneDeleteDBClusterParameterGroupResponse,
    NeptuneDeleteDBClusterRequest,
    NeptuneDeleteDBClusterResponse,
    NeptuneDeleteDBClusterSnapshotRequest,
    NeptuneDeleteDBClusterSnapshotResponse,
    NeptuneDeleteDBInstanceRequest,
    NeptuneDeleteDBInstanceResponse,
    NeptuneDeleteDBParameterGroupRequest,
    NeptuneDeleteDBParameterGroupResponse,
    NeptuneDeleteDBSubnetGroupRequest,
    NeptuneDeleteDBSubnetGroupResponse,
    NeptuneDeleteEventSubscriptionRequest,
    NeptuneDeleteEventSubscriptionResponse,
    NeptuneDeleteGlobalClusterRequest,
    NeptuneDeleteGlobalClusterResponse,
    NeptuneDescribeDBClusterEndpointsRequest,
    NeptuneDescribeDBClusterEndpointsResponse,
    NeptuneDescribeDBClusterParameterGroupsRequest,
    NeptuneDescribeDBClusterParameterGroupsResponse,
    NeptuneDescribeDBClusterParametersRequest,
    NeptuneDescribeDBClusterParametersResponse,
    NeptuneDescribeDBClusterSnapshotAttributesRequest,
    NeptuneDescribeDBClusterSnapshotAttributesResponse,
    NeptuneDescribeDBClusterSnapshotsRequest,
    NeptuneDescribeDBClusterSnapshotsResponse,
    NeptuneDescribeDBClustersRequest,
    NeptuneDescribeDBClustersResponse,
    NeptuneDescribeDBEngineVersionsRequest,
    NeptuneDescribeDBEngineVersionsResponse,
    NeptuneDescribeDBInstancesRequest,
    NeptuneDescribeDBInstancesResponse,
    NeptuneDescribeDBParameterGroupsRequest,
    NeptuneDescribeDBParameterGroupsResponse,
    NeptuneDescribeDBParametersRequest,
    NeptuneDescribeDBParametersResponse,
    NeptuneDescribeDBSubnetGroupsRequest,
    NeptuneDescribeDBSubnetGroupsResponse,
    NeptuneDescribeEngineDefaultClusterParametersRequest,
    NeptuneDescribeEngineDefaultClusterParametersResponse,
    NeptuneDescribeEngineDefaultParametersRequest,
    NeptuneDescribeEngineDefaultParametersResponse,
    NeptuneDescribeEventCategoriesRequest,
    NeptuneDescribeEventCategoriesResponse,
    NeptuneDescribeEventSubscriptionsRequest,
    NeptuneDescribeEventSubscriptionsResponse,
    NeptuneDescribeEventsRequest,
    NeptuneDescribeEventsResponse,
    NeptuneDescribeGlobalClustersRequest,
    NeptuneDescribeGlobalClustersResponse,
    NeptuneDescribeOrderableDBInstanceOptionsRequest,
    NeptuneDescribeOrderableDBInstanceOptionsResponse,
    NeptuneDescribePendingMaintenanceActionsRequest,
    NeptuneDescribePendingMaintenanceActionsResponse,
    NeptuneDescribeServerlessV2PlatformVersionsRequest,
    NeptuneDescribeServerlessV2PlatformVersionsResponse,
    NeptuneDescribeValidDBInstanceModificationsRequest,
    NeptuneDescribeValidDBInstanceModificationsResponse,
    NeptuneFailoverDBClusterRequest,
    NeptuneFailoverDBClusterResponse,
    NeptuneFailoverGlobalClusterRequest,
    NeptuneFailoverGlobalClusterResponse,
    NeptuneListTagsForResourceRequest,
    NeptuneListTagsForResourceResponse,
    NeptuneModifyDBClusterEndpointRequest,
    NeptuneModifyDBClusterEndpointResponse,
    NeptuneModifyDBClusterParameterGroupRequest,
    NeptuneModifyDBClusterParameterGroupResponse,
    NeptuneModifyDBClusterRequest,
    NeptuneModifyDBClusterResponse,
    NeptuneModifyDBClusterSnapshotAttributeRequest,
    NeptuneModifyDBClusterSnapshotAttributeResponse,
    NeptuneModifyDBInstanceRequest,
    NeptuneModifyDBInstanceResponse,
    NeptuneModifyDBParameterGroupRequest,
    NeptuneModifyDBParameterGroupResponse,
    NeptuneModifyDBSubnetGroupRequest,
    NeptuneModifyDBSubnetGroupResponse,
    NeptuneModifyEventSubscriptionRequest,
    NeptuneModifyEventSubscriptionResponse,
    NeptuneModifyGlobalClusterRequest,
    NeptuneModifyGlobalClusterResponse,
    NeptunePromoteReadReplicaDBClusterRequest,
    NeptunePromoteReadReplicaDBClusterResponse,
    NeptuneRebootDBInstanceRequest,
    NeptuneRebootDBInstanceResponse,
    NeptuneRemoveFromGlobalClusterRequest,
    NeptuneRemoveFromGlobalClusterResponse,
    NeptuneRemoveRoleFromDBClusterRequest,
    NeptuneRemoveRoleFromDBClusterResponse,
    NeptuneRemoveSourceIdentifierFromSubscriptionRequest,
    NeptuneRemoveSourceIdentifierFromSubscriptionResponse,
    NeptuneRemoveTagsFromResourceRequest,
    NeptuneRemoveTagsFromResourceResponse,
    NeptuneResetDBClusterParameterGroupRequest,
    NeptuneResetDBClusterParameterGroupResponse,
    NeptuneResetDBParameterGroupRequest,
    NeptuneResetDBParameterGroupResponse,
    NeptuneRestoreDBClusterFromSnapshotRequest,
    NeptuneRestoreDBClusterFromSnapshotResponse,
    NeptuneRestoreDBClusterToPointInTimeRequest,
    NeptuneRestoreDBClusterToPointInTimeResponse,
    NeptuneStartDBClusterRequest,
    NeptuneStartDBClusterResponse,
    NeptuneStopDBClusterRequest,
    NeptuneStopDBClusterResponse,
    NeptuneSwitchoverGlobalClusterRequest,
    NeptuneSwitchoverGlobalClusterResponse,
)
from werkflow_aws.types.neptune_client import NeptuneClient
from .base import AWSBaseService


class AWSNeptune(AWSBaseService[NeptuneClient]):
    service_name = 'neptune'
    boto3_service_name = 'neptune'

    def __init__(self) -> None:
        super().__init__(service_name='neptune', boto3_service_name='neptune')

    async def add_role_to_db_cluster(
        self,
        request: NeptuneAddRoleToDBClusterRequest,
    ) -> NeptuneAddRoleToDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.add_role_to_db_cluster, request, NeptuneAddRoleToDBClusterResponse)

    async def add_source_identifier_to_subscription(
        self,
        request: NeptuneAddSourceIdentifierToSubscriptionRequest,
    ) -> NeptuneAddSourceIdentifierToSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.add_source_identifier_to_subscription, request, NeptuneAddSourceIdentifierToSubscriptionResponse)

    async def add_tags_to_resource(
        self,
        request: NeptuneAddTagsToResourceRequest,
    ) -> NeptuneAddTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_resource, request, NeptuneAddTagsToResourceResponse)

    async def apply_pending_maintenance_action(
        self,
        request: NeptuneApplyPendingMaintenanceActionRequest,
    ) -> NeptuneApplyPendingMaintenanceActionResponse:
        client = self._require_client()
        return await self._execute(client.apply_pending_maintenance_action, request, NeptuneApplyPendingMaintenanceActionResponse)

    async def copy_db_cluster_parameter_group(
        self,
        request: NeptuneCopyDBClusterParameterGroupRequest,
    ) -> NeptuneCopyDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_cluster_parameter_group, request, NeptuneCopyDBClusterParameterGroupResponse)

    async def copy_db_cluster_snapshot(
        self,
        request: NeptuneCopyDBClusterSnapshotRequest,
    ) -> NeptuneCopyDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_cluster_snapshot, request, NeptuneCopyDBClusterSnapshotResponse)

    async def copy_db_parameter_group(
        self,
        request: NeptuneCopyDBParameterGroupRequest,
    ) -> NeptuneCopyDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_parameter_group, request, NeptuneCopyDBParameterGroupResponse)

    async def create_db_cluster(
        self,
        request: NeptuneCreateDBClusterRequest,
    ) -> NeptuneCreateDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster, request, NeptuneCreateDBClusterResponse)

    async def create_db_cluster_endpoint(
        self,
        request: NeptuneCreateDBClusterEndpointRequest,
    ) -> NeptuneCreateDBClusterEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster_endpoint, request, NeptuneCreateDBClusterEndpointResponse)

    async def create_db_cluster_parameter_group(
        self,
        request: NeptuneCreateDBClusterParameterGroupRequest,
    ) -> NeptuneCreateDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster_parameter_group, request, NeptuneCreateDBClusterParameterGroupResponse)

    async def create_db_cluster_snapshot(
        self,
        request: NeptuneCreateDBClusterSnapshotRequest,
    ) -> NeptuneCreateDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster_snapshot, request, NeptuneCreateDBClusterSnapshotResponse)

    async def create_db_instance(
        self,
        request: NeptuneCreateDBInstanceRequest,
    ) -> NeptuneCreateDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.create_db_instance, request, NeptuneCreateDBInstanceResponse)

    async def create_db_parameter_group(
        self,
        request: NeptuneCreateDBParameterGroupRequest,
    ) -> NeptuneCreateDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_parameter_group, request, NeptuneCreateDBParameterGroupResponse)

    async def create_db_subnet_group(
        self,
        request: NeptuneCreateDBSubnetGroupRequest,
    ) -> NeptuneCreateDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_subnet_group, request, NeptuneCreateDBSubnetGroupResponse)

    async def create_event_subscription(
        self,
        request: NeptuneCreateEventSubscriptionRequest,
    ) -> NeptuneCreateEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_event_subscription, request, NeptuneCreateEventSubscriptionResponse)

    async def create_global_cluster(
        self,
        request: NeptuneCreateGlobalClusterRequest,
    ) -> NeptuneCreateGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_global_cluster, request, NeptuneCreateGlobalClusterResponse)

    async def delete_db_cluster(
        self,
        request: NeptuneDeleteDBClusterRequest,
    ) -> NeptuneDeleteDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster, request, NeptuneDeleteDBClusterResponse)

    async def delete_db_cluster_endpoint(
        self,
        request: NeptuneDeleteDBClusterEndpointRequest,
    ) -> NeptuneDeleteDBClusterEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster_endpoint, request, NeptuneDeleteDBClusterEndpointResponse)

    async def delete_db_cluster_parameter_group(
        self,
        request: NeptuneDeleteDBClusterParameterGroupRequest,
    ) -> NeptuneDeleteDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster_parameter_group, request, NeptuneDeleteDBClusterParameterGroupResponse)

    async def delete_db_cluster_snapshot(
        self,
        request: NeptuneDeleteDBClusterSnapshotRequest,
    ) -> NeptuneDeleteDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster_snapshot, request, NeptuneDeleteDBClusterSnapshotResponse)

    async def delete_db_instance(
        self,
        request: NeptuneDeleteDBInstanceRequest,
    ) -> NeptuneDeleteDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_instance, request, NeptuneDeleteDBInstanceResponse)

    async def delete_db_parameter_group(
        self,
        request: NeptuneDeleteDBParameterGroupRequest,
    ) -> NeptuneDeleteDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_parameter_group, request, NeptuneDeleteDBParameterGroupResponse)

    async def delete_db_subnet_group(
        self,
        request: NeptuneDeleteDBSubnetGroupRequest,
    ) -> NeptuneDeleteDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_subnet_group, request, NeptuneDeleteDBSubnetGroupResponse)

    async def delete_event_subscription(
        self,
        request: NeptuneDeleteEventSubscriptionRequest,
    ) -> NeptuneDeleteEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_subscription, request, NeptuneDeleteEventSubscriptionResponse)

    async def delete_global_cluster(
        self,
        request: NeptuneDeleteGlobalClusterRequest,
    ) -> NeptuneDeleteGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_global_cluster, request, NeptuneDeleteGlobalClusterResponse)

    async def describe_db_cluster_endpoints(
        self,
        request: NeptuneDescribeDBClusterEndpointsRequest | None = None,
    ) -> NeptuneDescribeDBClusterEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_endpoints, request, NeptuneDescribeDBClusterEndpointsResponse)

    async def describe_db_cluster_endpoints_paginated(
        self,
        request: NeptuneDescribeDBClusterEndpointsRequest | None = None,
    ) -> list[NeptuneDescribeDBClusterEndpointsResponse]:
        return await self._paginate('describe_db_cluster_endpoints', request, NeptuneDescribeDBClusterEndpointsResponse)

    async def describe_db_cluster_parameter_groups(
        self,
        request: NeptuneDescribeDBClusterParameterGroupsRequest | None = None,
    ) -> NeptuneDescribeDBClusterParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_parameter_groups, request, NeptuneDescribeDBClusterParameterGroupsResponse)

    async def describe_db_cluster_parameter_groups_paginated(
        self,
        request: NeptuneDescribeDBClusterParameterGroupsRequest | None = None,
    ) -> list[NeptuneDescribeDBClusterParameterGroupsResponse]:
        return await self._paginate('describe_db_cluster_parameter_groups', request, NeptuneDescribeDBClusterParameterGroupsResponse)

    async def describe_db_cluster_parameters(
        self,
        request: NeptuneDescribeDBClusterParametersRequest,
    ) -> NeptuneDescribeDBClusterParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_parameters, request, NeptuneDescribeDBClusterParametersResponse)

    async def describe_db_cluster_parameters_paginated(
        self,
        request: NeptuneDescribeDBClusterParametersRequest,
    ) -> list[NeptuneDescribeDBClusterParametersResponse]:
        return await self._paginate('describe_db_cluster_parameters', request, NeptuneDescribeDBClusterParametersResponse)

    async def describe_db_cluster_snapshot_attributes(
        self,
        request: NeptuneDescribeDBClusterSnapshotAttributesRequest,
    ) -> NeptuneDescribeDBClusterSnapshotAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_snapshot_attributes, request, NeptuneDescribeDBClusterSnapshotAttributesResponse)

    async def describe_db_cluster_snapshots(
        self,
        request: NeptuneDescribeDBClusterSnapshotsRequest | None = None,
    ) -> NeptuneDescribeDBClusterSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_snapshots, request, NeptuneDescribeDBClusterSnapshotsResponse)

    async def describe_db_cluster_snapshots_paginated(
        self,
        request: NeptuneDescribeDBClusterSnapshotsRequest | None = None,
    ) -> list[NeptuneDescribeDBClusterSnapshotsResponse]:
        return await self._paginate('describe_db_cluster_snapshots', request, NeptuneDescribeDBClusterSnapshotsResponse)

    async def describe_db_clusters(
        self,
        request: NeptuneDescribeDBClustersRequest | None = None,
    ) -> NeptuneDescribeDBClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_clusters, request, NeptuneDescribeDBClustersResponse)

    async def describe_db_clusters_paginated(
        self,
        request: NeptuneDescribeDBClustersRequest | None = None,
    ) -> list[NeptuneDescribeDBClustersResponse]:
        return await self._paginate('describe_db_clusters', request, NeptuneDescribeDBClustersResponse)

    async def describe_db_engine_versions(
        self,
        request: NeptuneDescribeDBEngineVersionsRequest | None = None,
    ) -> NeptuneDescribeDBEngineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_engine_versions, request, NeptuneDescribeDBEngineVersionsResponse)

    async def describe_db_engine_versions_paginated(
        self,
        request: NeptuneDescribeDBEngineVersionsRequest | None = None,
    ) -> list[NeptuneDescribeDBEngineVersionsResponse]:
        return await self._paginate('describe_db_engine_versions', request, NeptuneDescribeDBEngineVersionsResponse)

    async def describe_db_instances(
        self,
        request: NeptuneDescribeDBInstancesRequest | None = None,
    ) -> NeptuneDescribeDBInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_instances, request, NeptuneDescribeDBInstancesResponse)

    async def describe_db_instances_paginated(
        self,
        request: NeptuneDescribeDBInstancesRequest | None = None,
    ) -> list[NeptuneDescribeDBInstancesResponse]:
        return await self._paginate('describe_db_instances', request, NeptuneDescribeDBInstancesResponse)

    async def describe_db_parameter_groups(
        self,
        request: NeptuneDescribeDBParameterGroupsRequest | None = None,
    ) -> NeptuneDescribeDBParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_parameter_groups, request, NeptuneDescribeDBParameterGroupsResponse)

    async def describe_db_parameter_groups_paginated(
        self,
        request: NeptuneDescribeDBParameterGroupsRequest | None = None,
    ) -> list[NeptuneDescribeDBParameterGroupsResponse]:
        return await self._paginate('describe_db_parameter_groups', request, NeptuneDescribeDBParameterGroupsResponse)

    async def describe_db_parameters(
        self,
        request: NeptuneDescribeDBParametersRequest,
    ) -> NeptuneDescribeDBParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_parameters, request, NeptuneDescribeDBParametersResponse)

    async def describe_db_parameters_paginated(
        self,
        request: NeptuneDescribeDBParametersRequest,
    ) -> list[NeptuneDescribeDBParametersResponse]:
        return await self._paginate('describe_db_parameters', request, NeptuneDescribeDBParametersResponse)

    async def describe_db_subnet_groups(
        self,
        request: NeptuneDescribeDBSubnetGroupsRequest | None = None,
    ) -> NeptuneDescribeDBSubnetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_subnet_groups, request, NeptuneDescribeDBSubnetGroupsResponse)

    async def describe_db_subnet_groups_paginated(
        self,
        request: NeptuneDescribeDBSubnetGroupsRequest | None = None,
    ) -> list[NeptuneDescribeDBSubnetGroupsResponse]:
        return await self._paginate('describe_db_subnet_groups', request, NeptuneDescribeDBSubnetGroupsResponse)

    async def describe_engine_default_cluster_parameters(
        self,
        request: NeptuneDescribeEngineDefaultClusterParametersRequest,
    ) -> NeptuneDescribeEngineDefaultClusterParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_engine_default_cluster_parameters, request, NeptuneDescribeEngineDefaultClusterParametersResponse)

    async def describe_engine_default_parameters(
        self,
        request: NeptuneDescribeEngineDefaultParametersRequest,
    ) -> NeptuneDescribeEngineDefaultParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_engine_default_parameters, request, NeptuneDescribeEngineDefaultParametersResponse)

    async def describe_engine_default_parameters_paginated(
        self,
        request: NeptuneDescribeEngineDefaultParametersRequest,
    ) -> list[NeptuneDescribeEngineDefaultParametersResponse]:
        return await self._paginate('describe_engine_default_parameters', request, NeptuneDescribeEngineDefaultParametersResponse)

    async def describe_event_categories(
        self,
        request: NeptuneDescribeEventCategoriesRequest | None = None,
    ) -> NeptuneDescribeEventCategoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_categories, request, NeptuneDescribeEventCategoriesResponse)

    async def describe_event_subscriptions(
        self,
        request: NeptuneDescribeEventSubscriptionsRequest | None = None,
    ) -> NeptuneDescribeEventSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_subscriptions, request, NeptuneDescribeEventSubscriptionsResponse)

    async def describe_event_subscriptions_paginated(
        self,
        request: NeptuneDescribeEventSubscriptionsRequest | None = None,
    ) -> list[NeptuneDescribeEventSubscriptionsResponse]:
        return await self._paginate('describe_event_subscriptions', request, NeptuneDescribeEventSubscriptionsResponse)

    async def describe_events(
        self,
        request: NeptuneDescribeEventsRequest | None = None,
    ) -> NeptuneDescribeEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_events, request, NeptuneDescribeEventsResponse)

    async def describe_events_paginated(
        self,
        request: NeptuneDescribeEventsRequest | None = None,
    ) -> list[NeptuneDescribeEventsResponse]:
        return await self._paginate('describe_events', request, NeptuneDescribeEventsResponse)

    async def describe_global_clusters(
        self,
        request: NeptuneDescribeGlobalClustersRequest | None = None,
    ) -> NeptuneDescribeGlobalClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_clusters, request, NeptuneDescribeGlobalClustersResponse)

    async def describe_global_clusters_paginated(
        self,
        request: NeptuneDescribeGlobalClustersRequest | None = None,
    ) -> list[NeptuneDescribeGlobalClustersResponse]:
        return await self._paginate('describe_global_clusters', request, NeptuneDescribeGlobalClustersResponse)

    async def describe_orderable_db_instance_options(
        self,
        request: NeptuneDescribeOrderableDBInstanceOptionsRequest,
    ) -> NeptuneDescribeOrderableDBInstanceOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_orderable_db_instance_options, request, NeptuneDescribeOrderableDBInstanceOptionsResponse)

    async def describe_orderable_db_instance_options_paginated(
        self,
        request: NeptuneDescribeOrderableDBInstanceOptionsRequest,
    ) -> list[NeptuneDescribeOrderableDBInstanceOptionsResponse]:
        return await self._paginate('describe_orderable_db_instance_options', request, NeptuneDescribeOrderableDBInstanceOptionsResponse)

    async def describe_pending_maintenance_actions(
        self,
        request: NeptuneDescribePendingMaintenanceActionsRequest | None = None,
    ) -> NeptuneDescribePendingMaintenanceActionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_pending_maintenance_actions, request, NeptuneDescribePendingMaintenanceActionsResponse)

    async def describe_pending_maintenance_actions_paginated(
        self,
        request: NeptuneDescribePendingMaintenanceActionsRequest | None = None,
    ) -> list[NeptuneDescribePendingMaintenanceActionsResponse]:
        return await self._paginate('describe_pending_maintenance_actions', request, NeptuneDescribePendingMaintenanceActionsResponse)

    async def describe_serverless_v2_platform_versions(
        self,
        request: NeptuneDescribeServerlessV2PlatformVersionsRequest | None = None,
    ) -> NeptuneDescribeServerlessV2PlatformVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_serverless_v2_platform_versions, request, NeptuneDescribeServerlessV2PlatformVersionsResponse)

    async def describe_serverless_v2_platform_versions_paginated(
        self,
        request: NeptuneDescribeServerlessV2PlatformVersionsRequest | None = None,
    ) -> list[NeptuneDescribeServerlessV2PlatformVersionsResponse]:
        return await self._paginate('describe_serverless_v2_platform_versions', request, NeptuneDescribeServerlessV2PlatformVersionsResponse)

    async def describe_valid_db_instance_modifications(
        self,
        request: NeptuneDescribeValidDBInstanceModificationsRequest,
    ) -> NeptuneDescribeValidDBInstanceModificationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_valid_db_instance_modifications, request, NeptuneDescribeValidDBInstanceModificationsResponse)

    async def failover_db_cluster(
        self,
        request: NeptuneFailoverDBClusterRequest | None = None,
    ) -> NeptuneFailoverDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.failover_db_cluster, request, NeptuneFailoverDBClusterResponse)

    async def failover_global_cluster(
        self,
        request: NeptuneFailoverGlobalClusterRequest,
    ) -> NeptuneFailoverGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.failover_global_cluster, request, NeptuneFailoverGlobalClusterResponse)

    async def list_tags_for_resource(
        self,
        request: NeptuneListTagsForResourceRequest,
    ) -> NeptuneListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, NeptuneListTagsForResourceResponse)

    async def modify_db_cluster(
        self,
        request: NeptuneModifyDBClusterRequest,
    ) -> NeptuneModifyDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster, request, NeptuneModifyDBClusterResponse)

    async def modify_db_cluster_endpoint(
        self,
        request: NeptuneModifyDBClusterEndpointRequest,
    ) -> NeptuneModifyDBClusterEndpointResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster_endpoint, request, NeptuneModifyDBClusterEndpointResponse)

    async def modify_db_cluster_parameter_group(
        self,
        request: NeptuneModifyDBClusterParameterGroupRequest,
    ) -> NeptuneModifyDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster_parameter_group, request, NeptuneModifyDBClusterParameterGroupResponse)

    async def modify_db_cluster_snapshot_attribute(
        self,
        request: NeptuneModifyDBClusterSnapshotAttributeRequest,
    ) -> NeptuneModifyDBClusterSnapshotAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster_snapshot_attribute, request, NeptuneModifyDBClusterSnapshotAttributeResponse)

    async def modify_db_instance(
        self,
        request: NeptuneModifyDBInstanceRequest,
    ) -> NeptuneModifyDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_instance, request, NeptuneModifyDBInstanceResponse)

    async def modify_db_parameter_group(
        self,
        request: NeptuneModifyDBParameterGroupRequest,
    ) -> NeptuneModifyDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_parameter_group, request, NeptuneModifyDBParameterGroupResponse)

    async def modify_db_subnet_group(
        self,
        request: NeptuneModifyDBSubnetGroupRequest,
    ) -> NeptuneModifyDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_subnet_group, request, NeptuneModifyDBSubnetGroupResponse)

    async def modify_event_subscription(
        self,
        request: NeptuneModifyEventSubscriptionRequest,
    ) -> NeptuneModifyEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.modify_event_subscription, request, NeptuneModifyEventSubscriptionResponse)

    async def modify_global_cluster(
        self,
        request: NeptuneModifyGlobalClusterRequest,
    ) -> NeptuneModifyGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.modify_global_cluster, request, NeptuneModifyGlobalClusterResponse)

    async def promote_read_replica_db_cluster(
        self,
        request: NeptunePromoteReadReplicaDBClusterRequest,
    ) -> NeptunePromoteReadReplicaDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.promote_read_replica_db_cluster, request, NeptunePromoteReadReplicaDBClusterResponse)

    async def reboot_db_instance(
        self,
        request: NeptuneRebootDBInstanceRequest,
    ) -> NeptuneRebootDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.reboot_db_instance, request, NeptuneRebootDBInstanceResponse)

    async def remove_from_global_cluster(
        self,
        request: NeptuneRemoveFromGlobalClusterRequest,
    ) -> NeptuneRemoveFromGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.remove_from_global_cluster, request, NeptuneRemoveFromGlobalClusterResponse)

    async def remove_role_from_db_cluster(
        self,
        request: NeptuneRemoveRoleFromDBClusterRequest,
    ) -> NeptuneRemoveRoleFromDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.remove_role_from_db_cluster, request, NeptuneRemoveRoleFromDBClusterResponse)

    async def remove_source_identifier_from_subscription(
        self,
        request: NeptuneRemoveSourceIdentifierFromSubscriptionRequest,
    ) -> NeptuneRemoveSourceIdentifierFromSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.remove_source_identifier_from_subscription, request, NeptuneRemoveSourceIdentifierFromSubscriptionResponse)

    async def remove_tags_from_resource(
        self,
        request: NeptuneRemoveTagsFromResourceRequest,
    ) -> NeptuneRemoveTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_resource, request, NeptuneRemoveTagsFromResourceResponse)

    async def reset_db_cluster_parameter_group(
        self,
        request: NeptuneResetDBClusterParameterGroupRequest,
    ) -> NeptuneResetDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.reset_db_cluster_parameter_group, request, NeptuneResetDBClusterParameterGroupResponse)

    async def reset_db_parameter_group(
        self,
        request: NeptuneResetDBParameterGroupRequest,
    ) -> NeptuneResetDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.reset_db_parameter_group, request, NeptuneResetDBParameterGroupResponse)

    async def restore_db_cluster_from_snapshot(
        self,
        request: NeptuneRestoreDBClusterFromSnapshotRequest,
    ) -> NeptuneRestoreDBClusterFromSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.restore_db_cluster_from_snapshot, request, NeptuneRestoreDBClusterFromSnapshotResponse)

    async def restore_db_cluster_to_point_in_time(
        self,
        request: NeptuneRestoreDBClusterToPointInTimeRequest,
    ) -> NeptuneRestoreDBClusterToPointInTimeResponse:
        client = self._require_client()
        return await self._execute(client.restore_db_cluster_to_point_in_time, request, NeptuneRestoreDBClusterToPointInTimeResponse)

    async def start_db_cluster(
        self,
        request: NeptuneStartDBClusterRequest,
    ) -> NeptuneStartDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.start_db_cluster, request, NeptuneStartDBClusterResponse)

    async def stop_db_cluster(
        self,
        request: NeptuneStopDBClusterRequest,
    ) -> NeptuneStopDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.stop_db_cluster, request, NeptuneStopDBClusterResponse)

    async def switchover_global_cluster(
        self,
        request: NeptuneSwitchoverGlobalClusterRequest,
    ) -> NeptuneSwitchoverGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.switchover_global_cluster, request, NeptuneSwitchoverGlobalClusterResponse)
