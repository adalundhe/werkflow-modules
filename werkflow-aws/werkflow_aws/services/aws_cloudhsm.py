from werkflow_aws.models.cloudhsm import (
    CloudHSMCopyBackupToRegionRequest,
    CloudHSMCopyBackupToRegionResponse,
    CloudHSMCreateClusterRequest,
    CloudHSMCreateClusterResponse,
    CloudHSMCreateHsmRequest,
    CloudHSMCreateHsmResponse,
    CloudHSMDeleteBackupRequest,
    CloudHSMDeleteBackupResponse,
    CloudHSMDeleteClusterRequest,
    CloudHSMDeleteClusterResponse,
    CloudHSMDeleteHsmRequest,
    CloudHSMDeleteHsmResponse,
    CloudHSMDeleteResourcePolicyRequest,
    CloudHSMDeleteResourcePolicyResponse,
    CloudHSMDescribeBackupsRequest,
    CloudHSMDescribeBackupsResponse,
    CloudHSMDescribeClustersRequest,
    CloudHSMDescribeClustersResponse,
    CloudHSMGetResourcePolicyRequest,
    CloudHSMGetResourcePolicyResponse,
    CloudHSMInitializeClusterRequest,
    CloudHSMInitializeClusterResponse,
    CloudHSMListTagsRequest,
    CloudHSMListTagsResponse,
    CloudHSMModifyBackupAttributesRequest,
    CloudHSMModifyBackupAttributesResponse,
    CloudHSMModifyClusterRequest,
    CloudHSMModifyClusterResponse,
    CloudHSMPutResourcePolicyRequest,
    CloudHSMPutResourcePolicyResponse,
    CloudHSMRestoreBackupRequest,
    CloudHSMRestoreBackupResponse,
    CloudHSMTagResourceRequest,
    CloudHSMTagResourceResponse,
    CloudHSMUntagResourceRequest,
    CloudHSMUntagResourceResponse,
)
from werkflow_aws.types.cloudhsm_client import CloudHSMClient
from .base import AWSBaseService


class AWSCloudHSM(AWSBaseService[CloudHSMClient]):
    service_name = 'cloudhsm'
    boto3_service_name = 'cloudhsmv2'

    def __init__(self) -> None:
        super().__init__(service_name='cloudhsm', boto3_service_name='cloudhsmv2')

    async def copy_backup_to_region(
        self,
        request: CloudHSMCopyBackupToRegionRequest,
    ) -> CloudHSMCopyBackupToRegionResponse:
        client = self._require_client()
        return await self._execute(client.copy_backup_to_region, request, CloudHSMCopyBackupToRegionResponse)

    async def create_cluster(
        self,
        request: CloudHSMCreateClusterRequest,
    ) -> CloudHSMCreateClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster, request, CloudHSMCreateClusterResponse)

    async def create_hsm(
        self,
        request: CloudHSMCreateHsmRequest,
    ) -> CloudHSMCreateHsmResponse:
        client = self._require_client()
        return await self._execute(client.create_hsm, request, CloudHSMCreateHsmResponse)

    async def delete_backup(
        self,
        request: CloudHSMDeleteBackupRequest,
    ) -> CloudHSMDeleteBackupResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup, request, CloudHSMDeleteBackupResponse)

    async def delete_cluster(
        self,
        request: CloudHSMDeleteClusterRequest,
    ) -> CloudHSMDeleteClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster, request, CloudHSMDeleteClusterResponse)

    async def delete_hsm(
        self,
        request: CloudHSMDeleteHsmRequest,
    ) -> CloudHSMDeleteHsmResponse:
        client = self._require_client()
        return await self._execute(client.delete_hsm, request, CloudHSMDeleteHsmResponse)

    async def delete_resource_policy(
        self,
        request: CloudHSMDeleteResourcePolicyRequest | None = None,
    ) -> CloudHSMDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, CloudHSMDeleteResourcePolicyResponse)

    async def describe_backups(
        self,
        request: CloudHSMDescribeBackupsRequest | None = None,
    ) -> CloudHSMDescribeBackupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_backups, request, CloudHSMDescribeBackupsResponse)

    async def describe_backups_paginated(
        self,
        request: CloudHSMDescribeBackupsRequest | None = None,
    ) -> list[CloudHSMDescribeBackupsResponse]:
        return await self._paginate('describe_backups', request, CloudHSMDescribeBackupsResponse)

    async def describe_clusters(
        self,
        request: CloudHSMDescribeClustersRequest | None = None,
    ) -> CloudHSMDescribeClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_clusters, request, CloudHSMDescribeClustersResponse)

    async def describe_clusters_paginated(
        self,
        request: CloudHSMDescribeClustersRequest | None = None,
    ) -> list[CloudHSMDescribeClustersResponse]:
        return await self._paginate('describe_clusters', request, CloudHSMDescribeClustersResponse)

    async def get_resource_policy(
        self,
        request: CloudHSMGetResourcePolicyRequest | None = None,
    ) -> CloudHSMGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, CloudHSMGetResourcePolicyResponse)

    async def initialize_cluster(
        self,
        request: CloudHSMInitializeClusterRequest,
    ) -> CloudHSMInitializeClusterResponse:
        client = self._require_client()
        return await self._execute(client.initialize_cluster, request, CloudHSMInitializeClusterResponse)

    async def list_tags(
        self,
        request: CloudHSMListTagsRequest,
    ) -> CloudHSMListTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_tags, request, CloudHSMListTagsResponse)

    async def list_tags_paginated(
        self,
        request: CloudHSMListTagsRequest,
    ) -> list[CloudHSMListTagsResponse]:
        return await self._paginate('list_tags', request, CloudHSMListTagsResponse)

    async def modify_backup_attributes(
        self,
        request: CloudHSMModifyBackupAttributesRequest,
    ) -> CloudHSMModifyBackupAttributesResponse:
        client = self._require_client()
        return await self._execute(client.modify_backup_attributes, request, CloudHSMModifyBackupAttributesResponse)

    async def modify_cluster(
        self,
        request: CloudHSMModifyClusterRequest,
    ) -> CloudHSMModifyClusterResponse:
        client = self._require_client()
        return await self._execute(client.modify_cluster, request, CloudHSMModifyClusterResponse)

    async def put_resource_policy(
        self,
        request: CloudHSMPutResourcePolicyRequest | None = None,
    ) -> CloudHSMPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, CloudHSMPutResourcePolicyResponse)

    async def restore_backup(
        self,
        request: CloudHSMRestoreBackupRequest,
    ) -> CloudHSMRestoreBackupResponse:
        client = self._require_client()
        return await self._execute(client.restore_backup, request, CloudHSMRestoreBackupResponse)

    async def tag_resource(
        self,
        request: CloudHSMTagResourceRequest,
    ) -> CloudHSMTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CloudHSMTagResourceResponse)

    async def untag_resource(
        self,
        request: CloudHSMUntagResourceRequest,
    ) -> CloudHSMUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CloudHSMUntagResourceResponse)
