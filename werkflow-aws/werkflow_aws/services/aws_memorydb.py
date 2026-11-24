from werkflow_aws.models.memorydb import (
    MemoryDBBatchUpdateClusterRequest,
    MemoryDBBatchUpdateClusterResponse,
    MemoryDBCopySnapshotRequest,
    MemoryDBCopySnapshotResponse,
    MemoryDBCreateACLRequest,
    MemoryDBCreateACLResponse,
    MemoryDBCreateClusterRequest,
    MemoryDBCreateClusterResponse,
    MemoryDBCreateMultiRegionClusterRequest,
    MemoryDBCreateMultiRegionClusterResponse,
    MemoryDBCreateParameterGroupRequest,
    MemoryDBCreateParameterGroupResponse,
    MemoryDBCreateSnapshotRequest,
    MemoryDBCreateSnapshotResponse,
    MemoryDBCreateSubnetGroupRequest,
    MemoryDBCreateSubnetGroupResponse,
    MemoryDBCreateUserRequest,
    MemoryDBCreateUserResponse,
    MemoryDBDeleteACLRequest,
    MemoryDBDeleteACLResponse,
    MemoryDBDeleteClusterRequest,
    MemoryDBDeleteClusterResponse,
    MemoryDBDeleteMultiRegionClusterRequest,
    MemoryDBDeleteMultiRegionClusterResponse,
    MemoryDBDeleteParameterGroupRequest,
    MemoryDBDeleteParameterGroupResponse,
    MemoryDBDeleteSnapshotRequest,
    MemoryDBDeleteSnapshotResponse,
    MemoryDBDeleteSubnetGroupRequest,
    MemoryDBDeleteSubnetGroupResponse,
    MemoryDBDeleteUserRequest,
    MemoryDBDeleteUserResponse,
    MemoryDBDescribeACLsRequest,
    MemoryDBDescribeACLsResponse,
    MemoryDBDescribeClustersRequest,
    MemoryDBDescribeClustersResponse,
    MemoryDBDescribeEngineVersionsRequest,
    MemoryDBDescribeEngineVersionsResponse,
    MemoryDBDescribeEventsRequest,
    MemoryDBDescribeEventsResponse,
    MemoryDBDescribeMultiRegionClustersRequest,
    MemoryDBDescribeMultiRegionClustersResponse,
    MemoryDBDescribeMultiRegionParameterGroupsRequest,
    MemoryDBDescribeMultiRegionParameterGroupsResponse,
    MemoryDBDescribeMultiRegionParametersRequest,
    MemoryDBDescribeMultiRegionParametersResponse,
    MemoryDBDescribeParameterGroupsRequest,
    MemoryDBDescribeParameterGroupsResponse,
    MemoryDBDescribeParametersRequest,
    MemoryDBDescribeParametersResponse,
    MemoryDBDescribeReservedNodesOfferingsRequest,
    MemoryDBDescribeReservedNodesOfferingsResponse,
    MemoryDBDescribeReservedNodesRequest,
    MemoryDBDescribeReservedNodesResponse,
    MemoryDBDescribeServiceUpdatesRequest,
    MemoryDBDescribeServiceUpdatesResponse,
    MemoryDBDescribeSnapshotsRequest,
    MemoryDBDescribeSnapshotsResponse,
    MemoryDBDescribeSubnetGroupsRequest,
    MemoryDBDescribeSubnetGroupsResponse,
    MemoryDBDescribeUsersRequest,
    MemoryDBDescribeUsersResponse,
    MemoryDBFailoverShardRequest,
    MemoryDBFailoverShardResponse,
    MemoryDBListAllowedMultiRegionClusterUpdatesRequest,
    MemoryDBListAllowedMultiRegionClusterUpdatesResponse,
    MemoryDBListAllowedNodeTypeUpdatesRequest,
    MemoryDBListAllowedNodeTypeUpdatesResponse,
    MemoryDBListTagsRequest,
    MemoryDBListTagsResponse,
    MemoryDBPurchaseReservedNodesOfferingRequest,
    MemoryDBPurchaseReservedNodesOfferingResponse,
    MemoryDBResetParameterGroupRequest,
    MemoryDBResetParameterGroupResponse,
    MemoryDBTagResourceRequest,
    MemoryDBTagResourceResponse,
    MemoryDBUntagResourceRequest,
    MemoryDBUntagResourceResponse,
    MemoryDBUpdateACLRequest,
    MemoryDBUpdateACLResponse,
    MemoryDBUpdateClusterRequest,
    MemoryDBUpdateClusterResponse,
    MemoryDBUpdateMultiRegionClusterRequest,
    MemoryDBUpdateMultiRegionClusterResponse,
    MemoryDBUpdateParameterGroupRequest,
    MemoryDBUpdateParameterGroupResponse,
    MemoryDBUpdateSubnetGroupRequest,
    MemoryDBUpdateSubnetGroupResponse,
    MemoryDBUpdateUserRequest,
    MemoryDBUpdateUserResponse,
)
from werkflow_aws.types.memorydb_client import MemoryDBClient
from .base import AWSBaseService


