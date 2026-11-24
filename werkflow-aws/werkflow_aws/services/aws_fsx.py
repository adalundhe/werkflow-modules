from werkflow_aws.models.fsx import (
    FSxAssociateFileSystemAliasesRequest,
    FSxAssociateFileSystemAliasesResponse,
    FSxCancelDataRepositoryTaskRequest,
    FSxCancelDataRepositoryTaskResponse,
    FSxCopyBackupRequest,
    FSxCopyBackupResponse,
    FSxCopySnapshotAndUpdateVolumeRequest,
    FSxCopySnapshotAndUpdateVolumeResponse,
    FSxCreateAndAttachS3AccessPointRequest,
    FSxCreateAndAttachS3AccessPointResponse,
    FSxCreateBackupRequest,
    FSxCreateBackupResponse,
    FSxCreateClusterPeerRequest,
    FSxCreateClusterPeerResponse,
    FSxCreateDataRepositoryAssociationRequest,
    FSxCreateDataRepositoryAssociationResponse,
    FSxCreateDataRepositoryTaskRequest,
    FSxCreateDataRepositoryTaskResponse,
    FSxCreateFileCacheRequest,
    FSxCreateFileCacheResponse,
    FSxCreateFileSystemFromBackupRequest,
    FSxCreateFileSystemFromBackupResponse,
    FSxCreateFileSystemRequest,
    FSxCreateFileSystemResponse,
    FSxCreateSnapmirrorPolicyRequest,
    FSxCreateSnapmirrorPolicyResponse,
    FSxCreateSnapmirrorRelationshipRequest,
    FSxCreateSnapmirrorRelationshipResponse,
    FSxCreateSnapshotPolicyRequest,
    FSxCreateSnapshotPolicyResponse,
    FSxCreateSnapshotRequest,
    FSxCreateSnapshotResponse,
    FSxCreateStorageVirtualMachinePeerRequest,
    FSxCreateStorageVirtualMachinePeerResponse,
    FSxCreateStorageVirtualMachineRequest,
    FSxCreateStorageVirtualMachineResponse,
    FSxCreateVolumeFromBackupRequest,
    FSxCreateVolumeFromBackupResponse,
    FSxCreateVolumeRequest,
    FSxCreateVolumeResponse,
    FSxDeleteBackupRequest,
    FSxDeleteBackupResponse,
    FSxDeleteClusterPeerRequest,
    FSxDeleteClusterPeerResponse,
    FSxDeleteDataRepositoryAssociationRequest,
    FSxDeleteDataRepositoryAssociationResponse,
    FSxDeleteFileCacheRequest,
    FSxDeleteFileCacheResponse,
    FSxDeleteFileSystemRequest,
    FSxDeleteFileSystemResponse,
    FSxDeleteSnapmirrorPolicyRequest,
    FSxDeleteSnapmirrorPolicyResponse,
    FSxDeleteSnapmirrorRelationshipRequest,
    FSxDeleteSnapmirrorRelationshipResponse,
    FSxDeleteSnapshotPolicyRequest,
    FSxDeleteSnapshotPolicyResponse,
    FSxDeleteSnapshotRequest,
    FSxDeleteSnapshotResponse,
    FSxDeleteStorageVirtualMachinePeerRequest,
    FSxDeleteStorageVirtualMachinePeerResponse,
    FSxDeleteStorageVirtualMachineRequest,
    FSxDeleteStorageVirtualMachineResponse,
    FSxDeleteVolumeRequest,
    FSxDeleteVolumeResponse,
    FSxDescribeBackupsRequest,
    FSxDescribeBackupsResponse,
    FSxDescribeClusterPeersRequest,
    FSxDescribeClusterPeersResponse,
    FSxDescribeDataRepositoryAssociationsRequest,
    FSxDescribeDataRepositoryAssociationsResponse,
    FSxDescribeDataRepositoryTasksRequest,
    FSxDescribeDataRepositoryTasksResponse,
    FSxDescribeFileCachesRequest,
    FSxDescribeFileCachesResponse,
    FSxDescribeFileSystemAliasesRequest,
    FSxDescribeFileSystemAliasesResponse,
    FSxDescribeFileSystemsRequest,
    FSxDescribeFileSystemsResponse,
    FSxDescribeS3AccessPointAttachmentsRequest,
    FSxDescribeS3AccessPointAttachmentsResponse,
    FSxDescribeSharedVpcConfigurationRequest,
    FSxDescribeSharedVpcConfigurationResponse,
    FSxDescribeSnapmirrorPoliciesRequest,
    FSxDescribeSnapmirrorPoliciesResponse,
    FSxDescribeSnapmirrorRelationshipsRequest,
    FSxDescribeSnapmirrorRelationshipsResponse,
    FSxDescribeSnapshotPoliciesRequest,
    FSxDescribeSnapshotPoliciesResponse,
    FSxDescribeSnapshotsRequest,
    FSxDescribeSnapshotsResponse,
    FSxDescribeStorageVirtualMachinePeersRequest,
    FSxDescribeStorageVirtualMachinePeersResponse,
    FSxDescribeStorageVirtualMachinesRequest,
    FSxDescribeStorageVirtualMachinesResponse,
    FSxDescribeVolumesRequest,
    FSxDescribeVolumesResponse,
    FSxDetachAndDeleteS3AccessPointRequest,
    FSxDetachAndDeleteS3AccessPointResponse,
    FSxDisassociateFileSystemAliasesRequest,
    FSxDisassociateFileSystemAliasesResponse,
    FSxListTagsForResourceRequest,
    FSxListTagsForResourceResponse,
    FSxReleaseFileSystemNfsV3LocksRequest,
    FSxReleaseFileSystemNfsV3LocksResponse,
    FSxRestoreVolumeFromSnapshotRequest,
    FSxRestoreVolumeFromSnapshotResponse,
    FSxStartMisconfiguredStateRecoveryRequest,
    FSxStartMisconfiguredStateRecoveryResponse,
    FSxTagResourceRequest,
    FSxTagResourceResponse,
    FSxUntagResourceRequest,
    FSxUntagResourceResponse,
    FSxUpdateClusterPeerRequest,
    FSxUpdateClusterPeerResponse,
    FSxUpdateDataRepositoryAssociationRequest,
    FSxUpdateDataRepositoryAssociationResponse,
    FSxUpdateFileCacheRequest,
    FSxUpdateFileCacheResponse,
    FSxUpdateFileSystemRequest,
    FSxUpdateFileSystemResponse,
    FSxUpdateSharedVpcConfigurationRequest,
    FSxUpdateSharedVpcConfigurationResponse,
    FSxUpdateSnapmirrorPolicyRequest,
    FSxUpdateSnapmirrorPolicyResponse,
    FSxUpdateSnapmirrorRelationshipRequest,
    FSxUpdateSnapmirrorRelationshipResponse,
    FSxUpdateSnapshotPolicyRequest,
    FSxUpdateSnapshotPolicyResponse,
    FSxUpdateSnapshotRequest,
    FSxUpdateSnapshotResponse,
    FSxUpdateStorageVirtualMachinePeerRequest,
    FSxUpdateStorageVirtualMachinePeerResponse,
    FSxUpdateStorageVirtualMachineRequest,
    FSxUpdateStorageVirtualMachineResponse,
    FSxUpdateVolumeRequest,
    FSxUpdateVolumeResponse,
)
from werkflow_aws.types.fsx_client import FSxClient
from .base import AWSBaseService


