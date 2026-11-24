from werkflow_aws.models.storage_gateway import (
    StorageGatewayActivateGatewayRequest,
    StorageGatewayActivateGatewayResponse,
    StorageGatewayAddCacheRequest,
    StorageGatewayAddCacheResponse,
    StorageGatewayAddTagsToResourceRequest,
    StorageGatewayAddTagsToResourceResponse,
    StorageGatewayAddUploadBufferRequest,
    StorageGatewayAddUploadBufferResponse,
    StorageGatewayAddWorkingStorageRequest,
    StorageGatewayAddWorkingStorageResponse,
    StorageGatewayAssignTapePoolRequest,
    StorageGatewayAssignTapePoolResponse,
    StorageGatewayAssociateFileSystemRequest,
    StorageGatewayAssociateFileSystemResponse,
    StorageGatewayAttachVolumeRequest,
    StorageGatewayAttachVolumeResponse,
    StorageGatewayCancelArchivalRequest,
    StorageGatewayCancelArchivalResponse,
    StorageGatewayCancelCacheReportRequest,
    StorageGatewayCancelCacheReportResponse,
    StorageGatewayCancelRetrievalRequest,
    StorageGatewayCancelRetrievalResponse,
    StorageGatewayCreateCachediSCSIVolumeRequest,
    StorageGatewayCreateCachediSCSIVolumeResponse,
    StorageGatewayCreateNFSFileShareRequest,
    StorageGatewayCreateNFSFileShareResponse,
    StorageGatewayCreateSMBFileShareRequest,
    StorageGatewayCreateSMBFileShareResponse,
    StorageGatewayCreateSnapshotFromVolumeRecoveryPointRequest,
    StorageGatewayCreateSnapshotFromVolumeRecoveryPointResponse,
    StorageGatewayCreateSnapshotRequest,
    StorageGatewayCreateSnapshotResponse,
    StorageGatewayCreateStorediSCSIVolumeRequest,
    StorageGatewayCreateStorediSCSIVolumeResponse,
    StorageGatewayCreateTapePoolRequest,
    StorageGatewayCreateTapePoolResponse,
    StorageGatewayCreateTapeWithBarcodeRequest,
    StorageGatewayCreateTapeWithBarcodeResponse,
    StorageGatewayCreateTapesRequest,
    StorageGatewayCreateTapesResponse,
    StorageGatewayDeleteAutomaticTapeCreationPolicyRequest,
    StorageGatewayDeleteAutomaticTapeCreationPolicyResponse,
    StorageGatewayDeleteBandwidthRateLimitRequest,
    StorageGatewayDeleteBandwidthRateLimitResponse,
    StorageGatewayDeleteCacheReportRequest,
    StorageGatewayDeleteCacheReportResponse,
    StorageGatewayDeleteChapCredentialsRequest,
    StorageGatewayDeleteChapCredentialsResponse,
    StorageGatewayDeleteFileShareRequest,
    StorageGatewayDeleteFileShareResponse,
    StorageGatewayDeleteGatewayRequest,
    StorageGatewayDeleteGatewayResponse,
    StorageGatewayDeleteSnapshotScheduleRequest,
    StorageGatewayDeleteSnapshotScheduleResponse,
    StorageGatewayDeleteTapeArchiveRequest,
    StorageGatewayDeleteTapeArchiveResponse,
    StorageGatewayDeleteTapePoolRequest,
    StorageGatewayDeleteTapePoolResponse,
    StorageGatewayDeleteTapeRequest,
    StorageGatewayDeleteTapeResponse,
    StorageGatewayDeleteVolumeRequest,
    StorageGatewayDeleteVolumeResponse,
    StorageGatewayDescribeAvailabilityMonitorTestRequest,
    StorageGatewayDescribeAvailabilityMonitorTestResponse,
    StorageGatewayDescribeBandwidthRateLimitRequest,
    StorageGatewayDescribeBandwidthRateLimitResponse,
    StorageGatewayDescribeBandwidthRateLimitScheduleRequest,
    StorageGatewayDescribeBandwidthRateLimitScheduleResponse,
    StorageGatewayDescribeCacheReportRequest,
    StorageGatewayDescribeCacheReportResponse,
    StorageGatewayDescribeCacheRequest,
    StorageGatewayDescribeCacheResponse,
    StorageGatewayDescribeCachediSCSIVolumesRequest,
    StorageGatewayDescribeCachediSCSIVolumesResponse,
    StorageGatewayDescribeChapCredentialsRequest,
    StorageGatewayDescribeChapCredentialsResponse,
    StorageGatewayDescribeFileSystemAssociationsRequest,
    StorageGatewayDescribeFileSystemAssociationsResponse,
    StorageGatewayDescribeGatewayInformationRequest,
    StorageGatewayDescribeGatewayInformationResponse,
    StorageGatewayDescribeMaintenanceStartTimeRequest,
    StorageGatewayDescribeMaintenanceStartTimeResponse,
    StorageGatewayDescribeNFSFileSharesRequest,
    StorageGatewayDescribeNFSFileSharesResponse,
    StorageGatewayDescribeSMBFileSharesRequest,
    StorageGatewayDescribeSMBFileSharesResponse,
    StorageGatewayDescribeSMBSettingsRequest,
    StorageGatewayDescribeSMBSettingsResponse,
    StorageGatewayDescribeSnapshotScheduleRequest,
    StorageGatewayDescribeSnapshotScheduleResponse,
    StorageGatewayDescribeStorediSCSIVolumesRequest,
    StorageGatewayDescribeStorediSCSIVolumesResponse,
    StorageGatewayDescribeTapeArchivesRequest,
    StorageGatewayDescribeTapeArchivesResponse,
    StorageGatewayDescribeTapeRecoveryPointsRequest,
    StorageGatewayDescribeTapeRecoveryPointsResponse,
    StorageGatewayDescribeTapesRequest,
    StorageGatewayDescribeTapesResponse,
    StorageGatewayDescribeUploadBufferRequest,
    StorageGatewayDescribeUploadBufferResponse,
    StorageGatewayDescribeVTLDevicesRequest,
    StorageGatewayDescribeVTLDevicesResponse,
    StorageGatewayDescribeWorkingStorageRequest,
    StorageGatewayDescribeWorkingStorageResponse,
    StorageGatewayDetachVolumeRequest,
    StorageGatewayDetachVolumeResponse,
    StorageGatewayDisableGatewayRequest,
    StorageGatewayDisableGatewayResponse,
    StorageGatewayDisassociateFileSystemRequest,
    StorageGatewayDisassociateFileSystemResponse,
    StorageGatewayEvictFilesFailingUploadRequest,
    StorageGatewayEvictFilesFailingUploadResponse,
    StorageGatewayJoinDomainRequest,
    StorageGatewayJoinDomainResponse,
    StorageGatewayListAutomaticTapeCreationPoliciesRequest,
    StorageGatewayListAutomaticTapeCreationPoliciesResponse,
    StorageGatewayListCacheReportsRequest,
    StorageGatewayListCacheReportsResponse,
    StorageGatewayListFileSharesRequest,
    StorageGatewayListFileSharesResponse,
    StorageGatewayListFileSystemAssociationsRequest,
    StorageGatewayListFileSystemAssociationsResponse,
    StorageGatewayListGatewaysRequest,
    StorageGatewayListGatewaysResponse,
    StorageGatewayListLocalDisksRequest,
    StorageGatewayListLocalDisksResponse,
    StorageGatewayListTagsForResourceRequest,
    StorageGatewayListTagsForResourceResponse,
    StorageGatewayListTapePoolsRequest,
    StorageGatewayListTapePoolsResponse,
    StorageGatewayListTapesRequest,
    StorageGatewayListTapesResponse,
    StorageGatewayListVolumeInitiatorsRequest,
    StorageGatewayListVolumeInitiatorsResponse,
    StorageGatewayListVolumeRecoveryPointsRequest,
    StorageGatewayListVolumeRecoveryPointsResponse,
    StorageGatewayListVolumesRequest,
    StorageGatewayListVolumesResponse,
    StorageGatewayNotifyWhenUploadedRequest,
    StorageGatewayNotifyWhenUploadedResponse,
    StorageGatewayRefreshCacheRequest,
    StorageGatewayRefreshCacheResponse,
    StorageGatewayRemoveTagsFromResourceRequest,
    StorageGatewayRemoveTagsFromResourceResponse,
    StorageGatewayResetCacheRequest,
    StorageGatewayResetCacheResponse,
    StorageGatewayRetrieveTapeArchiveRequest,
    StorageGatewayRetrieveTapeArchiveResponse,
    StorageGatewayRetrieveTapeRecoveryPointRequest,
    StorageGatewayRetrieveTapeRecoveryPointResponse,
    StorageGatewaySetLocalConsolePasswordRequest,
    StorageGatewaySetLocalConsolePasswordResponse,
    StorageGatewaySetSMBGuestPasswordRequest,
    StorageGatewaySetSMBGuestPasswordResponse,
    StorageGatewayShutdownGatewayRequest,
    StorageGatewayShutdownGatewayResponse,
    StorageGatewayStartAvailabilityMonitorTestRequest,
    StorageGatewayStartAvailabilityMonitorTestResponse,
    StorageGatewayStartCacheReportRequest,
    StorageGatewayStartCacheReportResponse,
    StorageGatewayStartGatewayRequest,
    StorageGatewayStartGatewayResponse,
    StorageGatewayUpdateAutomaticTapeCreationPolicyRequest,
    StorageGatewayUpdateAutomaticTapeCreationPolicyResponse,
    StorageGatewayUpdateBandwidthRateLimitRequest,
    StorageGatewayUpdateBandwidthRateLimitResponse,
    StorageGatewayUpdateBandwidthRateLimitScheduleRequest,
    StorageGatewayUpdateBandwidthRateLimitScheduleResponse,
    StorageGatewayUpdateChapCredentialsRequest,
    StorageGatewayUpdateChapCredentialsResponse,
    StorageGatewayUpdateFileSystemAssociationRequest,
    StorageGatewayUpdateFileSystemAssociationResponse,
    StorageGatewayUpdateGatewayInformationRequest,
    StorageGatewayUpdateGatewayInformationResponse,
    StorageGatewayUpdateGatewaySoftwareNowRequest,
    StorageGatewayUpdateGatewaySoftwareNowResponse,
    StorageGatewayUpdateMaintenanceStartTimeRequest,
    StorageGatewayUpdateMaintenanceStartTimeResponse,
    StorageGatewayUpdateNFSFileShareRequest,
    StorageGatewayUpdateNFSFileShareResponse,
    StorageGatewayUpdateSMBFileShareRequest,
    StorageGatewayUpdateSMBFileShareResponse,
    StorageGatewayUpdateSMBFileShareVisibilityRequest,
    StorageGatewayUpdateSMBFileShareVisibilityResponse,
    StorageGatewayUpdateSMBLocalGroupsRequest,
    StorageGatewayUpdateSMBLocalGroupsResponse,
    StorageGatewayUpdateSMBSecurityStrategyRequest,
    StorageGatewayUpdateSMBSecurityStrategyResponse,
    StorageGatewayUpdateSnapshotScheduleRequest,
    StorageGatewayUpdateSnapshotScheduleResponse,
    StorageGatewayUpdateVTLDeviceTypeRequest,
    StorageGatewayUpdateVTLDeviceTypeResponse,
)
from werkflow_aws.types.storage_gateway_client import StorageGatewayClient
from .base import AWSBaseService


