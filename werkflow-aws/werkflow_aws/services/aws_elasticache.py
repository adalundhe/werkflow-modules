from werkflow_aws.models.elasticache import (
    ElasticacheCacheClusterResponse,
    ElasticacheCreateCacheClusterRequest,
    ElasticacheCreateReplicationGroupRequest,
    ElasticacheCreateSnapshotRequest,
    ElasticacheDeleteCacheClusterRequest,
    ElasticacheDeleteReplicationGroupRequest,
    ElasticacheDeleteSnapshotRequest,
    ElasticacheDescribeCacheClustersRequest,
    ElasticacheDescribeCacheClustersResponse,
    ElasticacheDescribeReplicationGroupsRequest,
    ElasticacheDescribeReplicationGroupsResponse,
    ElasticacheDescribeSnapshotsRequest,
    ElasticacheDescribeSnapshotsResponse,
    ElasticacheModifyCacheClusterRequest,
    ElasticacheModifyReplicationGroupRequest,
    ElasticacheRebootCacheClusterRequest,
    ElasticacheReplicationGroupResponse,
    ElasticacheSnapshotResponse,
)
from werkflow_aws.types import ElastiCacheClient
from .base import AWSBaseService
from werkflow_aws.models.elasticache import (
    ElastiCacheAddTagsToResourceRequest,
    ElastiCacheAddTagsToResourceResponse,
    ElastiCacheAuthorizeCacheSecurityGroupIngressRequest,
    ElastiCacheAuthorizeCacheSecurityGroupIngressResponse,
    ElastiCacheBatchApplyUpdateActionRequest,
    ElastiCacheBatchApplyUpdateActionResponse,
    ElastiCacheBatchStopUpdateActionRequest,
    ElastiCacheBatchStopUpdateActionResponse,
    ElastiCacheCompleteMigrationRequest,
    ElastiCacheCompleteMigrationResponse,
    ElastiCacheCopyServerlessCacheSnapshotRequest,
    ElastiCacheCopyServerlessCacheSnapshotResponse,
    ElastiCacheCopySnapshotRequest,
    ElastiCacheCopySnapshotResponse,
    ElastiCacheCreateCacheParameterGroupRequest,
    ElastiCacheCreateCacheParameterGroupResponse,
    ElastiCacheCreateCacheSecurityGroupRequest,
    ElastiCacheCreateCacheSecurityGroupResponse,
    ElastiCacheCreateCacheSubnetGroupRequest,
    ElastiCacheCreateCacheSubnetGroupResponse,
    ElastiCacheCreateGlobalReplicationGroupRequest,
    ElastiCacheCreateGlobalReplicationGroupResponse,
    ElastiCacheCreateServerlessCacheRequest,
    ElastiCacheCreateServerlessCacheResponse,
    ElastiCacheCreateServerlessCacheSnapshotRequest,
    ElastiCacheCreateServerlessCacheSnapshotResponse,
    ElastiCacheCreateUserGroupRequest,
    ElastiCacheCreateUserGroupResponse,
    ElastiCacheCreateUserRequest,
    ElastiCacheCreateUserResponse,
    ElastiCacheDecreaseNodeGroupsInGlobalReplicationGroupRequest,
    ElastiCacheDecreaseNodeGroupsInGlobalReplicationGroupResponse,
    ElastiCacheDecreaseReplicaCountRequest,
    ElastiCacheDecreaseReplicaCountResponse,
    ElastiCacheDeleteCacheParameterGroupRequest,
    ElastiCacheDeleteCacheParameterGroupResponse,
    ElastiCacheDeleteCacheSecurityGroupRequest,
    ElastiCacheDeleteCacheSecurityGroupResponse,
    ElastiCacheDeleteCacheSubnetGroupRequest,
    ElastiCacheDeleteCacheSubnetGroupResponse,
    ElastiCacheDeleteGlobalReplicationGroupRequest,
    ElastiCacheDeleteGlobalReplicationGroupResponse,
    ElastiCacheDeleteServerlessCacheRequest,
    ElastiCacheDeleteServerlessCacheResponse,
    ElastiCacheDeleteServerlessCacheSnapshotRequest,
    ElastiCacheDeleteServerlessCacheSnapshotResponse,
    ElastiCacheDeleteUserGroupRequest,
    ElastiCacheDeleteUserGroupResponse,
    ElastiCacheDeleteUserRequest,
    ElastiCacheDeleteUserResponse,
    ElastiCacheDescribeCacheEngineVersionsRequest,
    ElastiCacheDescribeCacheEngineVersionsResponse,
    ElastiCacheDescribeCacheParameterGroupsRequest,
    ElastiCacheDescribeCacheParameterGroupsResponse,
    ElastiCacheDescribeCacheParametersRequest,
    ElastiCacheDescribeCacheParametersResponse,
    ElastiCacheDescribeCacheSecurityGroupsRequest,
    ElastiCacheDescribeCacheSecurityGroupsResponse,
    ElastiCacheDescribeCacheSubnetGroupsRequest,
    ElastiCacheDescribeCacheSubnetGroupsResponse,
    ElastiCacheDescribeEngineDefaultParametersRequest,
    ElastiCacheDescribeEngineDefaultParametersResponse,
    ElastiCacheDescribeEventsRequest,
    ElastiCacheDescribeEventsResponse,
    ElastiCacheDescribeGlobalReplicationGroupsRequest,
    ElastiCacheDescribeGlobalReplicationGroupsResponse,
    ElastiCacheDescribeReservedCacheNodesOfferingsRequest,
    ElastiCacheDescribeReservedCacheNodesOfferingsResponse,
    ElastiCacheDescribeReservedCacheNodesRequest,
    ElastiCacheDescribeReservedCacheNodesResponse,
    ElastiCacheDescribeServerlessCacheSnapshotsRequest,
    ElastiCacheDescribeServerlessCacheSnapshotsResponse,
    ElastiCacheDescribeServerlessCachesRequest,
    ElastiCacheDescribeServerlessCachesResponse,
    ElastiCacheDescribeServiceUpdatesRequest,
    ElastiCacheDescribeServiceUpdatesResponse,
    ElastiCacheDescribeUpdateActionsRequest,
    ElastiCacheDescribeUpdateActionsResponse,
    ElastiCacheDescribeUserGroupsRequest,
    ElastiCacheDescribeUserGroupsResponse,
    ElastiCacheDescribeUsersRequest,
    ElastiCacheDescribeUsersResponse,
    ElastiCacheDisassociateGlobalReplicationGroupRequest,
    ElastiCacheDisassociateGlobalReplicationGroupResponse,
    ElastiCacheExportServerlessCacheSnapshotRequest,
    ElastiCacheExportServerlessCacheSnapshotResponse,
    ElastiCacheFailoverGlobalReplicationGroupRequest,
    ElastiCacheFailoverGlobalReplicationGroupResponse,
    ElastiCacheIncreaseNodeGroupsInGlobalReplicationGroupRequest,
    ElastiCacheIncreaseNodeGroupsInGlobalReplicationGroupResponse,
    ElastiCacheIncreaseReplicaCountRequest,
    ElastiCacheIncreaseReplicaCountResponse,
    ElastiCacheListAllowedNodeTypeModificationsRequest,
    ElastiCacheListAllowedNodeTypeModificationsResponse,
    ElastiCacheListTagsForResourceRequest,
    ElastiCacheListTagsForResourceResponse,
    ElastiCacheModifyCacheParameterGroupRequest,
    ElastiCacheModifyCacheParameterGroupResponse,
    ElastiCacheModifyCacheSubnetGroupRequest,
    ElastiCacheModifyCacheSubnetGroupResponse,
    ElastiCacheModifyGlobalReplicationGroupRequest,
    ElastiCacheModifyGlobalReplicationGroupResponse,
    ElastiCacheModifyReplicationGroupShardConfigurationRequest,
    ElastiCacheModifyReplicationGroupShardConfigurationResponse,
    ElastiCacheModifyServerlessCacheRequest,
    ElastiCacheModifyServerlessCacheResponse,
    ElastiCacheModifyUserGroupRequest,
    ElastiCacheModifyUserGroupResponse,
    ElastiCacheModifyUserRequest,
    ElastiCacheModifyUserResponse,
    ElastiCachePrepareMigrationRequest,
    ElastiCachePrepareMigrationResponse,
    ElastiCachePurchaseReservedCacheNodesOfferingRequest,
    ElastiCachePurchaseReservedCacheNodesOfferingResponse,
    ElastiCacheRebalanceSlotsInGlobalReplicationGroupRequest,
    ElastiCacheRebalanceSlotsInGlobalReplicationGroupResponse,
    ElastiCacheRemoveTagsFromResourceRequest,
    ElastiCacheRemoveTagsFromResourceResponse,
    ElastiCacheResetCacheParameterGroupRequest,
    ElastiCacheResetCacheParameterGroupResponse,
    ElastiCacheRevokeCacheSecurityGroupIngressRequest,
    ElastiCacheRevokeCacheSecurityGroupIngressResponse,
    ElastiCacheStartMigrationRequest,
    ElastiCacheStartMigrationResponse,
    ElastiCacheStopMigrationRequest,
    ElastiCacheStopMigrationResponse,
    ElastiCacheTestFailoverRequest,
    ElastiCacheTestFailoverResponse,
    ElastiCacheTestMigrationRequest,
    ElastiCacheTestMigrationResponse,
)