class AWSFSx(AWSBaseService[FSxClient]):
    service_name = 'fsx'
    boto3_service_name = 'fsx'

    def __init__(self) -> None:
        super().__init__(service_name='fsx', boto3_service_name='fsx')

    async def associate_file_system_aliases(
        self,
        request: FSxAssociateFileSystemAliasesRequest,
    ) -> FSxAssociateFileSystemAliasesResponse:
        client = self._require_client()
        return await self._execute(client.associate_file_system_aliases, request, FSxAssociateFileSystemAliasesResponse)

    async def cancel_data_repository_task(
        self,
        request: FSxCancelDataRepositoryTaskRequest,
    ) -> FSxCancelDataRepositoryTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_data_repository_task, request, FSxCancelDataRepositoryTaskResponse)

    async def copy_backup(
        self,
        request: FSxCopyBackupRequest,
    ) -> FSxCopyBackupResponse:
        client = self._require_client()
        return await self._execute(client.copy_backup, request, FSxCopyBackupResponse)

    async def copy_snapshot_and_update_volume(
        self,
        request: FSxCopySnapshotAndUpdateVolumeRequest,
    ) -> FSxCopySnapshotAndUpdateVolumeResponse:
        client = self._require_client()
        return await self._execute(client.copy_snapshot_and_update_volume, request, FSxCopySnapshotAndUpdateVolumeResponse)

    async def create_and_attach_s3_access_point(
        self,
        request: FSxCreateAndAttachS3AccessPointRequest,
    ) -> FSxCreateAndAttachS3AccessPointResponse:
        client = self._require_client()
        return await self._execute(client.create_and_attach_s3_access_point, request, FSxCreateAndAttachS3AccessPointResponse)

    async def create_backup(
        self,
        request: FSxCreateBackupRequest | None = None,
    ) -> FSxCreateBackupResponse:
        client = self._require_client()
        return await self._execute(client.create_backup, request, FSxCreateBackupResponse)

    async def create_cluster_peer(
        self,
        request: FSxCreateClusterPeerRequest,
    ) -> FSxCreateClusterPeerResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster_peer, request, FSxCreateClusterPeerResponse)

    async def create_data_repository_association(
        self,
        request: FSxCreateDataRepositoryAssociationRequest,
    ) -> FSxCreateDataRepositoryAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_data_repository_association, request, FSxCreateDataRepositoryAssociationResponse)

    async def create_data_repository_task(
        self,
        request: FSxCreateDataRepositoryTaskRequest,
    ) -> FSxCreateDataRepositoryTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_data_repository_task, request, FSxCreateDataRepositoryTaskResponse)

    async def create_file_cache(
        self,
        request: FSxCreateFileCacheRequest,
    ) -> FSxCreateFileCacheResponse:
        client = self._require_client()
        return await self._execute(client.create_file_cache, request, FSxCreateFileCacheResponse)

    async def create_file_system(
        self,
        request: FSxCreateFileSystemRequest,
    ) -> FSxCreateFileSystemResponse:
        client = self._require_client()
        return await self._execute(client.create_file_system, request, FSxCreateFileSystemResponse)

    async def create_file_system_from_backup(
        self,
        request: FSxCreateFileSystemFromBackupRequest,
    ) -> FSxCreateFileSystemFromBackupResponse:
        client = self._require_client()
        return await self._execute(client.create_file_system_from_backup, request, FSxCreateFileSystemFromBackupResponse)

    async def create_snapmirror_policy(
        self,
        request: FSxCreateSnapmirrorPolicyRequest,
    ) -> FSxCreateSnapmirrorPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_snapmirror_policy, request, FSxCreateSnapmirrorPolicyResponse)

    async def create_snapmirror_relationship(
        self,
        request: FSxCreateSnapmirrorRelationshipRequest,
    ) -> FSxCreateSnapmirrorRelationshipResponse:
        client = self._require_client()
        return await self._execute(client.create_snapmirror_relationship, request, FSxCreateSnapmirrorRelationshipResponse)

    async def create_snapshot(
        self,
        request: FSxCreateSnapshotRequest,
    ) -> FSxCreateSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot, request, FSxCreateSnapshotResponse)

    async def create_snapshot_policy(
        self,
        request: FSxCreateSnapshotPolicyRequest,
    ) -> FSxCreateSnapshotPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot_policy, request, FSxCreateSnapshotPolicyResponse)

    async def create_storage_virtual_machine(
        self,
        request: FSxCreateStorageVirtualMachineRequest,
    ) -> FSxCreateStorageVirtualMachineResponse:
        client = self._require_client()
        return await self._execute(client.create_storage_virtual_machine, request, FSxCreateStorageVirtualMachineResponse)

    async def create_storage_virtual_machine_peer(
        self,
        request: FSxCreateStorageVirtualMachinePeerRequest,
    ) -> FSxCreateStorageVirtualMachinePeerResponse:
        client = self._require_client()
        return await self._execute(client.create_storage_virtual_machine_peer, request, FSxCreateStorageVirtualMachinePeerResponse)

    async def create_volume(
        self,
        request: FSxCreateVolumeRequest,
    ) -> FSxCreateVolumeResponse:
        client = self._require_client()
        return await self._execute(client.create_volume, request, FSxCreateVolumeResponse)

    async def create_volume_from_backup(
        self,
        request: FSxCreateVolumeFromBackupRequest,
    ) -> FSxCreateVolumeFromBackupResponse:
        client = self._require_client()
        return await self._execute(client.create_volume_from_backup, request, FSxCreateVolumeFromBackupResponse)

    async def delete_backup(
        self,
        request: FSxDeleteBackupRequest,
    ) -> FSxDeleteBackupResponse:
        client = self._require_client()
        return await self._execute(client.delete_backup, request, FSxDeleteBackupResponse)

    async def delete_cluster_peer(
        self,
        request: FSxDeleteClusterPeerRequest,
    ) -> FSxDeleteClusterPeerResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster_peer, request, FSxDeleteClusterPeerResponse)

    async def delete_data_repository_association(
        self,
        request: FSxDeleteDataRepositoryAssociationRequest,
    ) -> FSxDeleteDataRepositoryAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_repository_association, request, FSxDeleteDataRepositoryAssociationResponse)

    async def delete_file_cache(
        self,
        request: FSxDeleteFileCacheRequest,
    ) -> FSxDeleteFileCacheResponse:
        client = self._require_client()
        return await self._execute(client.delete_file_cache, request, FSxDeleteFileCacheResponse)

    async def delete_file_system(
        self,
        request: FSxDeleteFileSystemRequest,
    ) -> FSxDeleteFileSystemResponse:
        client = self._require_client()
        return await self._execute(client.delete_file_system, request, FSxDeleteFileSystemResponse)

    async def delete_snapmirror_policy(
        self,
        request: FSxDeleteSnapmirrorPolicyRequest,
    ) -> FSxDeleteSnapmirrorPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapmirror_policy, request, FSxDeleteSnapmirrorPolicyResponse)

    async def delete_snapmirror_relationship(
        self,
        request: FSxDeleteSnapmirrorRelationshipRequest,
    ) -> FSxDeleteSnapmirrorRelationshipResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapmirror_relationship, request, FSxDeleteSnapmirrorRelationshipResponse)

    async def delete_snapshot(
        self,
        request: FSxDeleteSnapshotRequest,
    ) -> FSxDeleteSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot, request, FSxDeleteSnapshotResponse)

    async def delete_snapshot_policy(
        self,
        request: FSxDeleteSnapshotPolicyRequest,
    ) -> FSxDeleteSnapshotPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot_policy, request, FSxDeleteSnapshotPolicyResponse)

    async def delete_storage_virtual_machine(
        self,
        request: FSxDeleteStorageVirtualMachineRequest,
    ) -> FSxDeleteStorageVirtualMachineResponse:
        client = self._require_client()
        return await self._execute(client.delete_storage_virtual_machine, request, FSxDeleteStorageVirtualMachineResponse)

    async def delete_storage_virtual_machine_peer(
        self,
        request: FSxDeleteStorageVirtualMachinePeerRequest,
    ) -> FSxDeleteStorageVirtualMachinePeerResponse:
        client = self._require_client()
        return await self._execute(client.delete_storage_virtual_machine_peer, request, FSxDeleteStorageVirtualMachinePeerResponse)

    async def delete_volume(
        self,
        request: FSxDeleteVolumeRequest,
    ) -> FSxDeleteVolumeResponse:
        client = self._require_client()
        return await self._execute(client.delete_volume, request, FSxDeleteVolumeResponse)

    async def describe_backups(
        self,
        request: FSxDescribeBackupsRequest | None = None,
    ) -> FSxDescribeBackupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_backups, request, FSxDescribeBackupsResponse)

    async def describe_backups_paginated(
        self,
        request: FSxDescribeBackupsRequest | None = None,
    ) -> list[FSxDescribeBackupsResponse]:
        return await self._paginate('describe_backups', request, FSxDescribeBackupsResponse)

    async def describe_cluster_peers(
        self,
        request: FSxDescribeClusterPeersRequest | None = None,
    ) -> FSxDescribeClusterPeersResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_peers, request, FSxDescribeClusterPeersResponse)

    async def describe_cluster_peers_paginated(
        self,
        request: FSxDescribeClusterPeersRequest | None = None,
    ) -> list[FSxDescribeClusterPeersResponse]:
        return await self._paginate('describe_cluster_peers', request, FSxDescribeClusterPeersResponse)

    async def describe_data_repository_associations(
        self,
        request: FSxDescribeDataRepositoryAssociationsRequest | None = None,
    ) -> FSxDescribeDataRepositoryAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_repository_associations, request, FSxDescribeDataRepositoryAssociationsResponse)

    async def describe_data_repository_tasks(
        self,
        request: FSxDescribeDataRepositoryTasksRequest | None = None,
    ) -> FSxDescribeDataRepositoryTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_repository_tasks, request, FSxDescribeDataRepositoryTasksResponse)

    async def describe_file_caches(
        self,
        request: FSxDescribeFileCachesRequest | None = None,
    ) -> FSxDescribeFileCachesResponse:
        client = self._require_client()
        return await self._execute(client.describe_file_caches, request, FSxDescribeFileCachesResponse)

    async def describe_file_system_aliases(
        self,
        request: FSxDescribeFileSystemAliasesRequest,
    ) -> FSxDescribeFileSystemAliasesResponse:
        client = self._require_client()
        return await self._execute(client.describe_file_system_aliases, request, FSxDescribeFileSystemAliasesResponse)

    async def describe_file_systems(
        self,
        request: FSxDescribeFileSystemsRequest | None = None,
    ) -> FSxDescribeFileSystemsResponse:
        client = self._require_client()
        return await self._execute(client.describe_file_systems, request, FSxDescribeFileSystemsResponse)

    async def describe_file_systems_paginated(
        self,
        request: FSxDescribeFileSystemsRequest | None = None,
    ) -> list[FSxDescribeFileSystemsResponse]:
        return await self._paginate('describe_file_systems', request, FSxDescribeFileSystemsResponse)

    async def describe_s3_access_point_attachments(
        self,
        request: FSxDescribeS3AccessPointAttachmentsRequest | None = None,
    ) -> FSxDescribeS3AccessPointAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_s3_access_point_attachments, request, FSxDescribeS3AccessPointAttachmentsResponse)

    async def describe_s3_access_point_attachments_paginated(
        self,
        request: FSxDescribeS3AccessPointAttachmentsRequest | None = None,
    ) -> list[FSxDescribeS3AccessPointAttachmentsResponse]:
        return await self._paginate('describe_s3_access_point_attachments', request, FSxDescribeS3AccessPointAttachmentsResponse)

    async def describe_shared_vpc_configuration(
        self,
        request: FSxDescribeSharedVpcConfigurationRequest | None = None,
    ) -> FSxDescribeSharedVpcConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_shared_vpc_configuration, request, FSxDescribeSharedVpcConfigurationResponse)

    async def describe_snapmirror_policies(
        self,
        request: FSxDescribeSnapmirrorPoliciesRequest | None = None,
    ) -> FSxDescribeSnapmirrorPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapmirror_policies, request, FSxDescribeSnapmirrorPoliciesResponse)

    async def describe_snapmirror_policies_paginated(
        self,
        request: FSxDescribeSnapmirrorPoliciesRequest | None = None,
    ) -> list[FSxDescribeSnapmirrorPoliciesResponse]:
        return await self._paginate('describe_snapmirror_policies', request, FSxDescribeSnapmirrorPoliciesResponse)

    async def describe_snapmirror_relationships(
        self,
        request: FSxDescribeSnapmirrorRelationshipsRequest | None = None,
    ) -> FSxDescribeSnapmirrorRelationshipsResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapmirror_relationships, request, FSxDescribeSnapmirrorRelationshipsResponse)

    async def describe_snapmirror_relationships_paginated(
        self,
        request: FSxDescribeSnapmirrorRelationshipsRequest | None = None,
    ) -> list[FSxDescribeSnapmirrorRelationshipsResponse]:
        return await self._paginate('describe_snapmirror_relationships', request, FSxDescribeSnapmirrorRelationshipsResponse)

    async def describe_snapshot_policies(
        self,
        request: FSxDescribeSnapshotPoliciesRequest | None = None,
    ) -> FSxDescribeSnapshotPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshot_policies, request, FSxDescribeSnapshotPoliciesResponse)

    async def describe_snapshot_policies_paginated(
        self,
        request: FSxDescribeSnapshotPoliciesRequest | None = None,
    ) -> list[FSxDescribeSnapshotPoliciesResponse]:
        return await self._paginate('describe_snapshot_policies', request, FSxDescribeSnapshotPoliciesResponse)

    async def describe_snapshots(
        self,
        request: FSxDescribeSnapshotsRequest | None = None,
    ) -> FSxDescribeSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshots, request, FSxDescribeSnapshotsResponse)

    async def describe_snapshots_paginated(
        self,
        request: FSxDescribeSnapshotsRequest | None = None,
    ) -> list[FSxDescribeSnapshotsResponse]:
        return await self._paginate('describe_snapshots', request, FSxDescribeSnapshotsResponse)

    async def describe_storage_virtual_machine_peers(
        self,
        request: FSxDescribeStorageVirtualMachinePeersRequest | None = None,
    ) -> FSxDescribeStorageVirtualMachinePeersResponse:
        client = self._require_client()
        return await self._execute(client.describe_storage_virtual_machine_peers, request, FSxDescribeStorageVirtualMachinePeersResponse)

    async def describe_storage_virtual_machine_peers_paginated(
        self,
        request: FSxDescribeStorageVirtualMachinePeersRequest | None = None,
    ) -> list[FSxDescribeStorageVirtualMachinePeersResponse]:
        return await self._paginate('describe_storage_virtual_machine_peers', request, FSxDescribeStorageVirtualMachinePeersResponse)

    async def describe_storage_virtual_machines(
        self,
        request: FSxDescribeStorageVirtualMachinesRequest | None = None,
    ) -> FSxDescribeStorageVirtualMachinesResponse:
        client = self._require_client()
        return await self._execute(client.describe_storage_virtual_machines, request, FSxDescribeStorageVirtualMachinesResponse)

    async def describe_storage_virtual_machines_paginated(
        self,
        request: FSxDescribeStorageVirtualMachinesRequest | None = None,
    ) -> list[FSxDescribeStorageVirtualMachinesResponse]:
        return await self._paginate('describe_storage_virtual_machines', request, FSxDescribeStorageVirtualMachinesResponse)

    async def describe_volumes(
        self,
        request: FSxDescribeVolumesRequest | None = None,
    ) -> FSxDescribeVolumesResponse:
        client = self._require_client()
        return await self._execute(client.describe_volumes, request, FSxDescribeVolumesResponse)

    async def describe_volumes_paginated(
        self,
        request: FSxDescribeVolumesRequest | None = None,
    ) -> list[FSxDescribeVolumesResponse]:
        return await self._paginate('describe_volumes', request, FSxDescribeVolumesResponse)

    async def detach_and_delete_s3_access_point(
        self,
        request: FSxDetachAndDeleteS3AccessPointRequest,
    ) -> FSxDetachAndDeleteS3AccessPointResponse:
        client = self._require_client()
        return await self._execute(client.detach_and_delete_s3_access_point, request, FSxDetachAndDeleteS3AccessPointResponse)

    async def disassociate_file_system_aliases(
        self,
        request: FSxDisassociateFileSystemAliasesRequest,
    ) -> FSxDisassociateFileSystemAliasesResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_file_system_aliases, request, FSxDisassociateFileSystemAliasesResponse)

    async def list_tags_for_resource(
        self,
        request: FSxListTagsForResourceRequest,
    ) -> FSxListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, FSxListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: FSxListTagsForResourceRequest,
    ) -> list[FSxListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, FSxListTagsForResourceResponse)

    async def release_file_system_nfs_v3_locks(
        self,
        request: FSxReleaseFileSystemNfsV3LocksRequest,
    ) -> FSxReleaseFileSystemNfsV3LocksResponse:
        client = self._require_client()
        return await self._execute(client.release_file_system_nfs_v3_locks, request, FSxReleaseFileSystemNfsV3LocksResponse)

    async def restore_volume_from_snapshot(
        self,
        request: FSxRestoreVolumeFromSnapshotRequest,
    ) -> FSxRestoreVolumeFromSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.restore_volume_from_snapshot, request, FSxRestoreVolumeFromSnapshotResponse)

    async def start_misconfigured_state_recovery(
        self,
        request: FSxStartMisconfiguredStateRecoveryRequest,
    ) -> FSxStartMisconfiguredStateRecoveryResponse:
        client = self._require_client()
        return await self._execute(client.start_misconfigured_state_recovery, request, FSxStartMisconfiguredStateRecoveryResponse)

    async def tag_resource(
        self,
        request: FSxTagResourceRequest,
    ) -> FSxTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, FSxTagResourceResponse)

    async def untag_resource(
        self,
        request: FSxUntagResourceRequest,
    ) -> FSxUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, FSxUntagResourceResponse)

    async def update_cluster_peer(
        self,
        request: FSxUpdateClusterPeerRequest,
    ) -> FSxUpdateClusterPeerResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster_peer, request, FSxUpdateClusterPeerResponse)

    async def update_data_repository_association(
        self,
        request: FSxUpdateDataRepositoryAssociationRequest,
    ) -> FSxUpdateDataRepositoryAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_data_repository_association, request, FSxUpdateDataRepositoryAssociationResponse)

    async def update_file_cache(
        self,
        request: FSxUpdateFileCacheRequest,
    ) -> FSxUpdateFileCacheResponse:
        client = self._require_client()
        return await self._execute(client.update_file_cache, request, FSxUpdateFileCacheResponse)

    async def update_file_system(
        self,
        request: FSxUpdateFileSystemRequest,
    ) -> FSxUpdateFileSystemResponse:
        client = self._require_client()
        return await self._execute(client.update_file_system, request, FSxUpdateFileSystemResponse)

    async def update_shared_vpc_configuration(
        self,
        request: FSxUpdateSharedVpcConfigurationRequest | None = None,
    ) -> FSxUpdateSharedVpcConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_shared_vpc_configuration, request, FSxUpdateSharedVpcConfigurationResponse)

    async def update_snapmirror_policy(
        self,
        request: FSxUpdateSnapmirrorPolicyRequest,
    ) -> FSxUpdateSnapmirrorPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_snapmirror_policy, request, FSxUpdateSnapmirrorPolicyResponse)

    async def update_snapmirror_relationship(
        self,
        request: FSxUpdateSnapmirrorRelationshipRequest,
    ) -> FSxUpdateSnapmirrorRelationshipResponse:
        client = self._require_client()
        return await self._execute(client.update_snapmirror_relationship, request, FSxUpdateSnapmirrorRelationshipResponse)

    async def update_snapshot(
        self,
        request: FSxUpdateSnapshotRequest,
    ) -> FSxUpdateSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.update_snapshot, request, FSxUpdateSnapshotResponse)

    async def update_snapshot_policy(
        self,
        request: FSxUpdateSnapshotPolicyRequest,
    ) -> FSxUpdateSnapshotPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_snapshot_policy, request, FSxUpdateSnapshotPolicyResponse)

    async def update_storage_virtual_machine(
        self,
        request: FSxUpdateStorageVirtualMachineRequest,
    ) -> FSxUpdateStorageVirtualMachineResponse:
        client = self._require_client()
        return await self._execute(client.update_storage_virtual_machine, request, FSxUpdateStorageVirtualMachineResponse)

    async def update_storage_virtual_machine_peer(
        self,
        request: FSxUpdateStorageVirtualMachinePeerRequest,
    ) -> FSxUpdateStorageVirtualMachinePeerResponse:
        client = self._require_client()
        return await self._execute(client.update_storage_virtual_machine_peer, request, FSxUpdateStorageVirtualMachinePeerResponse)

    async def update_volume(
        self,
        request: FSxUpdateVolumeRequest,
    ) -> FSxUpdateVolumeResponse:
        client = self._require_client()
        return await self._execute(client.update_volume, request, FSxUpdateVolumeResponse)