class AWSMemoryDB(AWSBaseService[MemoryDBClient]):
    service_name = 'memorydb'
    boto3_service_name = 'memorydb'

    def __init__(self) -> None:
        super().__init__(service_name='memorydb', boto3_service_name='memorydb')

    async def batch_update_cluster(
        self,
        request: MemoryDBBatchUpdateClusterRequest,
    ) -> MemoryDBBatchUpdateClusterResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_cluster, request, MemoryDBBatchUpdateClusterResponse)

    async def copy_snapshot(
        self,
        request: MemoryDBCopySnapshotRequest,
    ) -> MemoryDBCopySnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_snapshot, request, MemoryDBCopySnapshotResponse)

    async def create_acl(
        self,
        request: MemoryDBCreateACLRequest,
    ) -> MemoryDBCreateACLResponse:
        client = self._require_client()
        return await self._execute(client.create_acl, request, MemoryDBCreateACLResponse)

    async def create_cluster(
        self,
        request: MemoryDBCreateClusterRequest,
    ) -> MemoryDBCreateClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster, request, MemoryDBCreateClusterResponse)

    async def create_multi_region_cluster(
        self,
        request: MemoryDBCreateMultiRegionClusterRequest,
    ) -> MemoryDBCreateMultiRegionClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_multi_region_cluster, request, MemoryDBCreateMultiRegionClusterResponse)

    async def create_parameter_group(
        self,
        request: MemoryDBCreateParameterGroupRequest,
    ) -> MemoryDBCreateParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_parameter_group, request, MemoryDBCreateParameterGroupResponse)

    async def create_snapshot(
        self,
        request: MemoryDBCreateSnapshotRequest,
    ) -> MemoryDBCreateSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot, request, MemoryDBCreateSnapshotResponse)

    async def create_subnet_group(
        self,
        request: MemoryDBCreateSubnetGroupRequest,
    ) -> MemoryDBCreateSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_subnet_group, request, MemoryDBCreateSubnetGroupResponse)

    async def create_user(
        self,
        request: MemoryDBCreateUserRequest,
    ) -> MemoryDBCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, MemoryDBCreateUserResponse)

    async def delete_acl(
        self,
        request: MemoryDBDeleteACLRequest,
    ) -> MemoryDBDeleteACLResponse:
        client = self._require_client()
        return await self._execute(client.delete_acl, request, MemoryDBDeleteACLResponse)

    async def delete_cluster(
        self,
        request: MemoryDBDeleteClusterRequest,
    ) -> MemoryDBDeleteClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster, request, MemoryDBDeleteClusterResponse)

    async def delete_multi_region_cluster(
        self,
        request: MemoryDBDeleteMultiRegionClusterRequest,
    ) -> MemoryDBDeleteMultiRegionClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_multi_region_cluster, request, MemoryDBDeleteMultiRegionClusterResponse)

    async def delete_parameter_group(
        self,
        request: MemoryDBDeleteParameterGroupRequest,
    ) -> MemoryDBDeleteParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_parameter_group, request, MemoryDBDeleteParameterGroupResponse)

    async def delete_snapshot(
        self,
        request: MemoryDBDeleteSnapshotRequest,
    ) -> MemoryDBDeleteSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot, request, MemoryDBDeleteSnapshotResponse)

    async def delete_subnet_group(
        self,
        request: MemoryDBDeleteSubnetGroupRequest,
    ) -> MemoryDBDeleteSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_subnet_group, request, MemoryDBDeleteSubnetGroupResponse)

    async def delete_user(
        self,
        request: MemoryDBDeleteUserRequest,
    ) -> MemoryDBDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, MemoryDBDeleteUserResponse)

    async def describe_acls(
        self,
        request: MemoryDBDescribeACLsRequest | None = None,
    ) -> MemoryDBDescribeACLsResponse:
        client = self._require_client()
        return await self._execute(client.describe_acls, request, MemoryDBDescribeACLsResponse)

    async def describe_acls_paginated(
        self,
        request: MemoryDBDescribeACLsRequest | None = None,
    ) -> list[MemoryDBDescribeACLsResponse]:
        return await self._paginate('describe_acls', request, MemoryDBDescribeACLsResponse)

    async def describe_clusters(
        self,
        request: MemoryDBDescribeClustersRequest | None = None,
    ) -> MemoryDBDescribeClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_clusters, request, MemoryDBDescribeClustersResponse)

    async def describe_clusters_paginated(
        self,
        request: MemoryDBDescribeClustersRequest | None = None,
    ) -> list[MemoryDBDescribeClustersResponse]:
        return await self._paginate('describe_clusters', request, MemoryDBDescribeClustersResponse)

    async def describe_engine_versions(
        self,
        request: MemoryDBDescribeEngineVersionsRequest | None = None,
    ) -> MemoryDBDescribeEngineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_engine_versions, request, MemoryDBDescribeEngineVersionsResponse)

    async def describe_engine_versions_paginated(
        self,
        request: MemoryDBDescribeEngineVersionsRequest | None = None,
    ) -> list[MemoryDBDescribeEngineVersionsResponse]:
        return await self._paginate('describe_engine_versions', request, MemoryDBDescribeEngineVersionsResponse)

    async def describe_events(
        self,
        request: MemoryDBDescribeEventsRequest | None = None,
    ) -> MemoryDBDescribeEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_events, request, MemoryDBDescribeEventsResponse)

    async def describe_events_paginated(
        self,
        request: MemoryDBDescribeEventsRequest | None = None,
    ) -> list[MemoryDBDescribeEventsResponse]:
        return await self._paginate('describe_events', request, MemoryDBDescribeEventsResponse)

    async def describe_multi_region_clusters(
        self,
        request: MemoryDBDescribeMultiRegionClustersRequest | None = None,
    ) -> MemoryDBDescribeMultiRegionClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_multi_region_clusters, request, MemoryDBDescribeMultiRegionClustersResponse)

    async def describe_multi_region_clusters_paginated(
        self,
        request: MemoryDBDescribeMultiRegionClustersRequest | None = None,
    ) -> list[MemoryDBDescribeMultiRegionClustersResponse]:
        return await self._paginate('describe_multi_region_clusters', request, MemoryDBDescribeMultiRegionClustersResponse)

    async def describe_multi_region_parameter_groups(
        self,
        request: MemoryDBDescribeMultiRegionParameterGroupsRequest | None = None,
    ) -> MemoryDBDescribeMultiRegionParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_multi_region_parameter_groups, request, MemoryDBDescribeMultiRegionParameterGroupsResponse)

    async def describe_multi_region_parameters(
        self,
        request: MemoryDBDescribeMultiRegionParametersRequest,
    ) -> MemoryDBDescribeMultiRegionParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_multi_region_parameters, request, MemoryDBDescribeMultiRegionParametersResponse)

    async def describe_parameter_groups(
        self,
        request: MemoryDBDescribeParameterGroupsRequest | None = None,
    ) -> MemoryDBDescribeParameterGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_parameter_groups, request, MemoryDBDescribeParameterGroupsResponse)

    async def describe_parameter_groups_paginated(
        self,
        request: MemoryDBDescribeParameterGroupsRequest | None = None,
    ) -> list[MemoryDBDescribeParameterGroupsResponse]:
        return await self._paginate('describe_parameter_groups', request, MemoryDBDescribeParameterGroupsResponse)

    async def describe_parameters(
        self,
        request: MemoryDBDescribeParametersRequest,
    ) -> MemoryDBDescribeParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_parameters, request, MemoryDBDescribeParametersResponse)

    async def describe_parameters_paginated(
        self,
        request: MemoryDBDescribeParametersRequest,
    ) -> list[MemoryDBDescribeParametersResponse]:
        return await self._paginate('describe_parameters', request, MemoryDBDescribeParametersResponse)

    async def describe_reserved_nodes(
        self,
        request: MemoryDBDescribeReservedNodesRequest | None = None,
    ) -> MemoryDBDescribeReservedNodesResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_nodes, request, MemoryDBDescribeReservedNodesResponse)

    async def describe_reserved_nodes_paginated(
        self,
        request: MemoryDBDescribeReservedNodesRequest | None = None,
    ) -> list[MemoryDBDescribeReservedNodesResponse]:
        return await self._paginate('describe_reserved_nodes', request, MemoryDBDescribeReservedNodesResponse)

    async def describe_reserved_nodes_offerings(
        self,
        request: MemoryDBDescribeReservedNodesOfferingsRequest | None = None,
    ) -> MemoryDBDescribeReservedNodesOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_nodes_offerings, request, MemoryDBDescribeReservedNodesOfferingsResponse)

    async def describe_reserved_nodes_offerings_paginated(
        self,
        request: MemoryDBDescribeReservedNodesOfferingsRequest | None = None,
    ) -> list[MemoryDBDescribeReservedNodesOfferingsResponse]:
        return await self._paginate('describe_reserved_nodes_offerings', request, MemoryDBDescribeReservedNodesOfferingsResponse)

    async def describe_service_updates(
        self,
        request: MemoryDBDescribeServiceUpdatesRequest | None = None,
    ) -> MemoryDBDescribeServiceUpdatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_updates, request, MemoryDBDescribeServiceUpdatesResponse)

    async def describe_service_updates_paginated(
        self,
        request: MemoryDBDescribeServiceUpdatesRequest | None = None,
    ) -> list[MemoryDBDescribeServiceUpdatesResponse]:
        return await self._paginate('describe_service_updates', request, MemoryDBDescribeServiceUpdatesResponse)

    async def describe_snapshots(
        self,
        request: MemoryDBDescribeSnapshotsRequest | None = None,
    ) -> MemoryDBDescribeSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshots, request, MemoryDBDescribeSnapshotsResponse)

    async def describe_snapshots_paginated(
        self,
        request: MemoryDBDescribeSnapshotsRequest | None = None,
    ) -> list[MemoryDBDescribeSnapshotsResponse]:
        return await self._paginate('describe_snapshots', request, MemoryDBDescribeSnapshotsResponse)

    async def describe_subnet_groups(
        self,
        request: MemoryDBDescribeSubnetGroupsRequest | None = None,
    ) -> MemoryDBDescribeSubnetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_subnet_groups, request, MemoryDBDescribeSubnetGroupsResponse)

    async def describe_subnet_groups_paginated(
        self,
        request: MemoryDBDescribeSubnetGroupsRequest | None = None,
    ) -> list[MemoryDBDescribeSubnetGroupsResponse]:
        return await self._paginate('describe_subnet_groups', request, MemoryDBDescribeSubnetGroupsResponse)

    async def describe_users(
        self,
        request: MemoryDBDescribeUsersRequest | None = None,
    ) -> MemoryDBDescribeUsersResponse:
        client = self._require_client()
        return await self._execute(client.describe_users, request, MemoryDBDescribeUsersResponse)

    async def describe_users_paginated(
        self,
        request: MemoryDBDescribeUsersRequest | None = None,
    ) -> list[MemoryDBDescribeUsersResponse]:
        return await self._paginate('describe_users', request, MemoryDBDescribeUsersResponse)

    async def failover_shard(
        self,
        request: MemoryDBFailoverShardRequest,
    ) -> MemoryDBFailoverShardResponse:
        client = self._require_client()
        return await self._execute(client.failover_shard, request, MemoryDBFailoverShardResponse)

    async def list_allowed_multi_region_cluster_updates(
        self,
        request: MemoryDBListAllowedMultiRegionClusterUpdatesRequest,
    ) -> MemoryDBListAllowedMultiRegionClusterUpdatesResponse:
        client = self._require_client()
        return await self._execute(client.list_allowed_multi_region_cluster_updates, request, MemoryDBListAllowedMultiRegionClusterUpdatesResponse)

    async def list_allowed_node_type_updates(
        self,
        request: MemoryDBListAllowedNodeTypeUpdatesRequest,
    ) -> MemoryDBListAllowedNodeTypeUpdatesResponse:
        client = self._require_client()
        return await self._execute(client.list_allowed_node_type_updates, request, MemoryDBListAllowedNodeTypeUpdatesResponse)

    async def list_tags(
        self,
        request: MemoryDBListTagsRequest,
    ) -> MemoryDBListTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_tags, request, MemoryDBListTagsResponse)

    async def purchase_reserved_nodes_offering(
        self,
        request: MemoryDBPurchaseReservedNodesOfferingRequest,
    ) -> MemoryDBPurchaseReservedNodesOfferingResponse:
        client = self._require_client()
        return await self._execute(client.purchase_reserved_nodes_offering, request, MemoryDBPurchaseReservedNodesOfferingResponse)

    async def reset_parameter_group(
        self,
        request: MemoryDBResetParameterGroupRequest,
    ) -> MemoryDBResetParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.reset_parameter_group, request, MemoryDBResetParameterGroupResponse)

    async def tag_resource(
        self,
        request: MemoryDBTagResourceRequest,
    ) -> MemoryDBTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, MemoryDBTagResourceResponse)

    async def untag_resource(
        self,
        request: MemoryDBUntagResourceRequest,
    ) -> MemoryDBUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, MemoryDBUntagResourceResponse)

    async def update_acl(
        self,
        request: MemoryDBUpdateACLRequest,
    ) -> MemoryDBUpdateACLResponse:
        client = self._require_client()
        return await self._execute(client.update_acl, request, MemoryDBUpdateACLResponse)

    async def update_cluster(
        self,
        request: MemoryDBUpdateClusterRequest,
    ) -> MemoryDBUpdateClusterResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster, request, MemoryDBUpdateClusterResponse)

    async def update_multi_region_cluster(
        self,
        request: MemoryDBUpdateMultiRegionClusterRequest,
    ) -> MemoryDBUpdateMultiRegionClusterResponse:
        client = self._require_client()
        return await self._execute(client.update_multi_region_cluster, request, MemoryDBUpdateMultiRegionClusterResponse)

    async def update_parameter_group(
        self,
        request: MemoryDBUpdateParameterGroupRequest,
    ) -> MemoryDBUpdateParameterGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_parameter_group, request, MemoryDBUpdateParameterGroupResponse)

    async def update_subnet_group(
        self,
        request: MemoryDBUpdateSubnetGroupRequest,
    ) -> MemoryDBUpdateSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_subnet_group, request, MemoryDBUpdateSubnetGroupResponse)

    async def update_user(
        self,
        request: MemoryDBUpdateUserRequest,
    ) -> MemoryDBUpdateUserResponse:
        client = self._require_client()
        return await self._execute(client.update_user, request, MemoryDBUpdateUserResponse)