class AWSElastiCache(AWSBaseService[ElastiCacheClient]):
    service_name = 'ElastiCache'
    boto3_service_name = 'elasticache'

    def __init__(self) -> None:
        super().__init__(
            service_name='ElastiCache',
            boto3_service_name='elasticache',
        )

    async def describe_cache_clusters(
        self,
        request: ElasticacheDescribeCacheClustersRequest | None = None,
    ) -> ElasticacheDescribeCacheClustersResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_cache_clusters,
            request or ElasticacheDescribeCacheClustersRequest(),
            ElasticacheDescribeCacheClustersResponse,
        )

    async def describe_cache_clusters_paginated(
        self,
        request: ElasticacheDescribeCacheClustersRequest | None = None,
    ) -> list[ElasticacheDescribeCacheClustersResponse]:
        return await self._paginate(
            'describe_cache_clusters',
            request or ElasticacheDescribeCacheClustersRequest(),
            ElasticacheDescribeCacheClustersResponse,
        )

    async def describe_replication_groups(
        self,
        request: ElasticacheDescribeReplicationGroupsRequest | None = None,
    ) -> ElasticacheDescribeReplicationGroupsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_replication_groups,
            request or ElasticacheDescribeReplicationGroupsRequest(),
            ElasticacheDescribeReplicationGroupsResponse,
        )

    async def describe_replication_groups_paginated(
        self,
        request: ElasticacheDescribeReplicationGroupsRequest | None = None,
    ) -> list[ElasticacheDescribeReplicationGroupsResponse]:
        return await self._paginate(
            'describe_replication_groups',
            request or ElasticacheDescribeReplicationGroupsRequest(),
            ElasticacheDescribeReplicationGroupsResponse,
        )

    async def create_cache_cluster(
        self,
        request: ElasticacheCreateCacheClusterRequest,
    ) -> ElasticacheCacheClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.create_cache_cluster,
            request,
            ElasticacheCacheClusterResponse,
        )

    async def delete_cache_cluster(
        self,
        request: ElasticacheDeleteCacheClusterRequest,
    ) -> ElasticacheCacheClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_cache_cluster,
            request,
            ElasticacheCacheClusterResponse,
        )

    async def modify_cache_cluster(
        self,
        request: ElasticacheModifyCacheClusterRequest,
    ) -> ElasticacheCacheClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.modify_cache_cluster,
            request,
            ElasticacheCacheClusterResponse,
        )

    async def reboot_cache_cluster(
        self,
        request: ElasticacheRebootCacheClusterRequest,
    ) -> ElasticacheCacheClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.reboot_cache_cluster,
            request,
            ElasticacheCacheClusterResponse,
        )

    async def create_replication_group(
        self,
        request: ElasticacheCreateReplicationGroupRequest,
    ) -> ElasticacheReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.create_replication_group,
            request,
            ElasticacheReplicationGroupResponse,
        )

    async def delete_replication_group(
        self,
        request: ElasticacheDeleteReplicationGroupRequest,
    ) -> ElasticacheReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_replication_group,
            request,
            ElasticacheReplicationGroupResponse,
        )

    async def modify_replication_group(
        self,
        request: ElasticacheModifyReplicationGroupRequest,
    ) -> ElasticacheReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(
            client.modify_replication_group,
            request,
            ElasticacheReplicationGroupResponse,
        )

    async def describe_snapshots(
        self,
        request: ElasticacheDescribeSnapshotsRequest | None = None,
    ) -> ElasticacheDescribeSnapshotsResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_snapshots,
            request or ElasticacheDescribeSnapshotsRequest(),
            ElasticacheDescribeSnapshotsResponse,
        )

    async def describe_snapshots_paginated(
        self,
        request: ElasticacheDescribeSnapshotsRequest | None = None,
    ) -> list[ElasticacheDescribeSnapshotsResponse]:
        return await self._paginate(
            'describe_snapshots',
            request or ElasticacheDescribeSnapshotsRequest(),
            ElasticacheDescribeSnapshotsResponse,
        )

    async def create_snapshot(
        self,
        request: ElasticacheCreateSnapshotRequest,
    ) -> ElasticacheSnapshotResponse:
        client = self._require_client()
        return await self._execute(
            client.create_snapshot,
            request,
            ElasticacheSnapshotResponse,
        )

    async def delete_snapshot(
        self,
        request: ElasticacheDeleteSnapshotRequest,
    ) -> ElasticacheSnapshotResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_snapshot,
            request,
            ElasticacheSnapshotResponse,
        )

    async def add_tags_to_resource(
        self,
        request: ElastiCacheAddTagsToResourceRequest,
    ) -> ElastiCacheAddTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_resource, request, ElastiCacheAddTagsToResourceResponse)

    async def authorize_cache_security_group_ingress(
        self,
        request: ElastiCacheAuthorizeCacheSecurityGroupIngressRequest,
    ) -> ElastiCacheAuthorizeCacheSecurityGroupIngressResponse:
        client = self._require_client()
        return await self._execute(client.authorize_cache_security_group_ingress, request, ElastiCacheAuthorizeCacheSecurityGroupIngressResponse)

    async def batch_apply_update_action(
        self,
        request: ElastiCacheBatchApplyUpdateActionRequest,
    ) -> ElastiCacheBatchApplyUpdateActionResponse:
        client = self._require_client()
        return await self._execute(client.batch_apply_update_action, request, ElastiCacheBatchApplyUpdateActionResponse)

    async def batch_stop_update_action(
        self,
        request: ElastiCacheBatchStopUpdateActionRequest,
    ) -> ElastiCacheBatchStopUpdateActionResponse:
        client = self._require_client()
        return await self._execute(client.batch_stop_update_action, request, ElastiCacheBatchStopUpdateActionResponse)

    async def complete_migration(
        self,
        request: ElastiCacheCompleteMigrationRequest | None = None,
    ) -> ElastiCacheCompleteMigrationResponse:
        client = self._require_client()
        return await self._execute(client.complete_migration, request, ElastiCacheCompleteMigrationResponse)

    async def copy_serverless_cache_snapshot(
        self,
        request: ElastiCacheCopyServerlessCacheSnapshotRequest,
    ) -> ElastiCacheCopyServerlessCacheSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_serverless_cache_snapshot, request, ElastiCacheCopyServerlessCacheSnapshotResponse)

    async def copy_snapshot(
        self,
        request: ElastiCacheCopySnapshotRequest,
    ) -> ElastiCacheCopySnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_snapshot, request, ElastiCacheCopySnapshotResponse)

    async def create_cache_parameter_group(
        self,
        request: ElastiCacheCreateCacheParameterGroupRequest,
    ) -> ElastiCacheCreateCacheParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_cache_parameter_group, request, ElastiCacheCreateCacheParameterGroupResponse)

    async def create_cache_security_group(
        self,
        request: ElastiCacheCreateCacheSecurityGroupRequest,
    ) -> ElastiCacheCreateCacheSecurityGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_cache_security_group, request, ElastiCacheCreateCacheSecurityGroupResponse)

    async def create_cache_subnet_group(
        self,
        request: ElastiCacheCreateCacheSubnetGroupRequest,
    ) -> ElastiCacheCreateCacheSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_cache_subnet_group, request, ElastiCacheCreateCacheSubnetGroupResponse)

    async def create_global_replication_group(
        self,
        request: ElastiCacheCreateGlobalReplicationGroupRequest,
    ) -> ElastiCacheCreateGlobalReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_global_replication_group, request, ElastiCacheCreateGlobalReplicationGroupResponse)

    async def create_serverless_cache(
        self,
        request: ElastiCacheCreateServerlessCacheRequest,
    ) -> ElastiCacheCreateServerlessCacheResponse:
        client = self._require_client()
        return await self._execute(client.create_serverless_cache, request, ElastiCacheCreateServerlessCacheResponse)

    async def create_serverless_cache_snapshot(
        self,
        request: ElastiCacheCreateServerlessCacheSnapshotRequest,
    ) -> ElastiCacheCreateServerlessCacheSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_serverless_cache_snapshot, request, ElastiCacheCreateServerlessCacheSnapshotResponse)

    async def create_user(
        self,
        request: ElastiCacheCreateUserRequest,
    ) -> ElastiCacheCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, ElastiCacheCreateUserResponse)

    async def create_user_group(
        self,
        request: ElastiCacheCreateUserGroupRequest,
    ) -> ElastiCacheCreateUserGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_user_group, request, ElastiCacheCreateUserGroupResponse)

    async def decrease_node_groups_in_global_replication_group(
        self,
        request: ElastiCacheDecreaseNodeGroupsInGlobalReplicationGroupRequest,
    ) -> ElastiCacheDecreaseNodeGroupsInGlobalReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(client.decrease_node_groups_in_global_replication_group, request, ElastiCacheDecreaseNodeGroupsInGlobalReplicationGroupResponse)

    async def decrease_replica_count(
        self,
        request: ElastiCacheDecreaseReplicaCountRequest,
    ) -> ElastiCacheDecreaseReplicaCountResponse:
        client = self._require_client()
        return await self._execute(client.decrease_replica_count, request, ElastiCacheDecreaseReplicaCountResponse)

    async def delete_cache_parameter_group(
        self,
        request: ElastiCacheDeleteCacheParameterGroupRequest,
    ) -> ElastiCacheDeleteCacheParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_cache_parameter_group, request, ElastiCacheDeleteCacheParameterGroupResponse)

    async def delete_cache_security_group(
        self,
        request: ElastiCacheDeleteCacheSecurityGroupRequest,
    ) -> ElastiCacheDeleteCacheSecurityGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_cache_security_group, request, ElastiCacheDeleteCacheSecurityGroupResponse)

    async def delete_cache_subnet_group(
        self,
        request: ElastiCacheDeleteCacheSubnetGroupRequest,
    ) -> ElastiCacheDeleteCacheSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_cache_subnet_group, request, ElastiCacheDeleteCacheSubnetGroupResponse)

    async def delete_global_replication_group(
        self,
        request: ElastiCacheDeleteGlobalReplicationGroupRequest,
    ) -> ElastiCacheDeleteGlobalReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_global_replication_group, request, ElastiCacheDeleteGlobalReplicationGroupResponse)

    async def delete_serverless_cache(
        self,
        request: ElastiCacheDeleteServerlessCacheRequest,
    ) -> ElastiCacheDeleteServerlessCacheResponse:
        client = self._require_client()
        return await self._execute(client.delete_serverless_cache, request, ElastiCacheDeleteServerlessCacheResponse)

    async def delete_serverless_cache_snapshot(
        self,
        request: ElastiCacheDeleteServerlessCacheSnapshotRequest,
    ) -> ElastiCacheDeleteServerlessCacheSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_serverless_cache_snapshot, request, ElastiCacheDeleteServerlessCacheSnapshotResponse)

    async def delete_user(
        self,
        request: ElastiCacheDeleteUserRequest,
    ) -> ElastiCacheDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, ElastiCacheDeleteUserResponse)

    async def delete_user_group(
        self,
        request: ElastiCacheDeleteUserGroupRequest,
    ) -> ElastiCacheDeleteUserGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_group, request, ElastiCacheDeleteUserGroupResponse)

    async def describe_cache_engine_versions(
        self,
        request: ElastiCacheDescribeCacheEngineVersionsRequest | None = None,
    ) -> ElastiCacheDescribeCacheEngineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cache_engine_versions, request, ElastiCacheDescribeCacheEngineVersionsResponse)

    async def describe_cache_engine_versions_paginated(
        self,
        request: ElastiCacheDescribeCacheEngineVersionsRequest | None = None,
    ) -> list[ElastiCacheDescribeCacheEngineVersionsResponse]:
        return await self._paginate('describe_cache_engine_versions', request, ElastiCacheDescribeCacheEngineVersionsResponse)

    async def describe_cache_parameter_groups(
        self,
        request: ElastiCacheDescribeCacheParameterGroupsRequest | None = None,
    ) -> ElastiCacheDescribeCacheParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cache_parameter_groups, request, ElastiCacheDescribeCacheParameterGroupsResponse)

    async def describe_cache_parameter_groups_paginated(
        self,
        request: ElastiCacheDescribeCacheParameterGroupsRequest | None = None,
    ) -> list[ElastiCacheDescribeCacheParameterGroupsResponse]:
        return await self._paginate('describe_cache_parameter_groups', request, ElastiCacheDescribeCacheParameterGroupsResponse)

    async def describe_cache_parameters(
        self,
        request: ElastiCacheDescribeCacheParametersRequest,
    ) -> ElastiCacheDescribeCacheParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_cache_parameters, request, ElastiCacheDescribeCacheParametersResponse)

    async def describe_cache_parameters_paginated(
        self,
        request: ElastiCacheDescribeCacheParametersRequest,
    ) -> list[ElastiCacheDescribeCacheParametersResponse]:
        return await self._paginate('describe_cache_parameters', request, ElastiCacheDescribeCacheParametersResponse)

    async def describe_cache_security_groups(
        self,
        request: ElastiCacheDescribeCacheSecurityGroupsRequest | None = None,
    ) -> ElastiCacheDescribeCacheSecurityGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cache_security_groups, request, ElastiCacheDescribeCacheSecurityGroupsResponse)

    async def describe_cache_security_groups_paginated(
        self,
        request: ElastiCacheDescribeCacheSecurityGroupsRequest | None = None,
    ) -> list[ElastiCacheDescribeCacheSecurityGroupsResponse]:
        return await self._paginate('describe_cache_security_groups', request, ElastiCacheDescribeCacheSecurityGroupsResponse)

    async def describe_cache_subnet_groups(
        self,
        request: ElastiCacheDescribeCacheSubnetGroupsRequest | None = None,
    ) -> ElastiCacheDescribeCacheSubnetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_cache_subnet_groups, request, ElastiCacheDescribeCacheSubnetGroupsResponse)

    async def describe_cache_subnet_groups_paginated(
        self,
        request: ElastiCacheDescribeCacheSubnetGroupsRequest | None = None,
    ) -> list[ElastiCacheDescribeCacheSubnetGroupsResponse]:
        return await self._paginate('describe_cache_subnet_groups', request, ElastiCacheDescribeCacheSubnetGroupsResponse)

    async def describe_engine_default_parameters(
        self,
        request: ElastiCacheDescribeEngineDefaultParametersRequest,
    ) -> ElastiCacheDescribeEngineDefaultParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_engine_default_parameters, request, ElastiCacheDescribeEngineDefaultParametersResponse)

    async def describe_engine_default_parameters_paginated(
        self,
        request: ElastiCacheDescribeEngineDefaultParametersRequest,
    ) -> list[ElastiCacheDescribeEngineDefaultParametersResponse]:
        return await self._paginate('describe_engine_default_parameters', request, ElastiCacheDescribeEngineDefaultParametersResponse)

    async def describe_events(
        self,
        request: ElastiCacheDescribeEventsRequest | None = None,
    ) -> ElastiCacheDescribeEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_events, request, ElastiCacheDescribeEventsResponse)

    async def describe_events_paginated(
        self,
        request: ElastiCacheDescribeEventsRequest | None = None,
    ) -> list[ElastiCacheDescribeEventsResponse]:
        return await self._paginate('describe_events', request, ElastiCacheDescribeEventsResponse)

    async def describe_global_replication_groups(
        self,
        request: ElastiCacheDescribeGlobalReplicationGroupsRequest | None = None,
    ) -> ElastiCacheDescribeGlobalReplicationGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_replication_groups, request, ElastiCacheDescribeGlobalReplicationGroupsResponse)

    async def describe_global_replication_groups_paginated(
        self,
        request: ElastiCacheDescribeGlobalReplicationGroupsRequest | None = None,
    ) -> list[ElastiCacheDescribeGlobalReplicationGroupsResponse]:
        return await self._paginate('describe_global_replication_groups', request, ElastiCacheDescribeGlobalReplicationGroupsResponse)

    async def describe_reserved_cache_nodes(
        self,
        request: ElastiCacheDescribeReservedCacheNodesRequest | None = None,
    ) -> ElastiCacheDescribeReservedCacheNodesResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_cache_nodes, request, ElastiCacheDescribeReservedCacheNodesResponse)

    async def describe_reserved_cache_nodes_paginated(
        self,
        request: ElastiCacheDescribeReservedCacheNodesRequest | None = None,
    ) -> list[ElastiCacheDescribeReservedCacheNodesResponse]:
        return await self._paginate('describe_reserved_cache_nodes', request, ElastiCacheDescribeReservedCacheNodesResponse)

    async def describe_reserved_cache_nodes_offerings(
        self,
        request: ElastiCacheDescribeReservedCacheNodesOfferingsRequest | None = None,
    ) -> ElastiCacheDescribeReservedCacheNodesOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_cache_nodes_offerings, request, ElastiCacheDescribeReservedCacheNodesOfferingsResponse)

    async def describe_reserved_cache_nodes_offerings_paginated(
        self,
        request: ElastiCacheDescribeReservedCacheNodesOfferingsRequest | None = None,
    ) -> list[ElastiCacheDescribeReservedCacheNodesOfferingsResponse]:
        return await self._paginate('describe_reserved_cache_nodes_offerings', request, ElastiCacheDescribeReservedCacheNodesOfferingsResponse)

    async def describe_serverless_cache_snapshots(
        self,
        request: ElastiCacheDescribeServerlessCacheSnapshotsRequest | None = None,
    ) -> ElastiCacheDescribeServerlessCacheSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_serverless_cache_snapshots, request, ElastiCacheDescribeServerlessCacheSnapshotsResponse)

    async def describe_serverless_cache_snapshots_paginated(
        self,
        request: ElastiCacheDescribeServerlessCacheSnapshotsRequest | None = None,
    ) -> list[ElastiCacheDescribeServerlessCacheSnapshotsResponse]:
        return await self._paginate('describe_serverless_cache_snapshots', request, ElastiCacheDescribeServerlessCacheSnapshotsResponse)

    async def describe_serverless_caches(
        self,
        request: ElastiCacheDescribeServerlessCachesRequest | None = None,
    ) -> ElastiCacheDescribeServerlessCachesResponse:
        client = self._require_client()
        return await self._execute(client.describe_serverless_caches, request, ElastiCacheDescribeServerlessCachesResponse)

    async def describe_serverless_caches_paginated(
        self,
        request: ElastiCacheDescribeServerlessCachesRequest | None = None,
    ) -> list[ElastiCacheDescribeServerlessCachesResponse]:
        return await self._paginate('describe_serverless_caches', request, ElastiCacheDescribeServerlessCachesResponse)

    async def describe_service_updates(
        self,
        request: ElastiCacheDescribeServiceUpdatesRequest | None = None,
    ) -> ElastiCacheDescribeServiceUpdatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_updates, request, ElastiCacheDescribeServiceUpdatesResponse)

    async def describe_service_updates_paginated(
        self,
        request: ElastiCacheDescribeServiceUpdatesRequest | None = None,
    ) -> list[ElastiCacheDescribeServiceUpdatesResponse]:
        return await self._paginate('describe_service_updates', request, ElastiCacheDescribeServiceUpdatesResponse)

    async def describe_update_actions(
        self,
        request: ElastiCacheDescribeUpdateActionsRequest | None = None,
    ) -> ElastiCacheDescribeUpdateActionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_update_actions, request, ElastiCacheDescribeUpdateActionsResponse)

    async def describe_update_actions_paginated(
        self,
        request: ElastiCacheDescribeUpdateActionsRequest | None = None,
    ) -> list[ElastiCacheDescribeUpdateActionsResponse]:
        return await self._paginate('describe_update_actions', request, ElastiCacheDescribeUpdateActionsResponse)

    async def describe_user_groups(
        self,
        request: ElastiCacheDescribeUserGroupsRequest | None = None,
    ) -> ElastiCacheDescribeUserGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_groups, request, ElastiCacheDescribeUserGroupsResponse)

    async def describe_user_groups_paginated(
        self,
        request: ElastiCacheDescribeUserGroupsRequest | None = None,
    ) -> list[ElastiCacheDescribeUserGroupsResponse]:
        return await self._paginate('describe_user_groups', request, ElastiCacheDescribeUserGroupsResponse)

    async def describe_users(
        self,
        request: ElastiCacheDescribeUsersRequest | None = None,
    ) -> ElastiCacheDescribeUsersResponse:
        client = self._require_client()
        return await self._execute(client.describe_users, request, ElastiCacheDescribeUsersResponse)

    async def describe_users_paginated(
        self,
        request: ElastiCacheDescribeUsersRequest | None = None,
    ) -> list[ElastiCacheDescribeUsersResponse]:
        return await self._paginate('describe_users', request, ElastiCacheDescribeUsersResponse)

    async def disassociate_global_replication_group(
        self,
        request: ElastiCacheDisassociateGlobalReplicationGroupRequest,
    ) -> ElastiCacheDisassociateGlobalReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_global_replication_group, request, ElastiCacheDisassociateGlobalReplicationGroupResponse)

    async def export_serverless_cache_snapshot(
        self,
        request: ElastiCacheExportServerlessCacheSnapshotRequest,
    ) -> ElastiCacheExportServerlessCacheSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.export_serverless_cache_snapshot, request, ElastiCacheExportServerlessCacheSnapshotResponse)

    async def failover_global_replication_group(
        self,
        request: ElastiCacheFailoverGlobalReplicationGroupRequest,
    ) -> ElastiCacheFailoverGlobalReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(client.failover_global_replication_group, request, ElastiCacheFailoverGlobalReplicationGroupResponse)

    async def increase_node_groups_in_global_replication_group(
        self,
        request: ElastiCacheIncreaseNodeGroupsInGlobalReplicationGroupRequest,
    ) -> ElastiCacheIncreaseNodeGroupsInGlobalReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(client.increase_node_groups_in_global_replication_group, request, ElastiCacheIncreaseNodeGroupsInGlobalReplicationGroupResponse)

    async def increase_replica_count(
        self,
        request: ElastiCacheIncreaseReplicaCountRequest,
    ) -> ElastiCacheIncreaseReplicaCountResponse:
        client = self._require_client()
        return await self._execute(client.increase_replica_count, request, ElastiCacheIncreaseReplicaCountResponse)

    async def list_allowed_node_type_modifications(
        self,
        request: ElastiCacheListAllowedNodeTypeModificationsRequest | None = None,
    ) -> ElastiCacheListAllowedNodeTypeModificationsResponse:
        client = self._require_client()
        return await self._execute(client.list_allowed_node_type_modifications, request, ElastiCacheListAllowedNodeTypeModificationsResponse)

    async def list_tags_for_resource(
        self,
        request: ElastiCacheListTagsForResourceRequest,
    ) -> ElastiCacheListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ElastiCacheListTagsForResourceResponse)

    async def modify_cache_parameter_group(
        self,
        request: ElastiCacheModifyCacheParameterGroupRequest,
    ) -> ElastiCacheModifyCacheParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_cache_parameter_group, request, ElastiCacheModifyCacheParameterGroupResponse)

    async def modify_cache_subnet_group(
        self,
        request: ElastiCacheModifyCacheSubnetGroupRequest,
    ) -> ElastiCacheModifyCacheSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_cache_subnet_group, request, ElastiCacheModifyCacheSubnetGroupResponse)

    async def modify_global_replication_group(
        self,
        request: ElastiCacheModifyGlobalReplicationGroupRequest,
    ) -> ElastiCacheModifyGlobalReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_global_replication_group, request, ElastiCacheModifyGlobalReplicationGroupResponse)

    async def modify_replication_group_shard_configuration(
        self,
        request: ElastiCacheModifyReplicationGroupShardConfigurationRequest,
    ) -> ElastiCacheModifyReplicationGroupShardConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.modify_replication_group_shard_configuration, request, ElastiCacheModifyReplicationGroupShardConfigurationResponse)

    async def modify_serverless_cache(
        self,
        request: ElastiCacheModifyServerlessCacheRequest,
    ) -> ElastiCacheModifyServerlessCacheResponse:
        client = self._require_client()
        return await self._execute(client.modify_serverless_cache, request, ElastiCacheModifyServerlessCacheResponse)

    async def modify_user(
        self,
        request: ElastiCacheModifyUserRequest,
    ) -> ElastiCacheModifyUserResponse:
        client = self._require_client()
        return await self._execute(client.modify_user, request, ElastiCacheModifyUserResponse)

    async def modify_user_group(
        self,
        request: ElastiCacheModifyUserGroupRequest,
    ) -> ElastiCacheModifyUserGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_user_group, request, ElastiCacheModifyUserGroupResponse)

    async def prepare_migration(
        self,
        request: ElastiCachePrepareMigrationRequest,
    ) -> ElastiCachePrepareMigrationResponse:
        client = self._require_client()
        return await self._execute(client.prepare_migration, request, ElastiCachePrepareMigrationResponse)

    async def purchase_reserved_cache_nodes_offering(
        self,
        request: ElastiCachePurchaseReservedCacheNodesOfferingRequest,
    ) -> ElastiCachePurchaseReservedCacheNodesOfferingResponse:
        client = self._require_client()
        return await self._execute(client.purchase_reserved_cache_nodes_offering, request, ElastiCachePurchaseReservedCacheNodesOfferingResponse)

    async def rebalance_slots_in_global_replication_group(
        self,
        request: ElastiCacheRebalanceSlotsInGlobalReplicationGroupRequest,
    ) -> ElastiCacheRebalanceSlotsInGlobalReplicationGroupResponse:
        client = self._require_client()
        return await self._execute(client.rebalance_slots_in_global_replication_group, request, ElastiCacheRebalanceSlotsInGlobalReplicationGroupResponse)

    async def remove_tags_from_resource(
        self,
        request: ElastiCacheRemoveTagsFromResourceRequest,
    ) -> ElastiCacheRemoveTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_resource, request, ElastiCacheRemoveTagsFromResourceResponse)

    async def reset_cache_parameter_group(
        self,
        request: ElastiCacheResetCacheParameterGroupRequest,
    ) -> ElastiCacheResetCacheParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.reset_cache_parameter_group, request, ElastiCacheResetCacheParameterGroupResponse)

    async def revoke_cache_security_group_ingress(
        self,
        request: ElastiCacheRevokeCacheSecurityGroupIngressRequest,
    ) -> ElastiCacheRevokeCacheSecurityGroupIngressResponse:
        client = self._require_client()
        return await self._execute(client.revoke_cache_security_group_ingress, request, ElastiCacheRevokeCacheSecurityGroupIngressResponse)

    async def start_migration(
        self,
        request: ElastiCacheStartMigrationRequest | None = None,
    ) -> ElastiCacheStartMigrationResponse:
        client = self._require_client()
        return await self._execute(client.start_migration, request, ElastiCacheStartMigrationResponse)

    async def stop_migration(
        self,
        request: ElastiCacheStopMigrationRequest,
    ) -> ElastiCacheStopMigrationResponse:
        client = self._require_client()
        return await self._execute(client.stop_migration, request, ElastiCacheStopMigrationResponse)

    async def test_failover(
        self,
        request: ElastiCacheTestFailoverRequest,
    ) -> ElastiCacheTestFailoverResponse:
        client = self._require_client()
        return await self._execute(client.test_failover, request, ElastiCacheTestFailoverResponse)

    async def test_migration(
        self,
        request: ElastiCacheTestMigrationRequest,
    ) -> ElastiCacheTestMigrationResponse:
        client = self._require_client()
        return await self._execute(client.test_migration, request, ElastiCacheTestMigrationResponse)

