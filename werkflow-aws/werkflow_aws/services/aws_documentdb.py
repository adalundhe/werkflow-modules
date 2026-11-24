from werkflow_aws.models.documentdb import (
    DocumentDBAddSourceIdentifierToSubscriptionRequest,
    DocumentDBAddSourceIdentifierToSubscriptionResponse,
    DocumentDBAddTagsToResourceRequest,
    DocumentDBAddTagsToResourceResponse,
    DocumentDBApplyPendingMaintenanceActionRequest,
    DocumentDBApplyPendingMaintenanceActionResponse,
    DocumentDBCopyDBClusterParameterGroupRequest,
    DocumentDBCopyDBClusterParameterGroupResponse,
    DocumentDBCopyDBClusterSnapshotRequest,
    DocumentDBCopyDBClusterSnapshotResponse,
    DocumentDBCreateDBClusterParameterGroupRequest,
    DocumentDBCreateDBClusterParameterGroupResponse,
    DocumentDBCreateDBClusterRequest,
    DocumentDBCreateDBClusterResponse,
    DocumentDBCreateDBClusterSnapshotRequest,
    DocumentDBCreateDBClusterSnapshotResponse,
    DocumentDBCreateDBInstanceRequest,
    DocumentDBCreateDBInstanceResponse,
    DocumentDBCreateDBSubnetGroupRequest,
    DocumentDBCreateDBSubnetGroupResponse,
    DocumentDBCreateEventSubscriptionRequest,
    DocumentDBCreateEventSubscriptionResponse,
    DocumentDBCreateGlobalClusterRequest,
    DocumentDBCreateGlobalClusterResponse,
    DocumentDBDeleteDBClusterParameterGroupRequest,
    DocumentDBDeleteDBClusterParameterGroupResponse,
    DocumentDBDeleteDBClusterRequest,
    DocumentDBDeleteDBClusterResponse,
    DocumentDBDeleteDBClusterSnapshotRequest,
    DocumentDBDeleteDBClusterSnapshotResponse,
    DocumentDBDeleteDBInstanceRequest,
    DocumentDBDeleteDBInstanceResponse,
    DocumentDBDeleteDBSubnetGroupRequest,
    DocumentDBDeleteDBSubnetGroupResponse,
    DocumentDBDeleteEventSubscriptionRequest,
    DocumentDBDeleteEventSubscriptionResponse,
    DocumentDBDeleteGlobalClusterRequest,
    DocumentDBDeleteGlobalClusterResponse,
    DocumentDBDescribeCertificatesRequest,
    DocumentDBDescribeCertificatesResponse,
    DocumentDBDescribeDBClusterParameterGroupsRequest,
    DocumentDBDescribeDBClusterParameterGroupsResponse,
    DocumentDBDescribeDBClusterParametersRequest,
    DocumentDBDescribeDBClusterParametersResponse,
    DocumentDBDescribeDBClusterSnapshotAttributesRequest,
    DocumentDBDescribeDBClusterSnapshotAttributesResponse,
    DocumentDBDescribeDBClusterSnapshotsRequest,
    DocumentDBDescribeDBClusterSnapshotsResponse,
    DocumentDBDescribeDBClustersRequest,
    DocumentDBDescribeDBClustersResponse,
    DocumentDBDescribeDBEngineVersionsRequest,
    DocumentDBDescribeDBEngineVersionsResponse,
    DocumentDBDescribeDBInstancesRequest,
    DocumentDBDescribeDBInstancesResponse,
    DocumentDBDescribeDBSubnetGroupsRequest,
    DocumentDBDescribeDBSubnetGroupsResponse,
    DocumentDBDescribeEngineDefaultClusterParametersRequest,
    DocumentDBDescribeEngineDefaultClusterParametersResponse,
    DocumentDBDescribeEventCategoriesRequest,
    DocumentDBDescribeEventCategoriesResponse,
    DocumentDBDescribeEventSubscriptionsRequest,
    DocumentDBDescribeEventSubscriptionsResponse,
    DocumentDBDescribeEventsRequest,
    DocumentDBDescribeEventsResponse,
    DocumentDBDescribeGlobalClustersRequest,
    DocumentDBDescribeGlobalClustersResponse,
    DocumentDBDescribeOrderableDBInstanceOptionsRequest,
    DocumentDBDescribeOrderableDBInstanceOptionsResponse,
    DocumentDBDescribePendingMaintenanceActionsRequest,
    DocumentDBDescribePendingMaintenanceActionsResponse,
    DocumentDBDescribeServerlessV2PlatformVersionsRequest,
    DocumentDBDescribeServerlessV2PlatformVersionsResponse,
    DocumentDBFailoverDBClusterRequest,
    DocumentDBFailoverDBClusterResponse,
    DocumentDBFailoverGlobalClusterRequest,
    DocumentDBFailoverGlobalClusterResponse,
    DocumentDBListTagsForResourceRequest,
    DocumentDBListTagsForResourceResponse,
    DocumentDBModifyDBClusterParameterGroupRequest,
    DocumentDBModifyDBClusterParameterGroupResponse,
    DocumentDBModifyDBClusterRequest,
    DocumentDBModifyDBClusterResponse,
    DocumentDBModifyDBClusterSnapshotAttributeRequest,
    DocumentDBModifyDBClusterSnapshotAttributeResponse,
    DocumentDBModifyDBInstanceRequest,
    DocumentDBModifyDBInstanceResponse,
    DocumentDBModifyDBSubnetGroupRequest,
    DocumentDBModifyDBSubnetGroupResponse,
    DocumentDBModifyEventSubscriptionRequest,
    DocumentDBModifyEventSubscriptionResponse,
    DocumentDBModifyGlobalClusterRequest,
    DocumentDBModifyGlobalClusterResponse,
    DocumentDBRebootDBInstanceRequest,
    DocumentDBRebootDBInstanceResponse,
    DocumentDBRemoveFromGlobalClusterRequest,
    DocumentDBRemoveFromGlobalClusterResponse,
    DocumentDBRemoveSourceIdentifierFromSubscriptionRequest,
    DocumentDBRemoveSourceIdentifierFromSubscriptionResponse,
    DocumentDBRemoveTagsFromResourceRequest,
    DocumentDBRemoveTagsFromResourceResponse,
    DocumentDBResetDBClusterParameterGroupRequest,
    DocumentDBResetDBClusterParameterGroupResponse,
    DocumentDBRestoreDBClusterFromSnapshotRequest,
    DocumentDBRestoreDBClusterFromSnapshotResponse,
    DocumentDBRestoreDBClusterToPointInTimeRequest,
    DocumentDBRestoreDBClusterToPointInTimeResponse,
    DocumentDBStartDBClusterRequest,
    DocumentDBStartDBClusterResponse,
    DocumentDBStopDBClusterRequest,
    DocumentDBStopDBClusterResponse,
    DocumentDBSwitchoverGlobalClusterRequest,
    DocumentDBSwitchoverGlobalClusterResponse,
)
from werkflow_aws.types.documentdb_client import DocumentDBClient
from .base import AWSBaseService


