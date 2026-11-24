from werkflow_aws.models.efs import (
    EFSCreateAccessPointRequest,
    EFSCreateAccessPointResponse,
    EFSCreateFileSystemRequest,
    EFSCreateFileSystemResponse,
    EFSCreateMountTargetRequest,
    EFSCreateMountTargetResponse,
    EFSCreateReplicationConfigurationRequest,
    EFSCreateReplicationConfigurationResponse,
    EFSCreateTagsRequest,
    EFSCreateTagsResponse,
    EFSDeleteAccessPointRequest,
    EFSDeleteAccessPointResponse,
    EFSDeleteFileSystemPolicyRequest,
    EFSDeleteFileSystemPolicyResponse,
    EFSDeleteFileSystemRequest,
    EFSDeleteFileSystemResponse,
    EFSDeleteMountTargetRequest,
    EFSDeleteMountTargetResponse,
    EFSDeleteReplicationConfigurationRequest,
    EFSDeleteReplicationConfigurationResponse,
    EFSDeleteTagsRequest,
    EFSDeleteTagsResponse,
    EFSDescribeAccessPointsRequest,
    EFSDescribeAccessPointsResponse,
    EFSDescribeAccountPreferencesRequest,
    EFSDescribeAccountPreferencesResponse,
    EFSDescribeBackupPolicyRequest,
    EFSDescribeBackupPolicyResponse,
    EFSDescribeFileSystemPolicyRequest,
    EFSDescribeFileSystemPolicyResponse,
    EFSDescribeFileSystemsRequest,
    EFSDescribeFileSystemsResponse,
    EFSDescribeLifecycleConfigurationRequest,
    EFSDescribeLifecycleConfigurationResponse,
    EFSDescribeMountTargetSecurityGroupsRequest,
    EFSDescribeMountTargetSecurityGroupsResponse,
    EFSDescribeMountTargetsRequest,
    EFSDescribeMountTargetsResponse,
    EFSDescribeReplicationConfigurationsRequest,
    EFSDescribeReplicationConfigurationsResponse,
    EFSDescribeTagsRequest,
    EFSDescribeTagsResponse,
    EFSListTagsForResourceRequest,
    EFSListTagsForResourceResponse,
    EFSModifyMountTargetSecurityGroupsRequest,
    EFSModifyMountTargetSecurityGroupsResponse,
    EFSPutAccountPreferencesRequest,
    EFSPutAccountPreferencesResponse,
    EFSPutBackupPolicyRequest,
    EFSPutBackupPolicyResponse,
    EFSPutFileSystemPolicyRequest,
    EFSPutFileSystemPolicyResponse,
    EFSPutLifecycleConfigurationRequest,
    EFSPutLifecycleConfigurationResponse,
    EFSTagResourceRequest,
    EFSTagResourceResponse,
    EFSUntagResourceRequest,
    EFSUntagResourceResponse,
    EFSUpdateFileSystemProtectionRequest,
    EFSUpdateFileSystemProtectionResponse,
    EFSUpdateFileSystemRequest,
    EFSUpdateFileSystemResponse,
)
from werkflow_aws.types.efs_client import EFSClient
from .base import AWSBaseService


