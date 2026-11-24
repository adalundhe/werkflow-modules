from werkflow_aws.models.rds import (
    RDSAddTagsToResourceRequest,
    RDSAddTagsToResourceResponse,
    RDSCreateDBClusterRequest,
    RDSCreateDBClusterResponse,
    RDSCreateDBClusterSnapshotRequest,
    RDSCreateDBClusterSnapshotResponse,
    RDSCreateDBInstanceRequest,
    RDSCreateDBInstanceResponse,
    RDSCreateDBSnapshotRequest,
    RDSCreateDBSnapshotResponse,
    RDSDeleteDBClusterRequest,
    RDSDeleteDBClusterResponse,
    RDSDeleteDBClusterSnapshotRequest,
    RDSDeleteDBClusterSnapshotResponse,
    RDSDeleteDBInstanceRequest,
    RDSDeleteDBInstanceResponse,
    RDSDeleteDBSnapshotRequest,
    RDSDeleteDBSnapshotResponse,
    RDSDescribeDBClusterSnapshotsRequest,
    RDSDescribeDBClusterSnapshotsResponse,
    RDSDescribeDBClustersRequest,
    RDSDescribeDBClustersResponse,
    RDSDescribeDBInstancesRequest,
    RDSDescribeDBInstancesResponse,
    RDSDescribeDBParameterGroupsRequest,
    RDSDescribeDBParameterGroupsResponse,
    RDSDescribeDBSnapshotsRequest,
    RDSDescribeDBSnapshotsResponse,
    RDSDescribeDBSubnetGroupsRequest,
    RDSDescribeDBSubnetGroupsResponse,
    RDSListTagsForResourceRequest,
    RDSListTagsForResourceResponse,
    RDSModifyDBClusterRequest,
    RDSModifyDBClusterResponse,
    RDSModifyDBInstanceRequest,
    RDSModifyDBInstanceResponse,
    RDSRebootDBInstanceRequest,
    RDSRebootDBInstanceResponse,
    RDSRemoveTagsFromResourceRequest,
    RDSRemoveTagsFromResourceResponse,
    RDSStartDBClusterRequest,
    RDSStartDBClusterResponse,
    RDSStartDBInstanceRequest,
    RDSStartDBInstanceResponse,
    RDSStopDBClusterRequest,
    RDSStopDBClusterResponse,
    RDSStopDBInstanceRequest,
    RDSStopDBInstanceResponse,
)
from werkflow_aws.services.base import AWSBaseService
from werkflow_aws.types.rds_client import RDSClient
from werkflow_aws.models.rds import (
    RDSAddRoleToDBClusterRequest,
    RDSAddRoleToDBClusterResponse,
    RDSAddRoleToDBInstanceRequest,
    RDSAddRoleToDBInstanceResponse,
    RDSAddSourceIdentifierToSubscriptionRequest,
    RDSAddSourceIdentifierToSubscriptionResponse,
    RDSApplyPendingMaintenanceActionRequest,
    RDSApplyPendingMaintenanceActionResponse,
    RDSAuthorizeDBSecurityGroupIngressRequest,
    RDSAuthorizeDBSecurityGroupIngressResponse,
    RDSBacktrackDBClusterRequest,
    RDSBacktrackDBClusterResponse,
    RDSCancelDBCapacityReservationRequest,
    RDSCancelDBCapacityReservationResponse,
    RDSCancelExportTaskRequest,
    RDSCancelExportTaskResponse,
    RDSCopyDBClusterParameterGroupRequest,
    RDSCopyDBClusterParameterGroupResponse,
    RDSCopyDBClusterSnapshotRequest,
    RDSCopyDBClusterSnapshotResponse,
    RDSCopyDBParameterGroupRequest,
    RDSCopyDBParameterGroupResponse,
    RDSCopyDBSnapshotRequest,
    RDSCopyDBSnapshotResponse,
    RDSCopyOptionGroupRequest,
    RDSCopyOptionGroupResponse,
    RDSCreateBlueGreenDeploymentRequest,
    RDSCreateBlueGreenDeploymentResponse,
    RDSCreateCustomDBEngineVersionRequest,
    RDSCreateCustomDBEngineVersionResponse,
    RDSCreateDBCapacityReservationRequest,
    RDSCreateDBCapacityReservationResponse,
    RDSCreateDBClusterEndpointRequest,
    RDSCreateDBClusterEndpointResponse,
    RDSCreateDBClusterParameterGroupRequest,
    RDSCreateDBClusterParameterGroupResponse,
    RDSCreateDBInstanceReadReplicaRequest,
    RDSCreateDBInstanceReadReplicaResponse,
    RDSCreateDBParameterGroupRequest,
    RDSCreateDBParameterGroupResponse,
    RDSCreateDBProxyEndpointRequest,
    RDSCreateDBProxyEndpointResponse,
    RDSCreateDBProxyRequest,
    RDSCreateDBProxyResponse,
    RDSCreateDBSecurityGroupRequest,
    RDSCreateDBSecurityGroupResponse,
    RDSCreateDBShardGroupRequest,
    RDSCreateDBShardGroupResponse,
    RDSCreateDBSubnetGroupRequest,
    RDSCreateDBSubnetGroupResponse,
    RDSCreateEventSubscriptionRequest,
    RDSCreateEventSubscriptionResponse,
    RDSCreateGlobalClusterRequest,
    RDSCreateGlobalClusterResponse,
    RDSCreateIntegrationRequest,
    RDSCreateIntegrationResponse,
    RDSCreateOptionGroupRequest,
    RDSCreateOptionGroupResponse,
    RDSCreateTenantDatabaseRequest,
    RDSCreateTenantDatabaseResponse,
    RDSDeleteBlueGreenDeploymentRequest,
    RDSDeleteBlueGreenDeploymentResponse,
    RDSDeleteCustomDBEngineVersionRequest,
    RDSDeleteCustomDBEngineVersionResponse,
    RDSDeleteDBClusterAutomatedBackupRequest,
    RDSDeleteDBClusterAutomatedBackupResponse,
    RDSDeleteDBClusterEndpointRequest,
    RDSDeleteDBClusterEndpointResponse,
    RDSDeleteDBClusterParameterGroupRequest,
    RDSDeleteDBClusterParameterGroupResponse,
    RDSDeleteDBInstanceAutomatedBackupRequest,
    RDSDeleteDBInstanceAutomatedBackupResponse,
    RDSDeleteDBParameterGroupRequest,
    RDSDeleteDBParameterGroupResponse,
    RDSDeleteDBProxyEndpointRequest,
    RDSDeleteDBProxyEndpointResponse,
    RDSDeleteDBProxyRequest,
    RDSDeleteDBProxyResponse,
    RDSDeleteDBSecurityGroupRequest,
    RDSDeleteDBSecurityGroupResponse,
    RDSDeleteDBShardGroupRequest,
    RDSDeleteDBShardGroupResponse,
    RDSDeleteDBSubnetGroupRequest,
    RDSDeleteDBSubnetGroupResponse,
    RDSDeleteEventSubscriptionRequest,
    RDSDeleteEventSubscriptionResponse,
    RDSDeleteGlobalClusterRequest,
    RDSDeleteGlobalClusterResponse,
    RDSDeleteIntegrationRequest,
    RDSDeleteIntegrationResponse,
    RDSDeleteOptionGroupRequest,
    RDSDeleteOptionGroupResponse,
    RDSDeleteTenantDatabaseRequest,
    RDSDeleteTenantDatabaseResponse,
    RDSDeregisterDBProxyTargetsRequest,
    RDSDeregisterDBProxyTargetsResponse,
    RDSDescribeAccountAttributesRequest,
    RDSDescribeAccountAttributesResponse,
    RDSDescribeBlueGreenDeploymentsRequest,
    RDSDescribeBlueGreenDeploymentsResponse,
    RDSDescribeCertificatesRequest,
    RDSDescribeCertificatesResponse,
    RDSDescribeDBCapacityReservationsRequest,
    RDSDescribeDBCapacityReservationsResponse,
    RDSDescribeDBClusterAutomatedBackupsRequest,
    RDSDescribeDBClusterAutomatedBackupsResponse,
    RDSDescribeDBClusterBacktracksRequest,
    RDSDescribeDBClusterBacktracksResponse,
    RDSDescribeDBClusterEndpointsRequest,
    RDSDescribeDBClusterEndpointsResponse,
    RDSDescribeDBClusterParameterGroupsRequest,
    RDSDescribeDBClusterParameterGroupsResponse,
    RDSDescribeDBClusterParametersRequest,
    RDSDescribeDBClusterParametersResponse,
    RDSDescribeDBClusterSnapshotAttributesRequest,
    RDSDescribeDBClusterSnapshotAttributesResponse,
    RDSDescribeDBEngineVersionsRequest,
    RDSDescribeDBEngineVersionsResponse,
    RDSDescribeDBInstanceAutomatedBackupsRequest,
    RDSDescribeDBInstanceAutomatedBackupsResponse,
    RDSDescribeDBLogFilesRequest,
    RDSDescribeDBLogFilesResponse,
    RDSDescribeDBMajorEngineVersionsRequest,
    RDSDescribeDBMajorEngineVersionsResponse,
    RDSDescribeDBParametersRequest,
    RDSDescribeDBParametersResponse,
    RDSDescribeDBProxiesRequest,
    RDSDescribeDBProxiesResponse,
    RDSDescribeDBProxyEndpointsRequest,
    RDSDescribeDBProxyEndpointsResponse,
    RDSDescribeDBProxyTargetGroupsRequest,
    RDSDescribeDBProxyTargetGroupsResponse,
    RDSDescribeDBProxyTargetsRequest,
    RDSDescribeDBProxyTargetsResponse,
    RDSDescribeDBRecommendationsRequest,
    RDSDescribeDBRecommendationsResponse,
    RDSDescribeDBSecurityGroupsRequest,
    RDSDescribeDBSecurityGroupsResponse,
    RDSDescribeDBShardGroupsRequest,
    RDSDescribeDBShardGroupsResponse,
    RDSDescribeDBSnapshotAttributesRequest,
    RDSDescribeDBSnapshotAttributesResponse,
    RDSDescribeDBSnapshotTenantDatabasesRequest,
    RDSDescribeDBSnapshotTenantDatabasesResponse,
    RDSDescribeEngineDefaultClusterParametersRequest,
    RDSDescribeEngineDefaultClusterParametersResponse,
    RDSDescribeEngineDefaultParametersRequest,
    RDSDescribeEngineDefaultParametersResponse,
    RDSDescribeEventCategoriesRequest,
    RDSDescribeEventCategoriesResponse,
    RDSDescribeEventSubscriptionsRequest,
    RDSDescribeEventSubscriptionsResponse,
    RDSDescribeEventsRequest,
    RDSDescribeEventsResponse,
    RDSDescribeExportTasksRequest,
    RDSDescribeExportTasksResponse,
    RDSDescribeGlobalClustersRequest,
    RDSDescribeGlobalClustersResponse,
    RDSDescribeIntegrationsRequest,
    RDSDescribeIntegrationsResponse,
    RDSDescribeOptionGroupOptionsRequest,
    RDSDescribeOptionGroupOptionsResponse,
    RDSDescribeOptionGroupsRequest,
    RDSDescribeOptionGroupsResponse,
    RDSDescribeOrderableDBInstanceOptionsRequest,
    RDSDescribeOrderableDBInstanceOptionsResponse,
    RDSDescribePendingMaintenanceActionsRequest,
    RDSDescribePendingMaintenanceActionsResponse,
    RDSDescribeReservedDBInstancesOfferingsRequest,
    RDSDescribeReservedDBInstancesOfferingsResponse,
    RDSDescribeReservedDBInstancesRequest,
    RDSDescribeReservedDBInstancesResponse,
    RDSDescribeServerlessV2PlatformVersionsRequest,
    RDSDescribeServerlessV2PlatformVersionsResponse,
    RDSDescribeSourceRegionsRequest,
    RDSDescribeSourceRegionsResponse,
    RDSDescribeTenantDatabasesRequest,
    RDSDescribeTenantDatabasesResponse,
    RDSDescribeValidDBInstanceModificationsRequest,
    RDSDescribeValidDBInstanceModificationsResponse,
    RDSDisableHttpEndpointRequest,
    RDSDisableHttpEndpointResponse,
    RDSDownloadDBLogFilePortionRequest,
    RDSDownloadDBLogFilePortionResponse,
    RDSEnableHttpEndpointRequest,
    RDSEnableHttpEndpointResponse,
    RDSFailoverDBClusterRequest,
    RDSFailoverDBClusterResponse,
    RDSFailoverGlobalClusterRequest,
    RDSFailoverGlobalClusterResponse,
    RDSModifyActivityStreamRequest,
    RDSModifyActivityStreamResponse,
    RDSModifyCertificatesRequest,
    RDSModifyCertificatesResponse,
    RDSModifyCurrentDBClusterCapacityRequest,
    RDSModifyCurrentDBClusterCapacityResponse,
    RDSModifyCustomDBEngineVersionRequest,
    RDSModifyCustomDBEngineVersionResponse,
    RDSModifyDBCapacityReservationRequest,
    RDSModifyDBCapacityReservationResponse,
    RDSModifyDBClusterEndpointRequest,
    RDSModifyDBClusterEndpointResponse,
    RDSModifyDBClusterParameterGroupRequest,
    RDSModifyDBClusterParameterGroupResponse,
    RDSModifyDBClusterSnapshotAttributeRequest,
    RDSModifyDBClusterSnapshotAttributeResponse,
    RDSModifyDBParameterGroupRequest,
    RDSModifyDBParameterGroupResponse,
    RDSModifyDBProxyEndpointRequest,
    RDSModifyDBProxyEndpointResponse,
    RDSModifyDBProxyRequest,
    RDSModifyDBProxyResponse,
    RDSModifyDBProxyTargetGroupRequest,
    RDSModifyDBProxyTargetGroupResponse,
    RDSModifyDBRecommendationRequest,
    RDSModifyDBRecommendationResponse,
    RDSModifyDBShardGroupRequest,
    RDSModifyDBShardGroupResponse,
    RDSModifyDBSnapshotAttributeRequest,
    RDSModifyDBSnapshotAttributeResponse,
    RDSModifyDBSnapshotRequest,
    RDSModifyDBSnapshotResponse,
    RDSModifyDBSubnetGroupRequest,
    RDSModifyDBSubnetGroupResponse,
    RDSModifyEventSubscriptionRequest,
    RDSModifyEventSubscriptionResponse,
    RDSModifyGlobalClusterRequest,
    RDSModifyGlobalClusterResponse,
    RDSModifyIntegrationRequest,
    RDSModifyIntegrationResponse,
    RDSModifyOptionGroupRequest,
    RDSModifyOptionGroupResponse,
    RDSModifyTenantDatabaseRequest,
    RDSModifyTenantDatabaseResponse,
    RDSPromoteReadReplicaDBClusterRequest,
    RDSPromoteReadReplicaDBClusterResponse,
    RDSPromoteReadReplicaRequest,
    RDSPromoteReadReplicaResponse,
    RDSPurchaseReservedDBInstancesOfferingRequest,
    RDSPurchaseReservedDBInstancesOfferingResponse,
    RDSRebootDBClusterRequest,
    RDSRebootDBClusterResponse,
    RDSRebootDBShardGroupRequest,
    RDSRebootDBShardGroupResponse,
    RDSRegisterDBProxyTargetsRequest,
    RDSRegisterDBProxyTargetsResponse,
    RDSRemoveFromGlobalClusterRequest,
    RDSRemoveFromGlobalClusterResponse,
    RDSRemoveRoleFromDBClusterRequest,
    RDSRemoveRoleFromDBClusterResponse,
    RDSRemoveRoleFromDBInstanceRequest,
    RDSRemoveRoleFromDBInstanceResponse,
    RDSRemoveSourceIdentifierFromSubscriptionRequest,
    RDSRemoveSourceIdentifierFromSubscriptionResponse,
    RDSResetDBClusterParameterGroupRequest,
    RDSResetDBClusterParameterGroupResponse,
    RDSResetDBParameterGroupRequest,
    RDSResetDBParameterGroupResponse,
    RDSRestoreDBClusterFromS3Request,
    RDSRestoreDBClusterFromS3Response,
    RDSRestoreDBClusterFromSnapshotRequest,
    RDSRestoreDBClusterFromSnapshotResponse,
    RDSRestoreDBClusterToPointInTimeRequest,
    RDSRestoreDBClusterToPointInTimeResponse,
    RDSRestoreDBInstanceFromDBSnapshotRequest,
    RDSRestoreDBInstanceFromDBSnapshotResponse,
    RDSRestoreDBInstanceFromS3Request,
    RDSRestoreDBInstanceFromS3Response,
    RDSRestoreDBInstanceToPointInTimeRequest,
    RDSRestoreDBInstanceToPointInTimeResponse,
    RDSRevokeDBSecurityGroupIngressRequest,
    RDSRevokeDBSecurityGroupIngressResponse,
    RDSStartActivityStreamRequest,
    RDSStartActivityStreamResponse,
    RDSStartDBInstanceAutomatedBackupsReplicationRequest,
    RDSStartDBInstanceAutomatedBackupsReplicationResponse,
    RDSStartExportTaskRequest,
    RDSStartExportTaskResponse,
    RDSStopActivityStreamRequest,
    RDSStopActivityStreamResponse,
    RDSStopDBInstanceAutomatedBackupsReplicationRequest,
    RDSStopDBInstanceAutomatedBackupsReplicationResponse,
    RDSSwitchoverBlueGreenDeploymentRequest,
    RDSSwitchoverBlueGreenDeploymentResponse,
    RDSSwitchoverGlobalClusterRequest,
    RDSSwitchoverGlobalClusterResponse,
    RDSSwitchoverReadReplicaRequest,
    RDSSwitchoverReadReplicaResponse,
)