class AWSDocumentDB(AWSBaseService[DocumentDBClient]):
    service_name = 'documentdb'
    boto3_service_name = 'docdb'

    def __init__(self) -> None:
        super().__init__(service_name='documentdb', boto3_service_name='docdb')

    async def add_source_identifier_to_subscription(
        self,
        request: DocumentDBAddSourceIdentifierToSubscriptionRequest,
    ) -> DocumentDBAddSourceIdentifierToSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.add_source_identifier_to_subscription, request, DocumentDBAddSourceIdentifierToSubscriptionResponse)

    async def add_tags_to_resource(
        self,
        request: DocumentDBAddTagsToResourceRequest,
    ) -> DocumentDBAddTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_resource, request, DocumentDBAddTagsToResourceResponse)

    async def apply_pending_maintenance_action(
        self,
        request: DocumentDBApplyPendingMaintenanceActionRequest,
    ) -> DocumentDBApplyPendingMaintenanceActionResponse:
        client = self._require_client()
        return await self._execute(client.apply_pending_maintenance_action, request, DocumentDBApplyPendingMaintenanceActionResponse)

    async def copy_db_cluster_parameter_group(
        self,
        request: DocumentDBCopyDBClusterParameterGroupRequest,
    ) -> DocumentDBCopyDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_cluster_parameter_group, request, DocumentDBCopyDBClusterParameterGroupResponse)

    async def copy_db_cluster_snapshot(
        self,
        request: DocumentDBCopyDBClusterSnapshotRequest,
    ) -> DocumentDBCopyDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_cluster_snapshot, request, DocumentDBCopyDBClusterSnapshotResponse)

    async def create_db_cluster(
        self,
        request: DocumentDBCreateDBClusterRequest,
    ) -> DocumentDBCreateDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster, request, DocumentDBCreateDBClusterResponse)

    async def create_db_cluster_parameter_group(
        self,
        request: DocumentDBCreateDBClusterParameterGroupRequest,
    ) -> DocumentDBCreateDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster_parameter_group, request, DocumentDBCreateDBClusterParameterGroupResponse)

    async def create_db_cluster_snapshot(
        self,
        request: DocumentDBCreateDBClusterSnapshotRequest,
    ) -> DocumentDBCreateDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster_snapshot, request, DocumentDBCreateDBClusterSnapshotResponse)

    async def create_db_instance(
        self,
        request: DocumentDBCreateDBInstanceRequest,
    ) -> DocumentDBCreateDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.create_db_instance, request, DocumentDBCreateDBInstanceResponse)

    async def create_db_subnet_group(
        self,
        request: DocumentDBCreateDBSubnetGroupRequest,
    ) -> DocumentDBCreateDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_subnet_group, request, DocumentDBCreateDBSubnetGroupResponse)

    async def create_event_subscription(
        self,
        request: DocumentDBCreateEventSubscriptionRequest,
    ) -> DocumentDBCreateEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_event_subscription, request, DocumentDBCreateEventSubscriptionResponse)

    async def create_global_cluster(
        self,
        request: DocumentDBCreateGlobalClusterRequest,
    ) -> DocumentDBCreateGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_global_cluster, request, DocumentDBCreateGlobalClusterResponse)

    async def delete_db_cluster(
        self,
        request: DocumentDBDeleteDBClusterRequest,
    ) -> DocumentDBDeleteDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster, request, DocumentDBDeleteDBClusterResponse)

    async def delete_db_cluster_parameter_group(
        self,
        request: DocumentDBDeleteDBClusterParameterGroupRequest,
    ) -> DocumentDBDeleteDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster_parameter_group, request, DocumentDBDeleteDBClusterParameterGroupResponse)

    async def delete_db_cluster_snapshot(
        self,
        request: DocumentDBDeleteDBClusterSnapshotRequest,
    ) -> DocumentDBDeleteDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster_snapshot, request, DocumentDBDeleteDBClusterSnapshotResponse)

    async def delete_db_instance(
        self,
        request: DocumentDBDeleteDBInstanceRequest,
    ) -> DocumentDBDeleteDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_instance, request, DocumentDBDeleteDBInstanceResponse)

    async def delete_db_subnet_group(
        self,
        request: DocumentDBDeleteDBSubnetGroupRequest,
    ) -> DocumentDBDeleteDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_subnet_group, request, DocumentDBDeleteDBSubnetGroupResponse)

    async def delete_event_subscription(
        self,
        request: DocumentDBDeleteEventSubscriptionRequest,
    ) -> DocumentDBDeleteEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_subscription, request, DocumentDBDeleteEventSubscriptionResponse)

    async def delete_global_cluster(
        self,
        request: DocumentDBDeleteGlobalClusterRequest,
    ) -> DocumentDBDeleteGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_global_cluster, request, DocumentDBDeleteGlobalClusterResponse)

    async def describe_certificates(
        self,
        request: DocumentDBDescribeCertificatesRequest | None = None,
    ) -> DocumentDBDescribeCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificates, request, DocumentDBDescribeCertificatesResponse)

    async def describe_certificates_paginated(
        self,
        request: DocumentDBDescribeCertificatesRequest | None = None,
    ) -> list[DocumentDBDescribeCertificatesResponse]:
        return await self._paginate('describe_certificates', request, DocumentDBDescribeCertificatesResponse)

    async def describe_db_cluster_parameter_groups(
        self,
        request: DocumentDBDescribeDBClusterParameterGroupsRequest | None = None,
    ) -> DocumentDBDescribeDBClusterParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_parameter_groups, request, DocumentDBDescribeDBClusterParameterGroupsResponse)

    async def describe_db_cluster_parameter_groups_paginated(
        self,
        request: DocumentDBDescribeDBClusterParameterGroupsRequest | None = None,
    ) -> list[DocumentDBDescribeDBClusterParameterGroupsResponse]:
        return await self._paginate('describe_db_cluster_parameter_groups', request, DocumentDBDescribeDBClusterParameterGroupsResponse)

    async def describe_db_cluster_parameters(
        self,
        request: DocumentDBDescribeDBClusterParametersRequest,
    ) -> DocumentDBDescribeDBClusterParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_parameters, request, DocumentDBDescribeDBClusterParametersResponse)

    async def describe_db_cluster_parameters_paginated(
        self,
        request: DocumentDBDescribeDBClusterParametersRequest,
    ) -> list[DocumentDBDescribeDBClusterParametersResponse]:
        return await self._paginate('describe_db_cluster_parameters', request, DocumentDBDescribeDBClusterParametersResponse)

    async def describe_db_cluster_snapshot_attributes(
        self,
        request: DocumentDBDescribeDBClusterSnapshotAttributesRequest,
    ) -> DocumentDBDescribeDBClusterSnapshotAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_snapshot_attributes, request, DocumentDBDescribeDBClusterSnapshotAttributesResponse)

    async def describe_db_cluster_snapshots(
        self,
        request: DocumentDBDescribeDBClusterSnapshotsRequest | None = None,
    ) -> DocumentDBDescribeDBClusterSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_snapshots, request, DocumentDBDescribeDBClusterSnapshotsResponse)

    async def describe_db_cluster_snapshots_paginated(
        self,
        request: DocumentDBDescribeDBClusterSnapshotsRequest | None = None,
    ) -> list[DocumentDBDescribeDBClusterSnapshotsResponse]:
        return await self._paginate('describe_db_cluster_snapshots', request, DocumentDBDescribeDBClusterSnapshotsResponse)

    async def describe_db_clusters(
        self,
        request: DocumentDBDescribeDBClustersRequest | None = None,
    ) -> DocumentDBDescribeDBClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_clusters, request, DocumentDBDescribeDBClustersResponse)

    async def describe_db_clusters_paginated(
        self,
        request: DocumentDBDescribeDBClustersRequest | None = None,
    ) -> list[DocumentDBDescribeDBClustersResponse]:
        return await self._paginate('describe_db_clusters', request, DocumentDBDescribeDBClustersResponse)

    async def describe_db_engine_versions(
        self,
        request: DocumentDBDescribeDBEngineVersionsRequest | None = None,
    ) -> DocumentDBDescribeDBEngineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_engine_versions, request, DocumentDBDescribeDBEngineVersionsResponse)

    async def describe_db_engine_versions_paginated(
        self,
        request: DocumentDBDescribeDBEngineVersionsRequest | None = None,
    ) -> list[DocumentDBDescribeDBEngineVersionsResponse]:
        return await self._paginate('describe_db_engine_versions', request, DocumentDBDescribeDBEngineVersionsResponse)

    async def describe_db_instances(
        self,
        request: DocumentDBDescribeDBInstancesRequest | None = None,
    ) -> DocumentDBDescribeDBInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_instances, request, DocumentDBDescribeDBInstancesResponse)

    async def describe_db_instances_paginated(
        self,
        request: DocumentDBDescribeDBInstancesRequest | None = None,
    ) -> list[DocumentDBDescribeDBInstancesResponse]:
        return await self._paginate('describe_db_instances', request, DocumentDBDescribeDBInstancesResponse)

    async def describe_db_subnet_groups(
        self,
        request: DocumentDBDescribeDBSubnetGroupsRequest | None = None,
    ) -> DocumentDBDescribeDBSubnetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_subnet_groups, request, DocumentDBDescribeDBSubnetGroupsResponse)

    async def describe_db_subnet_groups_paginated(
        self,
        request: DocumentDBDescribeDBSubnetGroupsRequest | None = None,
    ) -> list[DocumentDBDescribeDBSubnetGroupsResponse]:
        return await self._paginate('describe_db_subnet_groups', request, DocumentDBDescribeDBSubnetGroupsResponse)

    async def describe_engine_default_cluster_parameters(
        self,
        request: DocumentDBDescribeEngineDefaultClusterParametersRequest,
    ) -> DocumentDBDescribeEngineDefaultClusterParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_engine_default_cluster_parameters, request, DocumentDBDescribeEngineDefaultClusterParametersResponse)

    async def describe_event_categories(
        self,
        request: DocumentDBDescribeEventCategoriesRequest | None = None,
    ) -> DocumentDBDescribeEventCategoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_categories, request, DocumentDBDescribeEventCategoriesResponse)

    async def describe_event_subscriptions(
        self,
        request: DocumentDBDescribeEventSubscriptionsRequest | None = None,
    ) -> DocumentDBDescribeEventSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_subscriptions, request, DocumentDBDescribeEventSubscriptionsResponse)

    async def describe_event_subscriptions_paginated(
        self,
        request: DocumentDBDescribeEventSubscriptionsRequest | None = None,
    ) -> list[DocumentDBDescribeEventSubscriptionsResponse]:
        return await self._paginate('describe_event_subscriptions', request, DocumentDBDescribeEventSubscriptionsResponse)

    async def describe_events(
        self,
        request: DocumentDBDescribeEventsRequest | None = None,
    ) -> DocumentDBDescribeEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_events, request, DocumentDBDescribeEventsResponse)

    async def describe_events_paginated(
        self,
        request: DocumentDBDescribeEventsRequest | None = None,
    ) -> list[DocumentDBDescribeEventsResponse]:
        return await self._paginate('describe_events', request, DocumentDBDescribeEventsResponse)

    async def describe_global_clusters(
        self,
        request: DocumentDBDescribeGlobalClustersRequest | None = None,
    ) -> DocumentDBDescribeGlobalClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_clusters, request, DocumentDBDescribeGlobalClustersResponse)

    async def describe_global_clusters_paginated(
        self,
        request: DocumentDBDescribeGlobalClustersRequest | None = None,
    ) -> list[DocumentDBDescribeGlobalClustersResponse]:
        return await self._paginate('describe_global_clusters', request, DocumentDBDescribeGlobalClustersResponse)

    async def describe_orderable_db_instance_options(
        self,
        request: DocumentDBDescribeOrderableDBInstanceOptionsRequest,
    ) -> DocumentDBDescribeOrderableDBInstanceOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_orderable_db_instance_options, request, DocumentDBDescribeOrderableDBInstanceOptionsResponse)

    async def describe_orderable_db_instance_options_paginated(
        self,
        request: DocumentDBDescribeOrderableDBInstanceOptionsRequest,
    ) -> list[DocumentDBDescribeOrderableDBInstanceOptionsResponse]:
        return await self._paginate('describe_orderable_db_instance_options', request, DocumentDBDescribeOrderableDBInstanceOptionsResponse)

    async def describe_pending_maintenance_actions(
        self,
        request: DocumentDBDescribePendingMaintenanceActionsRequest | None = None,
    ) -> DocumentDBDescribePendingMaintenanceActionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_pending_maintenance_actions, request, DocumentDBDescribePendingMaintenanceActionsResponse)

    async def describe_pending_maintenance_actions_paginated(
        self,
        request: DocumentDBDescribePendingMaintenanceActionsRequest | None = None,
    ) -> list[DocumentDBDescribePendingMaintenanceActionsResponse]:
        return await self._paginate('describe_pending_maintenance_actions', request, DocumentDBDescribePendingMaintenanceActionsResponse)

    async def describe_serverless_v2_platform_versions(
        self,
        request: DocumentDBDescribeServerlessV2PlatformVersionsRequest | None = None,
    ) -> DocumentDBDescribeServerlessV2PlatformVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_serverless_v2_platform_versions, request, DocumentDBDescribeServerlessV2PlatformVersionsResponse)

    async def describe_serverless_v2_platform_versions_paginated(
        self,
        request: DocumentDBDescribeServerlessV2PlatformVersionsRequest | None = None,
    ) -> list[DocumentDBDescribeServerlessV2PlatformVersionsResponse]:
        return await self._paginate('describe_serverless_v2_platform_versions', request, DocumentDBDescribeServerlessV2PlatformVersionsResponse)

    async def failover_db_cluster(
        self,
        request: DocumentDBFailoverDBClusterRequest | None = None,
    ) -> DocumentDBFailoverDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.failover_db_cluster, request, DocumentDBFailoverDBClusterResponse)

    async def failover_global_cluster(
        self,
        request: DocumentDBFailoverGlobalClusterRequest,
    ) -> DocumentDBFailoverGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.failover_global_cluster, request, DocumentDBFailoverGlobalClusterResponse)

    async def list_tags_for_resource(
        self,
        request: DocumentDBListTagsForResourceRequest,
    ) -> DocumentDBListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, DocumentDBListTagsForResourceResponse)

    async def modify_db_cluster(
        self,
        request: DocumentDBModifyDBClusterRequest,
    ) -> DocumentDBModifyDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster, request, DocumentDBModifyDBClusterResponse)

    async def modify_db_cluster_parameter_group(
        self,
        request: DocumentDBModifyDBClusterParameterGroupRequest,
    ) -> DocumentDBModifyDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster_parameter_group, request, DocumentDBModifyDBClusterParameterGroupResponse)

    async def modify_db_cluster_snapshot_attribute(
        self,
        request: DocumentDBModifyDBClusterSnapshotAttributeRequest,
    ) -> DocumentDBModifyDBClusterSnapshotAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster_snapshot_attribute, request, DocumentDBModifyDBClusterSnapshotAttributeResponse)

    async def modify_db_instance(
        self,
        request: DocumentDBModifyDBInstanceRequest,
    ) -> DocumentDBModifyDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_instance, request, DocumentDBModifyDBInstanceResponse)

    async def modify_db_subnet_group(
        self,
        request: DocumentDBModifyDBSubnetGroupRequest,
    ) -> DocumentDBModifyDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_subnet_group, request, DocumentDBModifyDBSubnetGroupResponse)

    async def modify_event_subscription(
        self,
        request: DocumentDBModifyEventSubscriptionRequest,
    ) -> DocumentDBModifyEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.modify_event_subscription, request, DocumentDBModifyEventSubscriptionResponse)

    async def modify_global_cluster(
        self,
        request: DocumentDBModifyGlobalClusterRequest,
    ) -> DocumentDBModifyGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.modify_global_cluster, request, DocumentDBModifyGlobalClusterResponse)

    async def reboot_db_instance(
        self,
        request: DocumentDBRebootDBInstanceRequest,
    ) -> DocumentDBRebootDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.reboot_db_instance, request, DocumentDBRebootDBInstanceResponse)

    async def remove_from_global_cluster(
        self,
        request: DocumentDBRemoveFromGlobalClusterRequest,
    ) -> DocumentDBRemoveFromGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.remove_from_global_cluster, request, DocumentDBRemoveFromGlobalClusterResponse)

    async def remove_source_identifier_from_subscription(
        self,
        request: DocumentDBRemoveSourceIdentifierFromSubscriptionRequest,
    ) -> DocumentDBRemoveSourceIdentifierFromSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.remove_source_identifier_from_subscription, request, DocumentDBRemoveSourceIdentifierFromSubscriptionResponse)

    async def remove_tags_from_resource(
        self,
        request: DocumentDBRemoveTagsFromResourceRequest,
    ) -> DocumentDBRemoveTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_resource, request, DocumentDBRemoveTagsFromResourceResponse)

    async def reset_db_cluster_parameter_group(
        self,
        request: DocumentDBResetDBClusterParameterGroupRequest,
    ) -> DocumentDBResetDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.reset_db_cluster_parameter_group, request, DocumentDBResetDBClusterParameterGroupResponse)

    async def restore_db_cluster_from_snapshot(
        self,
        request: DocumentDBRestoreDBClusterFromSnapshotRequest,
    ) -> DocumentDBRestoreDBClusterFromSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.restore_db_cluster_from_snapshot, request, DocumentDBRestoreDBClusterFromSnapshotResponse)

    async def restore_db_cluster_to_point_in_time(
        self,
        request: DocumentDBRestoreDBClusterToPointInTimeRequest,
    ) -> DocumentDBRestoreDBClusterToPointInTimeResponse:
        client = self._require_client()
        return await self._execute(client.restore_db_cluster_to_point_in_time, request, DocumentDBRestoreDBClusterToPointInTimeResponse)

    async def start_db_cluster(
        self,
        request: DocumentDBStartDBClusterRequest,
    ) -> DocumentDBStartDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.start_db_cluster, request, DocumentDBStartDBClusterResponse)

    async def stop_db_cluster(
        self,
        request: DocumentDBStopDBClusterRequest,
    ) -> DocumentDBStopDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.stop_db_cluster, request, DocumentDBStopDBClusterResponse)

    async def switchover_global_cluster(
        self,
        request: DocumentDBSwitchoverGlobalClusterRequest,
    ) -> DocumentDBSwitchoverGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.switchover_global_cluster, request, DocumentDBSwitchoverGlobalClusterResponse)