class AWSStorageGateway(AWSBaseService[StorageGatewayClient]):
    service_name = 'storage-gateway'
    boto3_service_name = 'storagegateway'

    def __init__(self) -> None:
        super().__init__(service_name='storage-gateway', boto3_service_name='storagegateway')

    async def activate_gateway(
        self,
        request: StorageGatewayActivateGatewayRequest,
    ) -> StorageGatewayActivateGatewayResponse:
        client = self._require_client()
        return await self._execute(client.activate_gateway, request, StorageGatewayActivateGatewayResponse)

    async def add_cache(
        self,
        request: StorageGatewayAddCacheRequest,
    ) -> StorageGatewayAddCacheResponse:
        client = self._require_client()
        return await self._execute(client.add_cache, request, StorageGatewayAddCacheResponse)

    async def add_tags_to_resource(
        self,
        request: StorageGatewayAddTagsToResourceRequest,
    ) -> StorageGatewayAddTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_resource, request, StorageGatewayAddTagsToResourceResponse)

    async def add_upload_buffer(
        self,
        request: StorageGatewayAddUploadBufferRequest,
    ) -> StorageGatewayAddUploadBufferResponse:
        client = self._require_client()
        return await self._execute(client.add_upload_buffer, request, StorageGatewayAddUploadBufferResponse)

    async def add_working_storage(
        self,
        request: StorageGatewayAddWorkingStorageRequest,
    ) -> StorageGatewayAddWorkingStorageResponse:
        client = self._require_client()
        return await self._execute(client.add_working_storage, request, StorageGatewayAddWorkingStorageResponse)

    async def assign_tape_pool(
        self,
        request: StorageGatewayAssignTapePoolRequest,
    ) -> StorageGatewayAssignTapePoolResponse:
        client = self._require_client()
        return await self._execute(client.assign_tape_pool, request, StorageGatewayAssignTapePoolResponse)

    async def associate_file_system(
        self,
        request: StorageGatewayAssociateFileSystemRequest,
    ) -> StorageGatewayAssociateFileSystemResponse:
        client = self._require_client()
        return await self._execute(client.associate_file_system, request, StorageGatewayAssociateFileSystemResponse)

    async def attach_volume(
        self,
        request: StorageGatewayAttachVolumeRequest,
    ) -> StorageGatewayAttachVolumeResponse:
        client = self._require_client()
        return await self._execute(client.attach_volume, request, StorageGatewayAttachVolumeResponse)

    async def cancel_archival(
        self,
        request: StorageGatewayCancelArchivalRequest,
    ) -> StorageGatewayCancelArchivalResponse:
        client = self._require_client()
        return await self._execute(client.cancel_archival, request, StorageGatewayCancelArchivalResponse)

    async def cancel_cache_report(
        self,
        request: StorageGatewayCancelCacheReportRequest,
    ) -> StorageGatewayCancelCacheReportResponse:
        client = self._require_client()
        return await self._execute(client.cancel_cache_report, request, StorageGatewayCancelCacheReportResponse)

    async def cancel_retrieval(
        self,
        request: StorageGatewayCancelRetrievalRequest,
    ) -> StorageGatewayCancelRetrievalResponse:
        client = self._require_client()
        return await self._execute(client.cancel_retrieval, request, StorageGatewayCancelRetrievalResponse)

    async def create_cached_iscsi_volume(
        self,
        request: StorageGatewayCreateCachediSCSIVolumeRequest,
    ) -> StorageGatewayCreateCachediSCSIVolumeResponse:
        client = self._require_client()
        return await self._execute(client.create_cached_iscsi_volume, request, StorageGatewayCreateCachediSCSIVolumeResponse)

    async def create_nfs_file_share(
        self,
        request: StorageGatewayCreateNFSFileShareRequest,
    ) -> StorageGatewayCreateNFSFileShareResponse:
        client = self._require_client()
        return await self._execute(client.create_nfs_file_share, request, StorageGatewayCreateNFSFileShareResponse)

    async def create_smb_file_share(
        self,
        request: StorageGatewayCreateSMBFileShareRequest,
    ) -> StorageGatewayCreateSMBFileShareResponse:
        client = self._require_client()
        return await self._execute(client.create_smb_file_share, request, StorageGatewayCreateSMBFileShareResponse)

    async def create_snapshot(
        self,
        request: StorageGatewayCreateSnapshotRequest,
    ) -> StorageGatewayCreateSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot, request, StorageGatewayCreateSnapshotResponse)

    async def create_snapshot_from_volume_recovery_point(
        self,
        request: StorageGatewayCreateSnapshotFromVolumeRecoveryPointRequest,
    ) -> StorageGatewayCreateSnapshotFromVolumeRecoveryPointResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot_from_volume_recovery_point, request, StorageGatewayCreateSnapshotFromVolumeRecoveryPointResponse)

    async def create_stored_iscsi_volume(
        self,
        request: StorageGatewayCreateStorediSCSIVolumeRequest,
    ) -> StorageGatewayCreateStorediSCSIVolumeResponse:
        client = self._require_client()
        return await self._execute(client.create_stored_iscsi_volume, request, StorageGatewayCreateStorediSCSIVolumeResponse)

    async def create_tape_pool(
        self,
        request: StorageGatewayCreateTapePoolRequest,
    ) -> StorageGatewayCreateTapePoolResponse:
        client = self._require_client()
        return await self._execute(client.create_tape_pool, request, StorageGatewayCreateTapePoolResponse)

    async def create_tape_with_barcode(
        self,
        request: StorageGatewayCreateTapeWithBarcodeRequest,
    ) -> StorageGatewayCreateTapeWithBarcodeResponse:
        client = self._require_client()
        return await self._execute(client.create_tape_with_barcode, request, StorageGatewayCreateTapeWithBarcodeResponse)

    async def create_tapes(
        self,
        request: StorageGatewayCreateTapesRequest,
    ) -> StorageGatewayCreateTapesResponse:
        client = self._require_client()
        return await self._execute(client.create_tapes, request, StorageGatewayCreateTapesResponse)

    async def delete_automatic_tape_creation_policy(
        self,
        request: StorageGatewayDeleteAutomaticTapeCreationPolicyRequest,
    ) -> StorageGatewayDeleteAutomaticTapeCreationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_automatic_tape_creation_policy, request, StorageGatewayDeleteAutomaticTapeCreationPolicyResponse)

    async def delete_bandwidth_rate_limit(
        self,
        request: StorageGatewayDeleteBandwidthRateLimitRequest,
    ) -> StorageGatewayDeleteBandwidthRateLimitResponse:
        client = self._require_client()
        return await self._execute(client.delete_bandwidth_rate_limit, request, StorageGatewayDeleteBandwidthRateLimitResponse)

    async def delete_cache_report(
        self,
        request: StorageGatewayDeleteCacheReportRequest,
    ) -> StorageGatewayDeleteCacheReportResponse:
        client = self._require_client()
        return await self._execute(client.delete_cache_report, request, StorageGatewayDeleteCacheReportResponse)

    async def delete_chap_credentials(
        self,
        request: StorageGatewayDeleteChapCredentialsRequest,
    ) -> StorageGatewayDeleteChapCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.delete_chap_credentials, request, StorageGatewayDeleteChapCredentialsResponse)

    async def delete_file_share(
        self,
        request: StorageGatewayDeleteFileShareRequest,
    ) -> StorageGatewayDeleteFileShareResponse:
        client = self._require_client()
        return await self._execute(client.delete_file_share, request, StorageGatewayDeleteFileShareResponse)

    async def delete_gateway(
        self,
        request: StorageGatewayDeleteGatewayRequest,
    ) -> StorageGatewayDeleteGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_gateway, request, StorageGatewayDeleteGatewayResponse)

    async def delete_snapshot_schedule(
        self,
        request: StorageGatewayDeleteSnapshotScheduleRequest,
    ) -> StorageGatewayDeleteSnapshotScheduleResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot_schedule, request, StorageGatewayDeleteSnapshotScheduleResponse)

    async def delete_tape(
        self,
        request: StorageGatewayDeleteTapeRequest,
    ) -> StorageGatewayDeleteTapeResponse:
        client = self._require_client()
        return await self._execute(client.delete_tape, request, StorageGatewayDeleteTapeResponse)

    async def delete_tape_archive(
        self,
        request: StorageGatewayDeleteTapeArchiveRequest,
    ) -> StorageGatewayDeleteTapeArchiveResponse:
        client = self._require_client()
        return await self._execute(client.delete_tape_archive, request, StorageGatewayDeleteTapeArchiveResponse)

    async def delete_tape_pool(
        self,
        request: StorageGatewayDeleteTapePoolRequest,
    ) -> StorageGatewayDeleteTapePoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_tape_pool, request, StorageGatewayDeleteTapePoolResponse)

    async def delete_volume(
        self,
        request: StorageGatewayDeleteVolumeRequest,
    ) -> StorageGatewayDeleteVolumeResponse:
        client = self._require_client()
        return await self._execute(client.delete_volume, request, StorageGatewayDeleteVolumeResponse)

    async def describe_availability_monitor_test(
        self,
        request: StorageGatewayDescribeAvailabilityMonitorTestRequest,
    ) -> StorageGatewayDescribeAvailabilityMonitorTestResponse:
        client = self._require_client()
        return await self._execute(client.describe_availability_monitor_test, request, StorageGatewayDescribeAvailabilityMonitorTestResponse)

    async def describe_bandwidth_rate_limit(
        self,
        request: StorageGatewayDescribeBandwidthRateLimitRequest,
    ) -> StorageGatewayDescribeBandwidthRateLimitResponse:
        client = self._require_client()
        return await self._execute(client.describe_bandwidth_rate_limit, request, StorageGatewayDescribeBandwidthRateLimitResponse)

    async def describe_bandwidth_rate_limit_schedule(
        self,
        request: StorageGatewayDescribeBandwidthRateLimitScheduleRequest,
    ) -> StorageGatewayDescribeBandwidthRateLimitScheduleResponse:
        client = self._require_client()
        return await self._execute(client.describe_bandwidth_rate_limit_schedule, request, StorageGatewayDescribeBandwidthRateLimitScheduleResponse)

    async def describe_cache(
        self,
        request: StorageGatewayDescribeCacheRequest,
    ) -> StorageGatewayDescribeCacheResponse:
        client = self._require_client()
        return await self._execute(client.describe_cache, request, StorageGatewayDescribeCacheResponse)

    async def describe_cache_report(
        self,
        request: StorageGatewayDescribeCacheReportRequest,
    ) -> StorageGatewayDescribeCacheReportResponse:
        client = self._require_client()
        return await self._execute(client.describe_cache_report, request, StorageGatewayDescribeCacheReportResponse)

    async def describe_cached_iscsi_volumes(
        self,
        request: StorageGatewayDescribeCachediSCSIVolumesRequest,
    ) -> StorageGatewayDescribeCachediSCSIVolumesResponse:
        client = self._require_client()
        return await self._execute(client.describe_cached_iscsi_volumes, request, StorageGatewayDescribeCachediSCSIVolumesResponse)

    async def describe_chap_credentials(
        self,
        request: StorageGatewayDescribeChapCredentialsRequest,
    ) -> StorageGatewayDescribeChapCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.describe_chap_credentials, request, StorageGatewayDescribeChapCredentialsResponse)

    async def describe_file_system_associations(
        self,
        request: StorageGatewayDescribeFileSystemAssociationsRequest,
    ) -> StorageGatewayDescribeFileSystemAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_file_system_associations, request, StorageGatewayDescribeFileSystemAssociationsResponse)

    async def describe_gateway_information(
        self,
        request: StorageGatewayDescribeGatewayInformationRequest,
    ) -> StorageGatewayDescribeGatewayInformationResponse:
        client = self._require_client()
        return await self._execute(client.describe_gateway_information, request, StorageGatewayDescribeGatewayInformationResponse)

    async def describe_maintenance_start_time(
        self,
        request: StorageGatewayDescribeMaintenanceStartTimeRequest,
    ) -> StorageGatewayDescribeMaintenanceStartTimeResponse:
        client = self._require_client()
        return await self._execute(client.describe_maintenance_start_time, request, StorageGatewayDescribeMaintenanceStartTimeResponse)

    async def describe_nfs_file_shares(
        self,
        request: StorageGatewayDescribeNFSFileSharesRequest,
    ) -> StorageGatewayDescribeNFSFileSharesResponse:
        client = self._require_client()
        return await self._execute(client.describe_nfs_file_shares, request, StorageGatewayDescribeNFSFileSharesResponse)

    async def describe_smb_file_shares(
        self,
        request: StorageGatewayDescribeSMBFileSharesRequest,
    ) -> StorageGatewayDescribeSMBFileSharesResponse:
        client = self._require_client()
        return await self._execute(client.describe_smb_file_shares, request, StorageGatewayDescribeSMBFileSharesResponse)

    async def describe_smb_settings(
        self,
        request: StorageGatewayDescribeSMBSettingsRequest,
    ) -> StorageGatewayDescribeSMBSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_smb_settings, request, StorageGatewayDescribeSMBSettingsResponse)

    async def describe_snapshot_schedule(
        self,
        request: StorageGatewayDescribeSnapshotScheduleRequest,
    ) -> StorageGatewayDescribeSnapshotScheduleResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshot_schedule, request, StorageGatewayDescribeSnapshotScheduleResponse)

    async def describe_stored_iscsi_volumes(
        self,
        request: StorageGatewayDescribeStorediSCSIVolumesRequest,
    ) -> StorageGatewayDescribeStorediSCSIVolumesResponse:
        client = self._require_client()
        return await self._execute(client.describe_stored_iscsi_volumes, request, StorageGatewayDescribeStorediSCSIVolumesResponse)

    async def describe_tape_archives(
        self,
        request: StorageGatewayDescribeTapeArchivesRequest | None = None,
    ) -> StorageGatewayDescribeTapeArchivesResponse:
        client = self._require_client()
        return await self._execute(client.describe_tape_archives, request, StorageGatewayDescribeTapeArchivesResponse)

    async def describe_tape_archives_paginated(
        self,
        request: StorageGatewayDescribeTapeArchivesRequest | None = None,
    ) -> list[StorageGatewayDescribeTapeArchivesResponse]:
        return await self._paginate('describe_tape_archives', request, StorageGatewayDescribeTapeArchivesResponse)

    async def describe_tape_recovery_points(
        self,
        request: StorageGatewayDescribeTapeRecoveryPointsRequest,
    ) -> StorageGatewayDescribeTapeRecoveryPointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_tape_recovery_points, request, StorageGatewayDescribeTapeRecoveryPointsResponse)

    async def describe_tape_recovery_points_paginated(
        self,
        request: StorageGatewayDescribeTapeRecoveryPointsRequest,
    ) -> list[StorageGatewayDescribeTapeRecoveryPointsResponse]:
        return await self._paginate('describe_tape_recovery_points', request, StorageGatewayDescribeTapeRecoveryPointsResponse)

    async def describe_tapes(
        self,
        request: StorageGatewayDescribeTapesRequest,
    ) -> StorageGatewayDescribeTapesResponse:
        client = self._require_client()
        return await self._execute(client.describe_tapes, request, StorageGatewayDescribeTapesResponse)

    async def describe_tapes_paginated(
        self,
        request: StorageGatewayDescribeTapesRequest,
    ) -> list[StorageGatewayDescribeTapesResponse]:
        return await self._paginate('describe_tapes', request, StorageGatewayDescribeTapesResponse)

    async def describe_upload_buffer(
        self,
        request: StorageGatewayDescribeUploadBufferRequest,
    ) -> StorageGatewayDescribeUploadBufferResponse:
        client = self._require_client()
        return await self._execute(client.describe_upload_buffer, request, StorageGatewayDescribeUploadBufferResponse)

    async def describe_vtl_devices(
        self,
        request: StorageGatewayDescribeVTLDevicesRequest,
    ) -> StorageGatewayDescribeVTLDevicesResponse:
        client = self._require_client()
        return await self._execute(client.describe_vtl_devices, request, StorageGatewayDescribeVTLDevicesResponse)

    async def describe_vtl_devices_paginated(
        self,
        request: StorageGatewayDescribeVTLDevicesRequest,
    ) -> list[StorageGatewayDescribeVTLDevicesResponse]:
        return await self._paginate('describe_vtl_devices', request, StorageGatewayDescribeVTLDevicesResponse)

    async def describe_working_storage(
        self,
        request: StorageGatewayDescribeWorkingStorageRequest,
    ) -> StorageGatewayDescribeWorkingStorageResponse:
        client = self._require_client()
        return await self._execute(client.describe_working_storage, request, StorageGatewayDescribeWorkingStorageResponse)

    async def detach_volume(
        self,
        request: StorageGatewayDetachVolumeRequest,
    ) -> StorageGatewayDetachVolumeResponse:
        client = self._require_client()
        return await self._execute(client.detach_volume, request, StorageGatewayDetachVolumeResponse)

    async def disable_gateway(
        self,
        request: StorageGatewayDisableGatewayRequest,
    ) -> StorageGatewayDisableGatewayResponse:
        client = self._require_client()
        return await self._execute(client.disable_gateway, request, StorageGatewayDisableGatewayResponse)

    async def disassociate_file_system(
        self,
        request: StorageGatewayDisassociateFileSystemRequest,
    ) -> StorageGatewayDisassociateFileSystemResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_file_system, request, StorageGatewayDisassociateFileSystemResponse)

    async def evict_files_failing_upload(
        self,
        request: StorageGatewayEvictFilesFailingUploadRequest,
    ) -> StorageGatewayEvictFilesFailingUploadResponse:
        client = self._require_client()
        return await self._execute(client.evict_files_failing_upload, request, StorageGatewayEvictFilesFailingUploadResponse)

    async def join_domain(
        self,
        request: StorageGatewayJoinDomainRequest,
    ) -> StorageGatewayJoinDomainResponse:
        client = self._require_client()
        return await self._execute(client.join_domain, request, StorageGatewayJoinDomainResponse)

    async def list_automatic_tape_creation_policies(
        self,
        request: StorageGatewayListAutomaticTapeCreationPoliciesRequest | None = None,
    ) -> StorageGatewayListAutomaticTapeCreationPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_automatic_tape_creation_policies, request, StorageGatewayListAutomaticTapeCreationPoliciesResponse)

    async def list_cache_reports(
        self,
        request: StorageGatewayListCacheReportsRequest | None = None,
    ) -> StorageGatewayListCacheReportsResponse:
        client = self._require_client()
        return await self._execute(client.list_cache_reports, request, StorageGatewayListCacheReportsResponse)

    async def list_cache_reports_paginated(
        self,
        request: StorageGatewayListCacheReportsRequest | None = None,
    ) -> list[StorageGatewayListCacheReportsResponse]:
        return await self._paginate('list_cache_reports', request, StorageGatewayListCacheReportsResponse)

    async def list_file_shares(
        self,
        request: StorageGatewayListFileSharesRequest | None = None,
    ) -> StorageGatewayListFileSharesResponse:
        client = self._require_client()
        return await self._execute(client.list_file_shares, request, StorageGatewayListFileSharesResponse)

    async def list_file_shares_paginated(
        self,
        request: StorageGatewayListFileSharesRequest | None = None,
    ) -> list[StorageGatewayListFileSharesResponse]:
        return await self._paginate('list_file_shares', request, StorageGatewayListFileSharesResponse)

    async def list_file_system_associations(
        self,
        request: StorageGatewayListFileSystemAssociationsRequest | None = None,
    ) -> StorageGatewayListFileSystemAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_file_system_associations, request, StorageGatewayListFileSystemAssociationsResponse)

    async def list_file_system_associations_paginated(
        self,
        request: StorageGatewayListFileSystemAssociationsRequest | None = None,
    ) -> list[StorageGatewayListFileSystemAssociationsResponse]:
        return await self._paginate('list_file_system_associations', request, StorageGatewayListFileSystemAssociationsResponse)

    async def list_gateways(
        self,
        request: StorageGatewayListGatewaysRequest | None = None,
    ) -> StorageGatewayListGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.list_gateways, request, StorageGatewayListGatewaysResponse)

    async def list_gateways_paginated(
        self,
        request: StorageGatewayListGatewaysRequest | None = None,
    ) -> list[StorageGatewayListGatewaysResponse]:
        return await self._paginate('list_gateways', request, StorageGatewayListGatewaysResponse)

    async def list_local_disks(
        self,
        request: StorageGatewayListLocalDisksRequest,
    ) -> StorageGatewayListLocalDisksResponse:
        client = self._require_client()
        return await self._execute(client.list_local_disks, request, StorageGatewayListLocalDisksResponse)

    async def list_tags_for_resource(
        self,
        request: StorageGatewayListTagsForResourceRequest,
    ) -> StorageGatewayListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, StorageGatewayListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: StorageGatewayListTagsForResourceRequest,
    ) -> list[StorageGatewayListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, StorageGatewayListTagsForResourceResponse)

    async def list_tape_pools(
        self,
        request: StorageGatewayListTapePoolsRequest | None = None,
    ) -> StorageGatewayListTapePoolsResponse:
        client = self._require_client()
        return await self._execute(client.list_tape_pools, request, StorageGatewayListTapePoolsResponse)

    async def list_tape_pools_paginated(
        self,
        request: StorageGatewayListTapePoolsRequest | None = None,
    ) -> list[StorageGatewayListTapePoolsResponse]:
        return await self._paginate('list_tape_pools', request, StorageGatewayListTapePoolsResponse)

    async def list_tapes(
        self,
        request: StorageGatewayListTapesRequest | None = None,
    ) -> StorageGatewayListTapesResponse:
        client = self._require_client()
        return await self._execute(client.list_tapes, request, StorageGatewayListTapesResponse)

    async def list_tapes_paginated(
        self,
        request: StorageGatewayListTapesRequest | None = None,
    ) -> list[StorageGatewayListTapesResponse]:
        return await self._paginate('list_tapes', request, StorageGatewayListTapesResponse)

    async def list_volume_initiators(
        self,
        request: StorageGatewayListVolumeInitiatorsRequest,
    ) -> StorageGatewayListVolumeInitiatorsResponse:
        client = self._require_client()
        return await self._execute(client.list_volume_initiators, request, StorageGatewayListVolumeInitiatorsResponse)

    async def list_volume_recovery_points(
        self,
        request: StorageGatewayListVolumeRecoveryPointsRequest,
    ) -> StorageGatewayListVolumeRecoveryPointsResponse:
        client = self._require_client()
        return await self._execute(client.list_volume_recovery_points, request, StorageGatewayListVolumeRecoveryPointsResponse)

    async def list_volumes(
        self,
        request: StorageGatewayListVolumesRequest | None = None,
    ) -> StorageGatewayListVolumesResponse:
        client = self._require_client()
        return await self._execute(client.list_volumes, request, StorageGatewayListVolumesResponse)

    async def list_volumes_paginated(
        self,
        request: StorageGatewayListVolumesRequest | None = None,
    ) -> list[StorageGatewayListVolumesResponse]:
        return await self._paginate('list_volumes', request, StorageGatewayListVolumesResponse)

    async def notify_when_uploaded(
        self,
        request: StorageGatewayNotifyWhenUploadedRequest,
    ) -> StorageGatewayNotifyWhenUploadedResponse:
        client = self._require_client()
        return await self._execute(client.notify_when_uploaded, request, StorageGatewayNotifyWhenUploadedResponse)

    async def refresh_cache(
        self,
        request: StorageGatewayRefreshCacheRequest,
    ) -> StorageGatewayRefreshCacheResponse:
        client = self._require_client()
        return await self._execute(client.refresh_cache, request, StorageGatewayRefreshCacheResponse)

    async def remove_tags_from_resource(
        self,
        request: StorageGatewayRemoveTagsFromResourceRequest,
    ) -> StorageGatewayRemoveTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_resource, request, StorageGatewayRemoveTagsFromResourceResponse)

    async def reset_cache(
        self,
        request: StorageGatewayResetCacheRequest,
    ) -> StorageGatewayResetCacheResponse:
        client = self._require_client()
        return await self._execute(client.reset_cache, request, StorageGatewayResetCacheResponse)

    async def retrieve_tape_archive(
        self,
        request: StorageGatewayRetrieveTapeArchiveRequest,
    ) -> StorageGatewayRetrieveTapeArchiveResponse:
        client = self._require_client()
        return await self._execute(client.retrieve_tape_archive, request, StorageGatewayRetrieveTapeArchiveResponse)

    async def retrieve_tape_recovery_point(
        self,
        request: StorageGatewayRetrieveTapeRecoveryPointRequest,
    ) -> StorageGatewayRetrieveTapeRecoveryPointResponse:
        client = self._require_client()
        return await self._execute(client.retrieve_tape_recovery_point, request, StorageGatewayRetrieveTapeRecoveryPointResponse)

    async def set_local_console_password(
        self,
        request: StorageGatewaySetLocalConsolePasswordRequest,
    ) -> StorageGatewaySetLocalConsolePasswordResponse:
        client = self._require_client()
        return await self._execute(client.set_local_console_password, request, StorageGatewaySetLocalConsolePasswordResponse)

    async def set_smb_guest_password(
        self,
        request: StorageGatewaySetSMBGuestPasswordRequest,
    ) -> StorageGatewaySetSMBGuestPasswordResponse:
        client = self._require_client()
        return await self._execute(client.set_smb_guest_password, request, StorageGatewaySetSMBGuestPasswordResponse)

    async def shutdown_gateway(
        self,
        request: StorageGatewayShutdownGatewayRequest,
    ) -> StorageGatewayShutdownGatewayResponse:
        client = self._require_client()
        return await self._execute(client.shutdown_gateway, request, StorageGatewayShutdownGatewayResponse)

    async def start_availability_monitor_test(
        self,
        request: StorageGatewayStartAvailabilityMonitorTestRequest,
    ) -> StorageGatewayStartAvailabilityMonitorTestResponse:
        client = self._require_client()
        return await self._execute(client.start_availability_monitor_test, request, StorageGatewayStartAvailabilityMonitorTestResponse)

    async def start_cache_report(
        self,
        request: StorageGatewayStartCacheReportRequest,
    ) -> StorageGatewayStartCacheReportResponse:
        client = self._require_client()
        return await self._execute(client.start_cache_report, request, StorageGatewayStartCacheReportResponse)

    async def start_gateway(
        self,
        request: StorageGatewayStartGatewayRequest,
    ) -> StorageGatewayStartGatewayResponse:
        client = self._require_client()
        return await self._execute(client.start_gateway, request, StorageGatewayStartGatewayResponse)

    async def update_automatic_tape_creation_policy(
        self,
        request: StorageGatewayUpdateAutomaticTapeCreationPolicyRequest,
    ) -> StorageGatewayUpdateAutomaticTapeCreationPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_automatic_tape_creation_policy, request, StorageGatewayUpdateAutomaticTapeCreationPolicyResponse)

    async def update_bandwidth_rate_limit(
        self,
        request: StorageGatewayUpdateBandwidthRateLimitRequest,
    ) -> StorageGatewayUpdateBandwidthRateLimitResponse:
        client = self._require_client()
        return await self._execute(client.update_bandwidth_rate_limit, request, StorageGatewayUpdateBandwidthRateLimitResponse)

    async def update_bandwidth_rate_limit_schedule(
        self,
        request: StorageGatewayUpdateBandwidthRateLimitScheduleRequest,
    ) -> StorageGatewayUpdateBandwidthRateLimitScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_bandwidth_rate_limit_schedule, request, StorageGatewayUpdateBandwidthRateLimitScheduleResponse)

    async def update_chap_credentials(
        self,
        request: StorageGatewayUpdateChapCredentialsRequest,
    ) -> StorageGatewayUpdateChapCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.update_chap_credentials, request, StorageGatewayUpdateChapCredentialsResponse)

    async def update_file_system_association(
        self,
        request: StorageGatewayUpdateFileSystemAssociationRequest,
    ) -> StorageGatewayUpdateFileSystemAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_file_system_association, request, StorageGatewayUpdateFileSystemAssociationResponse)

    async def update_gateway_information(
        self,
        request: StorageGatewayUpdateGatewayInformationRequest,
    ) -> StorageGatewayUpdateGatewayInformationResponse:
        client = self._require_client()
        return await self._execute(client.update_gateway_information, request, StorageGatewayUpdateGatewayInformationResponse)

    async def update_gateway_software_now(
        self,
        request: StorageGatewayUpdateGatewaySoftwareNowRequest,
    ) -> StorageGatewayUpdateGatewaySoftwareNowResponse:
        client = self._require_client()
        return await self._execute(client.update_gateway_software_now, request, StorageGatewayUpdateGatewaySoftwareNowResponse)

    async def update_maintenance_start_time(
        self,
        request: StorageGatewayUpdateMaintenanceStartTimeRequest,
    ) -> StorageGatewayUpdateMaintenanceStartTimeResponse:
        client = self._require_client()
        return await self._execute(client.update_maintenance_start_time, request, StorageGatewayUpdateMaintenanceStartTimeResponse)

    async def update_nfs_file_share(
        self,
        request: StorageGatewayUpdateNFSFileShareRequest,
    ) -> StorageGatewayUpdateNFSFileShareResponse:
        client = self._require_client()
        return await self._execute(client.update_nfs_file_share, request, StorageGatewayUpdateNFSFileShareResponse)

    async def update_smb_file_share(
        self,
        request: StorageGatewayUpdateSMBFileShareRequest,
    ) -> StorageGatewayUpdateSMBFileShareResponse:
        client = self._require_client()
        return await self._execute(client.update_smb_file_share, request, StorageGatewayUpdateSMBFileShareResponse)

    async def update_smb_file_share_visibility(
        self,
        request: StorageGatewayUpdateSMBFileShareVisibilityRequest,
    ) -> StorageGatewayUpdateSMBFileShareVisibilityResponse:
        client = self._require_client()
        return await self._execute(client.update_smb_file_share_visibility, request, StorageGatewayUpdateSMBFileShareVisibilityResponse)

    async def update_smb_local_groups(
        self,
        request: StorageGatewayUpdateSMBLocalGroupsRequest,
    ) -> StorageGatewayUpdateSMBLocalGroupsResponse:
        client = self._require_client()
        return await self._execute(client.update_smb_local_groups, request, StorageGatewayUpdateSMBLocalGroupsResponse)

    async def update_smb_security_strategy(
        self,
        request: StorageGatewayUpdateSMBSecurityStrategyRequest,
    ) -> StorageGatewayUpdateSMBSecurityStrategyResponse:
        client = self._require_client()
        return await self._execute(client.update_smb_security_strategy, request, StorageGatewayUpdateSMBSecurityStrategyResponse)

    async def update_snapshot_schedule(
        self,
        request: StorageGatewayUpdateSnapshotScheduleRequest,
    ) -> StorageGatewayUpdateSnapshotScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_snapshot_schedule, request, StorageGatewayUpdateSnapshotScheduleResponse)

    async def update_vtl_device_type(
        self,
        request: StorageGatewayUpdateVTLDeviceTypeRequest,
    ) -> StorageGatewayUpdateVTLDeviceTypeResponse:
        client = self._require_client()
        return await self._execute(client.update_vtl_device_type, request, StorageGatewayUpdateVTLDeviceTypeResponse)