class AWSRDS(AWSBaseService[RDSClient]):
    service_name = 'RDS'
    boto3_service_name = 'rds'

    async def describe_db_instances(
        self,
        request: RDSDescribeDBInstancesRequest | None = None,
    ) -> RDSDescribeDBInstancesResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_db_instances,
            request,
            RDSDescribeDBInstancesResponse,
        )

    async def describe_db_instances_paginated(
        self,
        request: RDSDescribeDBInstancesRequest | None = None,
    ) -> list[RDSDescribeDBInstancesResponse]:
        self._require_client()
        return await self._paginate(
            'describe_db_instances',
            request,
            RDSDescribeDBInstancesResponse,
        )

    async def create_db_instance(
        self,
        request: RDSCreateDBInstanceRequest,
    ) -> RDSCreateDBInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.create_db_instance,
            request,
            RDSCreateDBInstanceResponse,
        )

    async def modify_db_instance(
        self,
        request: RDSModifyDBInstanceRequest,
    ) -> RDSModifyDBInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.modify_db_instance,
            request,
            RDSModifyDBInstanceResponse,
        )

    async def delete_db_instance(
        self,
        request: RDSDeleteDBInstanceRequest,
    ) -> RDSDeleteDBInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_db_instance,
            request,
            RDSDeleteDBInstanceResponse,
        )

    async def start_db_instance(
        self,
        request: RDSStartDBInstanceRequest,
    ) -> RDSStartDBInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.start_db_instance,
            request,
            RDSStartDBInstanceResponse,
        )

    async def stop_db_instance(
        self,
        request: RDSStopDBInstanceRequest,
    ) -> RDSStopDBInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.stop_db_instance,
            request,
            RDSStopDBInstanceResponse,
        )

    async def reboot_db_instance(
        self,
        request: RDSRebootDBInstanceRequest,
    ) -> RDSRebootDBInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.reboot_db_instance,
            request,
            RDSRebootDBInstanceResponse,
        )

    async def describe_db_clusters(
        self,
        request: RDSDescribeDBClustersRequest | None = None,
    ) -> RDSDescribeDBClustersResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_db_clusters,
            request,
            RDSDescribeDBClustersResponse,
        )

    async def describe_db_clusters_paginated(
        self,
        request: RDSDescribeDBClustersRequest | None = None,
    ) -> list[RDSDescribeDBClustersResponse]:
        self._require_client()
        return await self._paginate(
            'describe_db_clusters',
            request,
            RDSDescribeDBClustersResponse,
        )

    async def create_db_cluster(
        self,
        request: RDSCreateDBClusterRequest,
    ) -> RDSCreateDBClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.create_db_cluster,
            request,
            RDSCreateDBClusterResponse,
        )

    async def modify_db_cluster(
        self,
        request: RDSModifyDBClusterRequest,
    ) -> RDSModifyDBClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.modify_db_cluster,
            request,
            RDSModifyDBClusterResponse,
        )

    async def delete_db_cluster(
        self,
        request: RDSDeleteDBClusterRequest,
    ) -> RDSDeleteDBClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_db_cluster,
            request,
            RDSDeleteDBClusterResponse,
        )

    async def start_db_cluster(
        self,
        request: RDSStartDBClusterRequest,
    ) -> RDSStartDBClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.start_db_cluster,
            request,
            RDSStartDBClusterResponse,
        )

    async def stop_db_cluster(
        self,
        request: RDSStopDBClusterRequest,
    ) -> RDSStopDBClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.stop_db_cluster,
            request,
            RDSStopDBClusterResponse,
        )

    async def describe_db_snapshots(
        self,
        request: RDSDescribeDBSnapshotsRequest | None = None,
    ) -> RDSDescribeDBSnapshotsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_db_snapshots,
            request,
            RDSDescribeDBSnapshotsResponse,
        )

    async def describe_db_snapshots_paginated(
        self,
        request: RDSDescribeDBSnapshotsRequest | None = None,
    ) -> list[RDSDescribeDBSnapshotsResponse]:
        self._require_client()
        return await self._paginate(
            'describe_db_snapshots',
            request,
            RDSDescribeDBSnapshotsResponse,
        )

    async def create_db_snapshot(
        self,
        request: RDSCreateDBSnapshotRequest,
    ) -> RDSCreateDBSnapshotResponse:
        client = self._require_client()
        return await self._execute(
            client.create_db_snapshot,
            request,
            RDSCreateDBSnapshotResponse,
        )

    async def delete_db_snapshot(
        self,
        request: RDSDeleteDBSnapshotRequest,
    ) -> RDSDeleteDBSnapshotResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_db_snapshot,
            request,
            RDSDeleteDBSnapshotResponse,
        )

    async def describe_db_cluster_snapshots(
        self,
        request: RDSDescribeDBClusterSnapshotsRequest | None = None,
    ) -> RDSDescribeDBClusterSnapshotsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_db_cluster_snapshots,
            request,
            RDSDescribeDBClusterSnapshotsResponse,
        )

    async def describe_db_cluster_snapshots_paginated(
        self,
        request: RDSDescribeDBClusterSnapshotsRequest | None = None,
    ) -> list[RDSDescribeDBClusterSnapshotsResponse]:
        self._require_client()
        return await self._paginate(
            'describe_db_cluster_snapshots',
            request,
            RDSDescribeDBClusterSnapshotsResponse,
        )

    async def create_db_cluster_snapshot(
        self,
        request: RDSCreateDBClusterSnapshotRequest,
    ) -> RDSCreateDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(
            client.create_db_cluster_snapshot,
            request,
            RDSCreateDBClusterSnapshotResponse,
        )

    async def delete_db_cluster_snapshot(
        self,
        request: RDSDeleteDBClusterSnapshotRequest,
    ) -> RDSDeleteDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_db_cluster_snapshot,
            request,
            RDSDeleteDBClusterSnapshotResponse,
        )

    async def describe_db_subnet_groups(
        self,
        request: RDSDescribeDBSubnetGroupsRequest | None = None,
    ) -> RDSDescribeDBSubnetGroupsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_db_subnet_groups,
            request,
            RDSDescribeDBSubnetGroupsResponse,
        )

    async def describe_db_subnet_groups_paginated(
        self,
        request: RDSDescribeDBSubnetGroupsRequest | None = None,
    ) -> list[RDSDescribeDBSubnetGroupsResponse]:
        self._require_client()
        return await self._paginate(
            'describe_db_subnet_groups',
            request,
            RDSDescribeDBSubnetGroupsResponse,
        )

    async def describe_db_parameter_groups(
        self,
        request: RDSDescribeDBParameterGroupsRequest | None = None,
    ) -> RDSDescribeDBParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_db_parameter_groups,
            request,
            RDSDescribeDBParameterGroupsResponse,
        )

    async def describe_db_parameter_groups_paginated(
        self,
        request: RDSDescribeDBParameterGroupsRequest | None = None,
    ) -> list[RDSDescribeDBParameterGroupsResponse]:
        self._require_client()
        return await self._paginate(
            'describe_db_parameter_groups',
            request,
            RDSDescribeDBParameterGroupsResponse,
        )

    async def list_tags_for_resource(
        self,
        request: RDSListTagsForResourceRequest,
    ) -> RDSListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tags_for_resource,
            request,
            RDSListTagsForResourceResponse,
        )

    async def add_tags_to_resource(
        self,
        request: RDSAddTagsToResourceRequest,
    ) -> RDSAddTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.add_tags_to_resource,
            request,
            RDSAddTagsToResourceResponse,
        )

    async def remove_tags_from_resource(
        self,
        request: RDSRemoveTagsFromResourceRequest,
    ) -> RDSRemoveTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.remove_tags_from_resource,
            request,
            RDSRemoveTagsFromResourceResponse,
        )

    async def add_role_to_db_cluster(
        self,
        request: RDSAddRoleToDBClusterRequest,
    ) -> RDSAddRoleToDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.add_role_to_db_cluster, request, RDSAddRoleToDBClusterResponse)

    async def add_role_to_db_instance(
        self,
        request: RDSAddRoleToDBInstanceRequest,
    ) -> RDSAddRoleToDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.add_role_to_db_instance, request, RDSAddRoleToDBInstanceResponse)

    async def add_source_identifier_to_subscription(
        self,
        request: RDSAddSourceIdentifierToSubscriptionRequest,
    ) -> RDSAddSourceIdentifierToSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.add_source_identifier_to_subscription, request, RDSAddSourceIdentifierToSubscriptionResponse)

    async def apply_pending_maintenance_action(
        self,
        request: RDSApplyPendingMaintenanceActionRequest,
    ) -> RDSApplyPendingMaintenanceActionResponse:
        client = self._require_client()
        return await self._execute(client.apply_pending_maintenance_action, request, RDSApplyPendingMaintenanceActionResponse)

    async def authorize_db_security_group_ingress(
        self,
        request: RDSAuthorizeDBSecurityGroupIngressRequest,
    ) -> RDSAuthorizeDBSecurityGroupIngressResponse:
        client = self._require_client()
        return await self._execute(client.authorize_db_security_group_ingress, request, RDSAuthorizeDBSecurityGroupIngressResponse)

    async def backtrack_db_cluster(
        self,
        request: RDSBacktrackDBClusterRequest,
    ) -> RDSBacktrackDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.backtrack_db_cluster, request, RDSBacktrackDBClusterResponse)

    async def cancel_db_capacity_reservation(
        self,
        request: RDSCancelDBCapacityReservationRequest,
    ) -> RDSCancelDBCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.cancel_db_capacity_reservation, request, RDSCancelDBCapacityReservationResponse)

    async def cancel_export_task(
        self,
        request: RDSCancelExportTaskRequest,
    ) -> RDSCancelExportTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_export_task, request, RDSCancelExportTaskResponse)

    async def copy_db_cluster_parameter_group(
        self,
        request: RDSCopyDBClusterParameterGroupRequest,
    ) -> RDSCopyDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_cluster_parameter_group, request, RDSCopyDBClusterParameterGroupResponse)

    async def copy_db_cluster_snapshot(
        self,
        request: RDSCopyDBClusterSnapshotRequest,
    ) -> RDSCopyDBClusterSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_cluster_snapshot, request, RDSCopyDBClusterSnapshotResponse)

    async def copy_db_parameter_group(
        self,
        request: RDSCopyDBParameterGroupRequest,
    ) -> RDSCopyDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_parameter_group, request, RDSCopyDBParameterGroupResponse)

    async def copy_db_snapshot(
        self,
        request: RDSCopyDBSnapshotRequest,
    ) -> RDSCopyDBSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_db_snapshot, request, RDSCopyDBSnapshotResponse)

    async def copy_option_group(
        self,
        request: RDSCopyOptionGroupRequest,
    ) -> RDSCopyOptionGroupResponse:
        client = self._require_client()
        return await self._execute(client.copy_option_group, request, RDSCopyOptionGroupResponse)

    async def create_blue_green_deployment(
        self,
        request: RDSCreateBlueGreenDeploymentRequest,
    ) -> RDSCreateBlueGreenDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.create_blue_green_deployment, request, RDSCreateBlueGreenDeploymentResponse)

    async def create_custom_db_engine_version(
        self,
        request: RDSCreateCustomDBEngineVersionRequest,
    ) -> RDSCreateCustomDBEngineVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_db_engine_version, request, RDSCreateCustomDBEngineVersionResponse)

    async def create_db_capacity_reservation(
        self,
        request: RDSCreateDBCapacityReservationRequest,
    ) -> RDSCreateDBCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.create_db_capacity_reservation, request, RDSCreateDBCapacityReservationResponse)

    async def create_db_cluster_endpoint(
        self,
        request: RDSCreateDBClusterEndpointRequest,
    ) -> RDSCreateDBClusterEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster_endpoint, request, RDSCreateDBClusterEndpointResponse)

    async def create_db_cluster_parameter_group(
        self,
        request: RDSCreateDBClusterParameterGroupRequest,
    ) -> RDSCreateDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_cluster_parameter_group, request, RDSCreateDBClusterParameterGroupResponse)

    async def create_db_instance_read_replica(
        self,
        request: RDSCreateDBInstanceReadReplicaRequest,
    ) -> RDSCreateDBInstanceReadReplicaResponse:
        client = self._require_client()
        return await self._execute(client.create_db_instance_read_replica, request, RDSCreateDBInstanceReadReplicaResponse)

    async def create_db_parameter_group(
        self,
        request: RDSCreateDBParameterGroupRequest,
    ) -> RDSCreateDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_parameter_group, request, RDSCreateDBParameterGroupResponse)

    async def create_db_proxy(
        self,
        request: RDSCreateDBProxyRequest,
    ) -> RDSCreateDBProxyResponse:
        client = self._require_client()
        return await self._execute(client.create_db_proxy, request, RDSCreateDBProxyResponse)

    async def create_db_proxy_endpoint(
        self,
        request: RDSCreateDBProxyEndpointRequest,
    ) -> RDSCreateDBProxyEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_db_proxy_endpoint, request, RDSCreateDBProxyEndpointResponse)

    async def create_db_security_group(
        self,
        request: RDSCreateDBSecurityGroupRequest,
    ) -> RDSCreateDBSecurityGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_security_group, request, RDSCreateDBSecurityGroupResponse)

    async def create_db_shard_group(
        self,
        request: RDSCreateDBShardGroupRequest,
    ) -> RDSCreateDBShardGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_shard_group, request, RDSCreateDBShardGroupResponse)

    async def create_db_subnet_group(
        self,
        request: RDSCreateDBSubnetGroupRequest,
    ) -> RDSCreateDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_db_subnet_group, request, RDSCreateDBSubnetGroupResponse)

    async def create_event_subscription(
        self,
        request: RDSCreateEventSubscriptionRequest,
    ) -> RDSCreateEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_event_subscription, request, RDSCreateEventSubscriptionResponse)

    async def create_global_cluster(
        self,
        request: RDSCreateGlobalClusterRequest,
    ) -> RDSCreateGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_global_cluster, request, RDSCreateGlobalClusterResponse)

    async def create_integration(
        self,
        request: RDSCreateIntegrationRequest,
    ) -> RDSCreateIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.create_integration, request, RDSCreateIntegrationResponse)

    async def create_option_group(
        self,
        request: RDSCreateOptionGroupRequest,
    ) -> RDSCreateOptionGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_option_group, request, RDSCreateOptionGroupResponse)

    async def create_tenant_database(
        self,
        request: RDSCreateTenantDatabaseRequest,
    ) -> RDSCreateTenantDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.create_tenant_database, request, RDSCreateTenantDatabaseResponse)

    async def delete_blue_green_deployment(
        self,
        request: RDSDeleteBlueGreenDeploymentRequest,
    ) -> RDSDeleteBlueGreenDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.delete_blue_green_deployment, request, RDSDeleteBlueGreenDeploymentResponse)

    async def delete_custom_db_engine_version(
        self,
        request: RDSDeleteCustomDBEngineVersionRequest,
    ) -> RDSDeleteCustomDBEngineVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_db_engine_version, request, RDSDeleteCustomDBEngineVersionResponse)

    async def delete_db_cluster_automated_backup(
        self,
        request: RDSDeleteDBClusterAutomatedBackupRequest,
    ) -> RDSDeleteDBClusterAutomatedBackupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster_automated_backup, request, RDSDeleteDBClusterAutomatedBackupResponse)

    async def delete_db_cluster_endpoint(
        self,
        request: RDSDeleteDBClusterEndpointRequest,
    ) -> RDSDeleteDBClusterEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster_endpoint, request, RDSDeleteDBClusterEndpointResponse)

    async def delete_db_cluster_parameter_group(
        self,
        request: RDSDeleteDBClusterParameterGroupRequest,
    ) -> RDSDeleteDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_cluster_parameter_group, request, RDSDeleteDBClusterParameterGroupResponse)

    async def delete_db_instance_automated_backup(
        self,
        request: RDSDeleteDBInstanceAutomatedBackupRequest | None = None,
    ) -> RDSDeleteDBInstanceAutomatedBackupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_instance_automated_backup, request, RDSDeleteDBInstanceAutomatedBackupResponse)

    async def delete_db_parameter_group(
        self,
        request: RDSDeleteDBParameterGroupRequest,
    ) -> RDSDeleteDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_parameter_group, request, RDSDeleteDBParameterGroupResponse)

    async def delete_db_proxy(
        self,
        request: RDSDeleteDBProxyRequest,
    ) -> RDSDeleteDBProxyResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_proxy, request, RDSDeleteDBProxyResponse)

    async def delete_db_proxy_endpoint(
        self,
        request: RDSDeleteDBProxyEndpointRequest,
    ) -> RDSDeleteDBProxyEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_proxy_endpoint, request, RDSDeleteDBProxyEndpointResponse)

    async def delete_db_security_group(
        self,
        request: RDSDeleteDBSecurityGroupRequest,
    ) -> RDSDeleteDBSecurityGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_security_group, request, RDSDeleteDBSecurityGroupResponse)

    async def delete_db_shard_group(
        self,
        request: RDSDeleteDBShardGroupRequest,
    ) -> RDSDeleteDBShardGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_shard_group, request, RDSDeleteDBShardGroupResponse)

    async def delete_db_subnet_group(
        self,
        request: RDSDeleteDBSubnetGroupRequest,
    ) -> RDSDeleteDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_db_subnet_group, request, RDSDeleteDBSubnetGroupResponse)

    async def delete_event_subscription(
        self,
        request: RDSDeleteEventSubscriptionRequest,
    ) -> RDSDeleteEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_subscription, request, RDSDeleteEventSubscriptionResponse)

    async def delete_global_cluster(
        self,
        request: RDSDeleteGlobalClusterRequest,
    ) -> RDSDeleteGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_global_cluster, request, RDSDeleteGlobalClusterResponse)

    async def delete_integration(
        self,
        request: RDSDeleteIntegrationRequest,
    ) -> RDSDeleteIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration, request, RDSDeleteIntegrationResponse)

    async def delete_option_group(
        self,
        request: RDSDeleteOptionGroupRequest,
    ) -> RDSDeleteOptionGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_option_group, request, RDSDeleteOptionGroupResponse)

    async def delete_tenant_database(
        self,
        request: RDSDeleteTenantDatabaseRequest,
    ) -> RDSDeleteTenantDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.delete_tenant_database, request, RDSDeleteTenantDatabaseResponse)

    async def deregister_db_proxy_targets(
        self,
        request: RDSDeregisterDBProxyTargetsRequest,
    ) -> RDSDeregisterDBProxyTargetsResponse:
        client = self._require_client()
        return await self._execute(client.deregister_db_proxy_targets, request, RDSDeregisterDBProxyTargetsResponse)

    async def describe_account_attributes(
        self,
        request: RDSDescribeAccountAttributesRequest | None = None,
    ) -> RDSDescribeAccountAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_attributes, request, RDSDescribeAccountAttributesResponse)

    async def describe_blue_green_deployments(
        self,
        request: RDSDescribeBlueGreenDeploymentsRequest | None = None,
    ) -> RDSDescribeBlueGreenDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_blue_green_deployments, request, RDSDescribeBlueGreenDeploymentsResponse)

    async def describe_blue_green_deployments_paginated(
        self,
        request: RDSDescribeBlueGreenDeploymentsRequest | None = None,
    ) -> list[RDSDescribeBlueGreenDeploymentsResponse]:
        return await self._paginate('describe_blue_green_deployments', request, RDSDescribeBlueGreenDeploymentsResponse)

    async def describe_certificates(
        self,
        request: RDSDescribeCertificatesRequest | None = None,
    ) -> RDSDescribeCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificates, request, RDSDescribeCertificatesResponse)

    async def describe_certificates_paginated(
        self,
        request: RDSDescribeCertificatesRequest | None = None,
    ) -> list[RDSDescribeCertificatesResponse]:
        return await self._paginate('describe_certificates', request, RDSDescribeCertificatesResponse)

    async def describe_db_capacity_reservations(
        self,
        request: RDSDescribeDBCapacityReservationsRequest | None = None,
    ) -> RDSDescribeDBCapacityReservationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_capacity_reservations, request, RDSDescribeDBCapacityReservationsResponse)

    async def describe_db_capacity_reservations_paginated(
        self,
        request: RDSDescribeDBCapacityReservationsRequest | None = None,
    ) -> list[RDSDescribeDBCapacityReservationsResponse]:
        return await self._paginate('describe_db_capacity_reservations', request, RDSDescribeDBCapacityReservationsResponse)

    async def describe_db_cluster_automated_backups(
        self,
        request: RDSDescribeDBClusterAutomatedBackupsRequest | None = None,
    ) -> RDSDescribeDBClusterAutomatedBackupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_automated_backups, request, RDSDescribeDBClusterAutomatedBackupsResponse)

    async def describe_db_cluster_automated_backups_paginated(
        self,
        request: RDSDescribeDBClusterAutomatedBackupsRequest | None = None,
    ) -> list[RDSDescribeDBClusterAutomatedBackupsResponse]:
        return await self._paginate('describe_db_cluster_automated_backups', request, RDSDescribeDBClusterAutomatedBackupsResponse)

    async def describe_db_cluster_backtracks(
        self,
        request: RDSDescribeDBClusterBacktracksRequest,
    ) -> RDSDescribeDBClusterBacktracksResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_backtracks, request, RDSDescribeDBClusterBacktracksResponse)

    async def describe_db_cluster_backtracks_paginated(
        self,
        request: RDSDescribeDBClusterBacktracksRequest,
    ) -> list[RDSDescribeDBClusterBacktracksResponse]:
        return await self._paginate('describe_db_cluster_backtracks', request, RDSDescribeDBClusterBacktracksResponse)

    async def describe_db_cluster_endpoints(
        self,
        request: RDSDescribeDBClusterEndpointsRequest | None = None,
    ) -> RDSDescribeDBClusterEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_endpoints, request, RDSDescribeDBClusterEndpointsResponse)

    async def describe_db_cluster_endpoints_paginated(
        self,
        request: RDSDescribeDBClusterEndpointsRequest | None = None,
    ) -> list[RDSDescribeDBClusterEndpointsResponse]:
        return await self._paginate('describe_db_cluster_endpoints', request, RDSDescribeDBClusterEndpointsResponse)

    async def describe_db_cluster_parameter_groups(
        self,
        request: RDSDescribeDBClusterParameterGroupsRequest | None = None,
    ) -> RDSDescribeDBClusterParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_parameter_groups, request, RDSDescribeDBClusterParameterGroupsResponse)

    async def describe_db_cluster_parameter_groups_paginated(
        self,
        request: RDSDescribeDBClusterParameterGroupsRequest | None = None,
    ) -> list[RDSDescribeDBClusterParameterGroupsResponse]:
        return await self._paginate('describe_db_cluster_parameter_groups', request, RDSDescribeDBClusterParameterGroupsResponse)

    async def describe_db_cluster_parameters(
        self,
        request: RDSDescribeDBClusterParametersRequest,
    ) -> RDSDescribeDBClusterParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_parameters, request, RDSDescribeDBClusterParametersResponse)

    async def describe_db_cluster_parameters_paginated(
        self,
        request: RDSDescribeDBClusterParametersRequest,
    ) -> list[RDSDescribeDBClusterParametersResponse]:
        return await self._paginate('describe_db_cluster_parameters', request, RDSDescribeDBClusterParametersResponse)

    async def describe_db_cluster_snapshot_attributes(
        self,
        request: RDSDescribeDBClusterSnapshotAttributesRequest,
    ) -> RDSDescribeDBClusterSnapshotAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_cluster_snapshot_attributes, request, RDSDescribeDBClusterSnapshotAttributesResponse)

    async def describe_db_engine_versions(
        self,
        request: RDSDescribeDBEngineVersionsRequest | None = None,
    ) -> RDSDescribeDBEngineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_engine_versions, request, RDSDescribeDBEngineVersionsResponse)

    async def describe_db_engine_versions_paginated(
        self,
        request: RDSDescribeDBEngineVersionsRequest | None = None,
    ) -> list[RDSDescribeDBEngineVersionsResponse]:
        return await self._paginate('describe_db_engine_versions', request, RDSDescribeDBEngineVersionsResponse)

    async def describe_db_instance_automated_backups(
        self,
        request: RDSDescribeDBInstanceAutomatedBackupsRequest | None = None,
    ) -> RDSDescribeDBInstanceAutomatedBackupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_instance_automated_backups, request, RDSDescribeDBInstanceAutomatedBackupsResponse)

    async def describe_db_instance_automated_backups_paginated(
        self,
        request: RDSDescribeDBInstanceAutomatedBackupsRequest | None = None,
    ) -> list[RDSDescribeDBInstanceAutomatedBackupsResponse]:
        return await self._paginate('describe_db_instance_automated_backups', request, RDSDescribeDBInstanceAutomatedBackupsResponse)

    async def describe_db_log_files(
        self,
        request: RDSDescribeDBLogFilesRequest,
    ) -> RDSDescribeDBLogFilesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_log_files, request, RDSDescribeDBLogFilesResponse)

    async def describe_db_log_files_paginated(
        self,
        request: RDSDescribeDBLogFilesRequest,
    ) -> list[RDSDescribeDBLogFilesResponse]:
        return await self._paginate('describe_db_log_files', request, RDSDescribeDBLogFilesResponse)

    async def describe_db_major_engine_versions(
        self,
        request: RDSDescribeDBMajorEngineVersionsRequest | None = None,
    ) -> RDSDescribeDBMajorEngineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_major_engine_versions, request, RDSDescribeDBMajorEngineVersionsResponse)

    async def describe_db_major_engine_versions_paginated(
        self,
        request: RDSDescribeDBMajorEngineVersionsRequest | None = None,
    ) -> list[RDSDescribeDBMajorEngineVersionsResponse]:
        return await self._paginate('describe_db_major_engine_versions', request, RDSDescribeDBMajorEngineVersionsResponse)

    async def describe_db_parameters(
        self,
        request: RDSDescribeDBParametersRequest,
    ) -> RDSDescribeDBParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_parameters, request, RDSDescribeDBParametersResponse)

    async def describe_db_parameters_paginated(
        self,
        request: RDSDescribeDBParametersRequest,
    ) -> list[RDSDescribeDBParametersResponse]:
        return await self._paginate('describe_db_parameters', request, RDSDescribeDBParametersResponse)

    async def describe_db_proxies(
        self,
        request: RDSDescribeDBProxiesRequest | None = None,
    ) -> RDSDescribeDBProxiesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_proxies, request, RDSDescribeDBProxiesResponse)

    async def describe_db_proxies_paginated(
        self,
        request: RDSDescribeDBProxiesRequest | None = None,
    ) -> list[RDSDescribeDBProxiesResponse]:
        return await self._paginate('describe_db_proxies', request, RDSDescribeDBProxiesResponse)

    async def describe_db_proxy_endpoints(
        self,
        request: RDSDescribeDBProxyEndpointsRequest | None = None,
    ) -> RDSDescribeDBProxyEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_proxy_endpoints, request, RDSDescribeDBProxyEndpointsResponse)

    async def describe_db_proxy_endpoints_paginated(
        self,
        request: RDSDescribeDBProxyEndpointsRequest | None = None,
    ) -> list[RDSDescribeDBProxyEndpointsResponse]:
        return await self._paginate('describe_db_proxy_endpoints', request, RDSDescribeDBProxyEndpointsResponse)

    async def describe_db_proxy_target_groups(
        self,
        request: RDSDescribeDBProxyTargetGroupsRequest,
    ) -> RDSDescribeDBProxyTargetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_proxy_target_groups, request, RDSDescribeDBProxyTargetGroupsResponse)

    async def describe_db_proxy_target_groups_paginated(
        self,
        request: RDSDescribeDBProxyTargetGroupsRequest,
    ) -> list[RDSDescribeDBProxyTargetGroupsResponse]:
        return await self._paginate('describe_db_proxy_target_groups', request, RDSDescribeDBProxyTargetGroupsResponse)

    async def describe_db_proxy_targets(
        self,
        request: RDSDescribeDBProxyTargetsRequest,
    ) -> RDSDescribeDBProxyTargetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_proxy_targets, request, RDSDescribeDBProxyTargetsResponse)

    async def describe_db_proxy_targets_paginated(
        self,
        request: RDSDescribeDBProxyTargetsRequest,
    ) -> list[RDSDescribeDBProxyTargetsResponse]:
        return await self._paginate('describe_db_proxy_targets', request, RDSDescribeDBProxyTargetsResponse)

    async def describe_db_recommendations(
        self,
        request: RDSDescribeDBRecommendationsRequest | None = None,
    ) -> RDSDescribeDBRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_recommendations, request, RDSDescribeDBRecommendationsResponse)

    async def describe_db_recommendations_paginated(
        self,
        request: RDSDescribeDBRecommendationsRequest | None = None,
    ) -> list[RDSDescribeDBRecommendationsResponse]:
        return await self._paginate('describe_db_recommendations', request, RDSDescribeDBRecommendationsResponse)

    async def describe_db_security_groups(
        self,
        request: RDSDescribeDBSecurityGroupsRequest | None = None,
    ) -> RDSDescribeDBSecurityGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_security_groups, request, RDSDescribeDBSecurityGroupsResponse)

    async def describe_db_security_groups_paginated(
        self,
        request: RDSDescribeDBSecurityGroupsRequest | None = None,
    ) -> list[RDSDescribeDBSecurityGroupsResponse]:
        return await self._paginate('describe_db_security_groups', request, RDSDescribeDBSecurityGroupsResponse)

    async def describe_db_shard_groups(
        self,
        request: RDSDescribeDBShardGroupsRequest | None = None,
    ) -> RDSDescribeDBShardGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_shard_groups, request, RDSDescribeDBShardGroupsResponse)

    async def describe_db_snapshot_attributes(
        self,
        request: RDSDescribeDBSnapshotAttributesRequest,
    ) -> RDSDescribeDBSnapshotAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_snapshot_attributes, request, RDSDescribeDBSnapshotAttributesResponse)

    async def describe_db_snapshot_tenant_databases(
        self,
        request: RDSDescribeDBSnapshotTenantDatabasesRequest | None = None,
    ) -> RDSDescribeDBSnapshotTenantDatabasesResponse:
        client = self._require_client()
        return await self._execute(client.describe_db_snapshot_tenant_databases, request, RDSDescribeDBSnapshotTenantDatabasesResponse)

    async def describe_db_snapshot_tenant_databases_paginated(
        self,
        request: RDSDescribeDBSnapshotTenantDatabasesRequest | None = None,
    ) -> list[RDSDescribeDBSnapshotTenantDatabasesResponse]:
        return await self._paginate('describe_db_snapshot_tenant_databases', request, RDSDescribeDBSnapshotTenantDatabasesResponse)

    async def describe_engine_default_cluster_parameters(
        self,
        request: RDSDescribeEngineDefaultClusterParametersRequest,
    ) -> RDSDescribeEngineDefaultClusterParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_engine_default_cluster_parameters, request, RDSDescribeEngineDefaultClusterParametersResponse)

    async def describe_engine_default_cluster_parameters_paginated(
        self,
        request: RDSDescribeEngineDefaultClusterParametersRequest,
    ) -> list[RDSDescribeEngineDefaultClusterParametersResponse]:
        return await self._paginate('describe_engine_default_cluster_parameters', request, RDSDescribeEngineDefaultClusterParametersResponse)

    async def describe_engine_default_parameters(
        self,
        request: RDSDescribeEngineDefaultParametersRequest,
    ) -> RDSDescribeEngineDefaultParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_engine_default_parameters, request, RDSDescribeEngineDefaultParametersResponse)

    async def describe_engine_default_parameters_paginated(
        self,
        request: RDSDescribeEngineDefaultParametersRequest,
    ) -> list[RDSDescribeEngineDefaultParametersResponse]:
        return await self._paginate('describe_engine_default_parameters', request, RDSDescribeEngineDefaultParametersResponse)

    async def describe_event_categories(
        self,
        request: RDSDescribeEventCategoriesRequest | None = None,
    ) -> RDSDescribeEventCategoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_categories, request, RDSDescribeEventCategoriesResponse)

    async def describe_event_subscriptions(
        self,
        request: RDSDescribeEventSubscriptionsRequest | None = None,
    ) -> RDSDescribeEventSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_subscriptions, request, RDSDescribeEventSubscriptionsResponse)

    async def describe_event_subscriptions_paginated(
        self,
        request: RDSDescribeEventSubscriptionsRequest | None = None,
    ) -> list[RDSDescribeEventSubscriptionsResponse]:
        return await self._paginate('describe_event_subscriptions', request, RDSDescribeEventSubscriptionsResponse)

    async def describe_events(
        self,
        request: RDSDescribeEventsRequest | None = None,
    ) -> RDSDescribeEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_events, request, RDSDescribeEventsResponse)

    async def describe_events_paginated(
        self,
        request: RDSDescribeEventsRequest | None = None,
    ) -> list[RDSDescribeEventsResponse]:
        return await self._paginate('describe_events', request, RDSDescribeEventsResponse)

    async def describe_export_tasks(
        self,
        request: RDSDescribeExportTasksRequest | None = None,
    ) -> RDSDescribeExportTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_export_tasks, request, RDSDescribeExportTasksResponse)

    async def describe_export_tasks_paginated(
        self,
        request: RDSDescribeExportTasksRequest | None = None,
    ) -> list[RDSDescribeExportTasksResponse]:
        return await self._paginate('describe_export_tasks', request, RDSDescribeExportTasksResponse)

    async def describe_global_clusters(
        self,
        request: RDSDescribeGlobalClustersRequest | None = None,
    ) -> RDSDescribeGlobalClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_clusters, request, RDSDescribeGlobalClustersResponse)

    async def describe_global_clusters_paginated(
        self,
        request: RDSDescribeGlobalClustersRequest | None = None,
    ) -> list[RDSDescribeGlobalClustersResponse]:
        return await self._paginate('describe_global_clusters', request, RDSDescribeGlobalClustersResponse)

    async def describe_integrations(
        self,
        request: RDSDescribeIntegrationsRequest | None = None,
    ) -> RDSDescribeIntegrationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_integrations, request, RDSDescribeIntegrationsResponse)

    async def describe_integrations_paginated(
        self,
        request: RDSDescribeIntegrationsRequest | None = None,
    ) -> list[RDSDescribeIntegrationsResponse]:
        return await self._paginate('describe_integrations', request, RDSDescribeIntegrationsResponse)

    async def describe_option_group_options(
        self,
        request: RDSDescribeOptionGroupOptionsRequest,
    ) -> RDSDescribeOptionGroupOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_option_group_options, request, RDSDescribeOptionGroupOptionsResponse)

    async def describe_option_group_options_paginated(
        self,
        request: RDSDescribeOptionGroupOptionsRequest,
    ) -> list[RDSDescribeOptionGroupOptionsResponse]:
        return await self._paginate('describe_option_group_options', request, RDSDescribeOptionGroupOptionsResponse)

    async def describe_option_groups(
        self,
        request: RDSDescribeOptionGroupsRequest | None = None,
    ) -> RDSDescribeOptionGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_option_groups, request, RDSDescribeOptionGroupsResponse)

    async def describe_option_groups_paginated(
        self,
        request: RDSDescribeOptionGroupsRequest | None = None,
    ) -> list[RDSDescribeOptionGroupsResponse]:
        return await self._paginate('describe_option_groups', request, RDSDescribeOptionGroupsResponse)

    async def describe_orderable_db_instance_options(
        self,
        request: RDSDescribeOrderableDBInstanceOptionsRequest,
    ) -> RDSDescribeOrderableDBInstanceOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_orderable_db_instance_options, request, RDSDescribeOrderableDBInstanceOptionsResponse)

    async def describe_orderable_db_instance_options_paginated(
        self,
        request: RDSDescribeOrderableDBInstanceOptionsRequest,
    ) -> list[RDSDescribeOrderableDBInstanceOptionsResponse]:
        return await self._paginate('describe_orderable_db_instance_options', request, RDSDescribeOrderableDBInstanceOptionsResponse)

    async def describe_pending_maintenance_actions(
        self,
        request: RDSDescribePendingMaintenanceActionsRequest | None = None,
    ) -> RDSDescribePendingMaintenanceActionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_pending_maintenance_actions, request, RDSDescribePendingMaintenanceActionsResponse)

    async def describe_pending_maintenance_actions_paginated(
        self,
        request: RDSDescribePendingMaintenanceActionsRequest | None = None,
    ) -> list[RDSDescribePendingMaintenanceActionsResponse]:
        return await self._paginate('describe_pending_maintenance_actions', request, RDSDescribePendingMaintenanceActionsResponse)

    async def describe_reserved_db_instances(
        self,
        request: RDSDescribeReservedDBInstancesRequest | None = None,
    ) -> RDSDescribeReservedDBInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_db_instances, request, RDSDescribeReservedDBInstancesResponse)

    async def describe_reserved_db_instances_paginated(
        self,
        request: RDSDescribeReservedDBInstancesRequest | None = None,
    ) -> list[RDSDescribeReservedDBInstancesResponse]:
        return await self._paginate('describe_reserved_db_instances', request, RDSDescribeReservedDBInstancesResponse)

    async def describe_reserved_db_instances_offerings(
        self,
        request: RDSDescribeReservedDBInstancesOfferingsRequest | None = None,
    ) -> RDSDescribeReservedDBInstancesOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_db_instances_offerings, request, RDSDescribeReservedDBInstancesOfferingsResponse)

    async def describe_reserved_db_instances_offerings_paginated(
        self,
        request: RDSDescribeReservedDBInstancesOfferingsRequest | None = None,
    ) -> list[RDSDescribeReservedDBInstancesOfferingsResponse]:
        return await self._paginate('describe_reserved_db_instances_offerings', request, RDSDescribeReservedDBInstancesOfferingsResponse)

    async def describe_serverless_v2_platform_versions(
        self,
        request: RDSDescribeServerlessV2PlatformVersionsRequest | None = None,
    ) -> RDSDescribeServerlessV2PlatformVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_serverless_v2_platform_versions, request, RDSDescribeServerlessV2PlatformVersionsResponse)

    async def describe_serverless_v2_platform_versions_paginated(
        self,
        request: RDSDescribeServerlessV2PlatformVersionsRequest | None = None,
    ) -> list[RDSDescribeServerlessV2PlatformVersionsResponse]:
        return await self._paginate('describe_serverless_v2_platform_versions', request, RDSDescribeServerlessV2PlatformVersionsResponse)

    async def describe_source_regions(
        self,
        request: RDSDescribeSourceRegionsRequest | None = None,
    ) -> RDSDescribeSourceRegionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_source_regions, request, RDSDescribeSourceRegionsResponse)

    async def describe_source_regions_paginated(
        self,
        request: RDSDescribeSourceRegionsRequest | None = None,
    ) -> list[RDSDescribeSourceRegionsResponse]:
        return await self._paginate('describe_source_regions', request, RDSDescribeSourceRegionsResponse)

    async def describe_tenant_databases(
        self,
        request: RDSDescribeTenantDatabasesRequest | None = None,
    ) -> RDSDescribeTenantDatabasesResponse:
        client = self._require_client()
        return await self._execute(client.describe_tenant_databases, request, RDSDescribeTenantDatabasesResponse)

    async def describe_tenant_databases_paginated(
        self,
        request: RDSDescribeTenantDatabasesRequest | None = None,
    ) -> list[RDSDescribeTenantDatabasesResponse]:
        return await self._paginate('describe_tenant_databases', request, RDSDescribeTenantDatabasesResponse)

    async def describe_valid_db_instance_modifications(
        self,
        request: RDSDescribeValidDBInstanceModificationsRequest,
    ) -> RDSDescribeValidDBInstanceModificationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_valid_db_instance_modifications, request, RDSDescribeValidDBInstanceModificationsResponse)

    async def disable_http_endpoint(
        self,
        request: RDSDisableHttpEndpointRequest,
    ) -> RDSDisableHttpEndpointResponse:
        client = self._require_client()
        return await self._execute(client.disable_http_endpoint, request, RDSDisableHttpEndpointResponse)

    async def download_db_log_file_portion(
        self,
        request: RDSDownloadDBLogFilePortionRequest,
    ) -> RDSDownloadDBLogFilePortionResponse:
        client = self._require_client()
        return await self._execute(client.download_db_log_file_portion, request, RDSDownloadDBLogFilePortionResponse)

    async def download_db_log_file_portion_paginated(
        self,
        request: RDSDownloadDBLogFilePortionRequest,
    ) -> list[RDSDownloadDBLogFilePortionResponse]:
        return await self._paginate('download_db_log_file_portion', request, RDSDownloadDBLogFilePortionResponse)

    async def enable_http_endpoint(
        self,
        request: RDSEnableHttpEndpointRequest,
    ) -> RDSEnableHttpEndpointResponse:
        client = self._require_client()
        return await self._execute(client.enable_http_endpoint, request, RDSEnableHttpEndpointResponse)

    async def failover_db_cluster(
        self,
        request: RDSFailoverDBClusterRequest,
    ) -> RDSFailoverDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.failover_db_cluster, request, RDSFailoverDBClusterResponse)

    async def failover_global_cluster(
        self,
        request: RDSFailoverGlobalClusterRequest,
    ) -> RDSFailoverGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.failover_global_cluster, request, RDSFailoverGlobalClusterResponse)

    async def modify_activity_stream(
        self,
        request: RDSModifyActivityStreamRequest | None = None,
    ) -> RDSModifyActivityStreamResponse:
        client = self._require_client()
        return await self._execute(client.modify_activity_stream, request, RDSModifyActivityStreamResponse)

    async def modify_certificates(
        self,
        request: RDSModifyCertificatesRequest | None = None,
    ) -> RDSModifyCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.modify_certificates, request, RDSModifyCertificatesResponse)

    async def modify_current_db_cluster_capacity(
        self,
        request: RDSModifyCurrentDBClusterCapacityRequest,
    ) -> RDSModifyCurrentDBClusterCapacityResponse:
        client = self._require_client()
        return await self._execute(client.modify_current_db_cluster_capacity, request, RDSModifyCurrentDBClusterCapacityResponse)

    async def modify_custom_db_engine_version(
        self,
        request: RDSModifyCustomDBEngineVersionRequest,
    ) -> RDSModifyCustomDBEngineVersionResponse:
        client = self._require_client()
        return await self._execute(client.modify_custom_db_engine_version, request, RDSModifyCustomDBEngineVersionResponse)

    async def modify_db_capacity_reservation(
        self,
        request: RDSModifyDBCapacityReservationRequest,
    ) -> RDSModifyDBCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_capacity_reservation, request, RDSModifyDBCapacityReservationResponse)

    async def modify_db_cluster_endpoint(
        self,
        request: RDSModifyDBClusterEndpointRequest,
    ) -> RDSModifyDBClusterEndpointResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster_endpoint, request, RDSModifyDBClusterEndpointResponse)

    async def modify_db_cluster_parameter_group(
        self,
        request: RDSModifyDBClusterParameterGroupRequest,
    ) -> RDSModifyDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster_parameter_group, request, RDSModifyDBClusterParameterGroupResponse)

    async def modify_db_cluster_snapshot_attribute(
        self,
        request: RDSModifyDBClusterSnapshotAttributeRequest,
    ) -> RDSModifyDBClusterSnapshotAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_cluster_snapshot_attribute, request, RDSModifyDBClusterSnapshotAttributeResponse)

    async def modify_db_parameter_group(
        self,
        request: RDSModifyDBParameterGroupRequest,
    ) -> RDSModifyDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_parameter_group, request, RDSModifyDBParameterGroupResponse)

    async def modify_db_proxy(
        self,
        request: RDSModifyDBProxyRequest,
    ) -> RDSModifyDBProxyResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_proxy, request, RDSModifyDBProxyResponse)

    async def modify_db_proxy_endpoint(
        self,
        request: RDSModifyDBProxyEndpointRequest,
    ) -> RDSModifyDBProxyEndpointResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_proxy_endpoint, request, RDSModifyDBProxyEndpointResponse)

    async def modify_db_proxy_target_group(
        self,
        request: RDSModifyDBProxyTargetGroupRequest,
    ) -> RDSModifyDBProxyTargetGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_proxy_target_group, request, RDSModifyDBProxyTargetGroupResponse)

    async def modify_db_recommendation(
        self,
        request: RDSModifyDBRecommendationRequest,
    ) -> RDSModifyDBRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_recommendation, request, RDSModifyDBRecommendationResponse)

    async def modify_db_shard_group(
        self,
        request: RDSModifyDBShardGroupRequest,
    ) -> RDSModifyDBShardGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_shard_group, request, RDSModifyDBShardGroupResponse)

    async def modify_db_snapshot(
        self,
        request: RDSModifyDBSnapshotRequest,
    ) -> RDSModifyDBSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_snapshot, request, RDSModifyDBSnapshotResponse)

    async def modify_db_snapshot_attribute(
        self,
        request: RDSModifyDBSnapshotAttributeRequest,
    ) -> RDSModifyDBSnapshotAttributeResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_snapshot_attribute, request, RDSModifyDBSnapshotAttributeResponse)

    async def modify_db_subnet_group(
        self,
        request: RDSModifyDBSubnetGroupRequest,
    ) -> RDSModifyDBSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_db_subnet_group, request, RDSModifyDBSubnetGroupResponse)

    async def modify_event_subscription(
        self,
        request: RDSModifyEventSubscriptionRequest,
    ) -> RDSModifyEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.modify_event_subscription, request, RDSModifyEventSubscriptionResponse)

    async def modify_global_cluster(
        self,
        request: RDSModifyGlobalClusterRequest,
    ) -> RDSModifyGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.modify_global_cluster, request, RDSModifyGlobalClusterResponse)

    async def modify_integration(
        self,
        request: RDSModifyIntegrationRequest,
    ) -> RDSModifyIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.modify_integration, request, RDSModifyIntegrationResponse)

    async def modify_option_group(
        self,
        request: RDSModifyOptionGroupRequest,
    ) -> RDSModifyOptionGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_option_group, request, RDSModifyOptionGroupResponse)

    async def modify_tenant_database(
        self,
        request: RDSModifyTenantDatabaseRequest,
    ) -> RDSModifyTenantDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.modify_tenant_database, request, RDSModifyTenantDatabaseResponse)

    async def promote_read_replica(
        self,
        request: RDSPromoteReadReplicaRequest,
    ) -> RDSPromoteReadReplicaResponse:
        client = self._require_client()
        return await self._execute(client.promote_read_replica, request, RDSPromoteReadReplicaResponse)

    async def promote_read_replica_db_cluster(
        self,
        request: RDSPromoteReadReplicaDBClusterRequest,
    ) -> RDSPromoteReadReplicaDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.promote_read_replica_db_cluster, request, RDSPromoteReadReplicaDBClusterResponse)

    async def purchase_reserved_db_instances_offering(
        self,
        request: RDSPurchaseReservedDBInstancesOfferingRequest,
    ) -> RDSPurchaseReservedDBInstancesOfferingResponse:
        client = self._require_client()
        return await self._execute(client.purchase_reserved_db_instances_offering, request, RDSPurchaseReservedDBInstancesOfferingResponse)

    async def reboot_db_cluster(
        self,
        request: RDSRebootDBClusterRequest,
    ) -> RDSRebootDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.reboot_db_cluster, request, RDSRebootDBClusterResponse)

    async def reboot_db_shard_group(
        self,
        request: RDSRebootDBShardGroupRequest,
    ) -> RDSRebootDBShardGroupResponse:
        client = self._require_client()
        return await self._execute(client.reboot_db_shard_group, request, RDSRebootDBShardGroupResponse)

    async def register_db_proxy_targets(
        self,
        request: RDSRegisterDBProxyTargetsRequest,
    ) -> RDSRegisterDBProxyTargetsResponse:
        client = self._require_client()
        return await self._execute(client.register_db_proxy_targets, request, RDSRegisterDBProxyTargetsResponse)

    async def remove_from_global_cluster(
        self,
        request: RDSRemoveFromGlobalClusterRequest,
    ) -> RDSRemoveFromGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.remove_from_global_cluster, request, RDSRemoveFromGlobalClusterResponse)

    async def remove_role_from_db_cluster(
        self,
        request: RDSRemoveRoleFromDBClusterRequest,
    ) -> RDSRemoveRoleFromDBClusterResponse:
        client = self._require_client()
        return await self._execute(client.remove_role_from_db_cluster, request, RDSRemoveRoleFromDBClusterResponse)

    async def remove_role_from_db_instance(
        self,
        request: RDSRemoveRoleFromDBInstanceRequest,
    ) -> RDSRemoveRoleFromDBInstanceResponse:
        client = self._require_client()
        return await self._execute(client.remove_role_from_db_instance, request, RDSRemoveRoleFromDBInstanceResponse)

    async def remove_source_identifier_from_subscription(
        self,
        request: RDSRemoveSourceIdentifierFromSubscriptionRequest,
    ) -> RDSRemoveSourceIdentifierFromSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.remove_source_identifier_from_subscription, request, RDSRemoveSourceIdentifierFromSubscriptionResponse)

    async def reset_db_cluster_parameter_group(
        self,
        request: RDSResetDBClusterParameterGroupRequest,
    ) -> RDSResetDBClusterParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.reset_db_cluster_parameter_group, request, RDSResetDBClusterParameterGroupResponse)

    async def reset_db_parameter_group(
        self,
        request: RDSResetDBParameterGroupRequest,
    ) -> RDSResetDBParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.reset_db_parameter_group, request, RDSResetDBParameterGroupResponse)

    async def restore_db_cluster_from_s3(
        self,
        request: RDSRestoreDBClusterFromS3Request,
    ) -> RDSRestoreDBClusterFromS3Response:
        client = self._require_client()
        return await self._execute(client.restore_db_cluster_from_s3, request, RDSRestoreDBClusterFromS3Response)

    async def restore_db_cluster_from_snapshot(
        self,
        request: RDSRestoreDBClusterFromSnapshotRequest,
    ) -> RDSRestoreDBClusterFromSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.restore_db_cluster_from_snapshot, request, RDSRestoreDBClusterFromSnapshotResponse)

    async def restore_db_cluster_to_point_in_time(
        self,
        request: RDSRestoreDBClusterToPointInTimeRequest,
    ) -> RDSRestoreDBClusterToPointInTimeResponse:
        client = self._require_client()
        return await self._execute(client.restore_db_cluster_to_point_in_time, request, RDSRestoreDBClusterToPointInTimeResponse)

    async def restore_db_instance_from_db_snapshot(
        self,
        request: RDSRestoreDBInstanceFromDBSnapshotRequest,
    ) -> RDSRestoreDBInstanceFromDBSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.restore_db_instance_from_db_snapshot, request, RDSRestoreDBInstanceFromDBSnapshotResponse)

    async def restore_db_instance_from_s3(
        self,
        request: RDSRestoreDBInstanceFromS3Request,
    ) -> RDSRestoreDBInstanceFromS3Response:
        client = self._require_client()
        return await self._execute(client.restore_db_instance_from_s3, request, RDSRestoreDBInstanceFromS3Response)

    async def restore_db_instance_to_point_in_time(
        self,
        request: RDSRestoreDBInstanceToPointInTimeRequest,
    ) -> RDSRestoreDBInstanceToPointInTimeResponse:
        client = self._require_client()
        return await self._execute(client.restore_db_instance_to_point_in_time, request, RDSRestoreDBInstanceToPointInTimeResponse)

    async def revoke_db_security_group_ingress(
        self,
        request: RDSRevokeDBSecurityGroupIngressRequest,
    ) -> RDSRevokeDBSecurityGroupIngressResponse:
        client = self._require_client()
        return await self._execute(client.revoke_db_security_group_ingress, request, RDSRevokeDBSecurityGroupIngressResponse)

    async def start_activity_stream(
        self,
        request: RDSStartActivityStreamRequest,
    ) -> RDSStartActivityStreamResponse:
        client = self._require_client()
        return await self._execute(client.start_activity_stream, request, RDSStartActivityStreamResponse)

    async def start_db_instance_automated_backups_replication(
        self,
        request: RDSStartDBInstanceAutomatedBackupsReplicationRequest,
    ) -> RDSStartDBInstanceAutomatedBackupsReplicationResponse:
        client = self._require_client()
        return await self._execute(client.start_db_instance_automated_backups_replication, request, RDSStartDBInstanceAutomatedBackupsReplicationResponse)

    async def start_export_task(
        self,
        request: RDSStartExportTaskRequest,
    ) -> RDSStartExportTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_export_task, request, RDSStartExportTaskResponse)

    async def stop_activity_stream(
        self,
        request: RDSStopActivityStreamRequest,
    ) -> RDSStopActivityStreamResponse:
        client = self._require_client()
        return await self._execute(client.stop_activity_stream, request, RDSStopActivityStreamResponse)

    async def stop_db_instance_automated_backups_replication(
        self,
        request: RDSStopDBInstanceAutomatedBackupsReplicationRequest,
    ) -> RDSStopDBInstanceAutomatedBackupsReplicationResponse:
        client = self._require_client()
        return await self._execute(client.stop_db_instance_automated_backups_replication, request, RDSStopDBInstanceAutomatedBackupsReplicationResponse)

    async def switchover_blue_green_deployment(
        self,
        request: RDSSwitchoverBlueGreenDeploymentRequest,
    ) -> RDSSwitchoverBlueGreenDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.switchover_blue_green_deployment, request, RDSSwitchoverBlueGreenDeploymentResponse)

    async def switchover_global_cluster(
        self,
        request: RDSSwitchoverGlobalClusterRequest,
    ) -> RDSSwitchoverGlobalClusterResponse:
        client = self._require_client()
        return await self._execute(client.switchover_global_cluster, request, RDSSwitchoverGlobalClusterResponse)

    async def switchover_read_replica(
        self,
        request: RDSSwitchoverReadReplicaRequest,
    ) -> RDSSwitchoverReadReplicaResponse:
        client = self._require_client()
        return await self._execute(client.switchover_read_replica, request, RDSSwitchoverReadReplicaResponse)