class AWSEFS(AWSBaseService[EFSClient]):
    service_name = 'efs'
    boto3_service_name = 'efs'

    def __init__(self) -> None:
        super().__init__(service_name='efs', boto3_service_name='efs')

    async def create_access_point(
        self,
        request: EFSCreateAccessPointRequest,
    ) -> EFSCreateAccessPointResponse:
        client = self._require_client()
        return await self._execute(client.create_access_point, request, EFSCreateAccessPointResponse)

    async def create_file_system(
        self,
        request: EFSCreateFileSystemRequest,
    ) -> EFSCreateFileSystemResponse:
        client = self._require_client()
        return await self._execute(client.create_file_system, request, EFSCreateFileSystemResponse)

    async def create_mount_target(
        self,
        request: EFSCreateMountTargetRequest,
    ) -> EFSCreateMountTargetResponse:
        client = self._require_client()
        return await self._execute(client.create_mount_target, request, EFSCreateMountTargetResponse)

    async def create_replication_configuration(
        self,
        request: EFSCreateReplicationConfigurationRequest,
    ) -> EFSCreateReplicationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_replication_configuration, request, EFSCreateReplicationConfigurationResponse)

    async def create_tags(
        self,
        request: EFSCreateTagsRequest,
    ) -> EFSCreateTagsResponse:
        client = self._require_client()
        return await self._execute(client.create_tags, request, EFSCreateTagsResponse)

    async def delete_access_point(
        self,
        request: EFSDeleteAccessPointRequest,
    ) -> EFSDeleteAccessPointResponse:
        client = self._require_client()
        return await self._execute(client.delete_access_point, request, EFSDeleteAccessPointResponse)

    async def delete_file_system(
        self,
        request: EFSDeleteFileSystemRequest,
    ) -> EFSDeleteFileSystemResponse:
        client = self._require_client()
        return await self._execute(client.delete_file_system, request, EFSDeleteFileSystemResponse)

    async def delete_file_system_policy(
        self,
        request: EFSDeleteFileSystemPolicyRequest,
    ) -> EFSDeleteFileSystemPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_file_system_policy, request, EFSDeleteFileSystemPolicyResponse)

    async def delete_mount_target(
        self,
        request: EFSDeleteMountTargetRequest,
    ) -> EFSDeleteMountTargetResponse:
        client = self._require_client()
        return await self._execute(client.delete_mount_target, request, EFSDeleteMountTargetResponse)

    async def delete_replication_configuration(
        self,
        request: EFSDeleteReplicationConfigurationRequest,
    ) -> EFSDeleteReplicationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_replication_configuration, request, EFSDeleteReplicationConfigurationResponse)

    async def delete_tags(
        self,
        request: EFSDeleteTagsRequest,
    ) -> EFSDeleteTagsResponse:
        client = self._require_client()
        return await self._execute(client.delete_tags, request, EFSDeleteTagsResponse)

    async def describe_access_points(
        self,
        request: EFSDescribeAccessPointsRequest | None = None,
    ) -> EFSDescribeAccessPointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_access_points, request, EFSDescribeAccessPointsResponse)

    async def describe_access_points_paginated(
        self,
        request: EFSDescribeAccessPointsRequest | None = None,
    ) -> list[EFSDescribeAccessPointsResponse]:
        return await self._paginate('describe_access_points', request, EFSDescribeAccessPointsResponse)

    async def describe_account_preferences(
        self,
        request: EFSDescribeAccountPreferencesRequest | None = None,
    ) -> EFSDescribeAccountPreferencesResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_preferences, request, EFSDescribeAccountPreferencesResponse)

    async def describe_backup_policy(
        self,
        request: EFSDescribeBackupPolicyRequest,
    ) -> EFSDescribeBackupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_backup_policy, request, EFSDescribeBackupPolicyResponse)

    async def describe_file_system_policy(
        self,
        request: EFSDescribeFileSystemPolicyRequest,
    ) -> EFSDescribeFileSystemPolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_file_system_policy, request, EFSDescribeFileSystemPolicyResponse)

    async def describe_file_systems(
        self,
        request: EFSDescribeFileSystemsRequest | None = None,
    ) -> EFSDescribeFileSystemsResponse:
        client = self._require_client()
        return await self._execute(client.describe_file_systems, request, EFSDescribeFileSystemsResponse)

    async def describe_file_systems_paginated(
        self,
        request: EFSDescribeFileSystemsRequest | None = None,
    ) -> list[EFSDescribeFileSystemsResponse]:
        return await self._paginate('describe_file_systems', request, EFSDescribeFileSystemsResponse)

    async def describe_lifecycle_configuration(
        self,
        request: EFSDescribeLifecycleConfigurationRequest,
    ) -> EFSDescribeLifecycleConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_lifecycle_configuration, request, EFSDescribeLifecycleConfigurationResponse)

    async def describe_mount_target_security_groups(
        self,
        request: EFSDescribeMountTargetSecurityGroupsRequest,
    ) -> EFSDescribeMountTargetSecurityGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_mount_target_security_groups, request, EFSDescribeMountTargetSecurityGroupsResponse)

    async def describe_mount_targets(
        self,
        request: EFSDescribeMountTargetsRequest | None = None,
    ) -> EFSDescribeMountTargetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_mount_targets, request, EFSDescribeMountTargetsResponse)

    async def describe_mount_targets_paginated(
        self,
        request: EFSDescribeMountTargetsRequest | None = None,
    ) -> list[EFSDescribeMountTargetsResponse]:
        return await self._paginate('describe_mount_targets', request, EFSDescribeMountTargetsResponse)

    async def describe_replication_configurations(
        self,
        request: EFSDescribeReplicationConfigurationsRequest | None = None,
    ) -> EFSDescribeReplicationConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_configurations, request, EFSDescribeReplicationConfigurationsResponse)

    async def describe_replication_configurations_paginated(
        self,
        request: EFSDescribeReplicationConfigurationsRequest | None = None,
    ) -> list[EFSDescribeReplicationConfigurationsResponse]:
        return await self._paginate('describe_replication_configurations', request, EFSDescribeReplicationConfigurationsResponse)

    async def describe_tags(
        self,
        request: EFSDescribeTagsRequest,
    ) -> EFSDescribeTagsResponse:
        client = self._require_client()
        return await self._execute(client.describe_tags, request, EFSDescribeTagsResponse)

    async def describe_tags_paginated(
        self,
        request: EFSDescribeTagsRequest,
    ) -> list[EFSDescribeTagsResponse]:
        return await self._paginate('describe_tags', request, EFSDescribeTagsResponse)

    async def list_tags_for_resource(
        self,
        request: EFSListTagsForResourceRequest,
    ) -> EFSListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, EFSListTagsForResourceResponse)

    async def modify_mount_target_security_groups(
        self,
        request: EFSModifyMountTargetSecurityGroupsRequest,
    ) -> EFSModifyMountTargetSecurityGroupsResponse:
        client = self._require_client()
        return await self._execute(client.modify_mount_target_security_groups, request, EFSModifyMountTargetSecurityGroupsResponse)

    async def put_account_preferences(
        self,
        request: EFSPutAccountPreferencesRequest,
    ) -> EFSPutAccountPreferencesResponse:
        client = self._require_client()
        return await self._execute(client.put_account_preferences, request, EFSPutAccountPreferencesResponse)

    async def put_backup_policy(
        self,
        request: EFSPutBackupPolicyRequest,
    ) -> EFSPutBackupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_backup_policy, request, EFSPutBackupPolicyResponse)

    async def put_file_system_policy(
        self,
        request: EFSPutFileSystemPolicyRequest,
    ) -> EFSPutFileSystemPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_file_system_policy, request, EFSPutFileSystemPolicyResponse)

    async def put_lifecycle_configuration(
        self,
        request: EFSPutLifecycleConfigurationRequest,
    ) -> EFSPutLifecycleConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_lifecycle_configuration, request, EFSPutLifecycleConfigurationResponse)

    async def tag_resource(
        self,
        request: EFSTagResourceRequest,
    ) -> EFSTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, EFSTagResourceResponse)

    async def untag_resource(
        self,
        request: EFSUntagResourceRequest,
    ) -> EFSUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, EFSUntagResourceResponse)

    async def update_file_system(
        self,
        request: EFSUpdateFileSystemRequest,
    ) -> EFSUpdateFileSystemResponse:
        client = self._require_client()
        return await self._execute(client.update_file_system, request, EFSUpdateFileSystemResponse)

    async def update_file_system_protection(
        self,
        request: EFSUpdateFileSystemProtectionRequest,
    ) -> EFSUpdateFileSystemProtectionResponse:
        client = self._require_client()
        return await self._execute(client.update_file_system_protection, request, EFSUpdateFileSystemProtectionResponse)
