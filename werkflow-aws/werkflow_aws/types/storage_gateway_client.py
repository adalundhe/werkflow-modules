from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class StorageGatewayClient(ABC):

    @abstractmethod
    def activate_gateway(
        self,
        *,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: str | None = None,
        TapeDriveType: str | None = None,
        MediumChangerType: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_cache(
        self,
        *,
        GatewayARN: str,
        DiskIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags_to_resource(
        self,
        *,
        ResourceARN: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_upload_buffer(
        self,
        *,
        GatewayARN: str,
        DiskIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_working_storage(
        self,
        *,
        GatewayARN: str,
        DiskIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def assign_tape_pool(
        self,
        *,
        TapeARN: str,
        PoolId: str,
        BypassGovernanceRetention: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_file_system(
        self,
        *,
        UserName: str,
        Password: str,
        ClientToken: str,
        GatewayARN: str,
        LocationARN: str,
        Tags: list[dict[str, Any]] | None = None,
        AuditDestinationARN: str | None = None,
        CacheAttributes: dict[str, Any] | None = None,
        EndpointNetworkConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_volume(
        self,
        *,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: str | None = None,
        DiskId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_archival(
        self,
        *,
        GatewayARN: str,
        TapeARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_cache_report(
        self,
        *,
        CacheReportARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_retrieval(
        self,
        *,
        GatewayARN: str,
        TapeARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cached_iscsi_volume(
        self,
        *,
        GatewayARN: str,
        VolumeSizeInBytes: int,
        TargetName: str,
        NetworkInterfaceId: str,
        ClientToken: str,
        SnapshotId: str | None = None,
        SourceVolumeARN: str | None = None,
        KMSEncrypted: bool | None = None,
        KMSKey: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_nfs_file_share(
        self,
        *,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        NFSFileShareDefaults: dict[str, Any] | None = None,
        EncryptionType: str | None = None,
        KMSEncrypted: bool | None = None,
        KMSKey: str | None = None,
        DefaultStorageClass: str | None = None,
        ObjectACL: str | None = None,
        ClientList: list[str] | None = None,
        Squash: str | None = None,
        ReadOnly: bool | None = None,
        GuessMIMETypeEnabled: bool | None = None,
        RequesterPays: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        FileShareName: str | None = None,
        CacheAttributes: dict[str, Any] | None = None,
        NotificationPolicy: str | None = None,
        VPCEndpointDNSName: str | None = None,
        BucketRegion: str | None = None,
        AuditDestinationARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_smb_file_share(
        self,
        *,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        EncryptionType: str | None = None,
        KMSEncrypted: bool | None = None,
        KMSKey: str | None = None,
        DefaultStorageClass: str | None = None,
        ObjectACL: str | None = None,
        ReadOnly: bool | None = None,
        GuessMIMETypeEnabled: bool | None = None,
        RequesterPays: bool | None = None,
        SMBACLEnabled: bool | None = None,
        AccessBasedEnumeration: bool | None = None,
        AdminUserList: list[str] | None = None,
        ValidUserList: list[str] | None = None,
        InvalidUserList: list[str] | None = None,
        AuditDestinationARN: str | None = None,
        Authentication: str | None = None,
        CaseSensitivity: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        FileShareName: str | None = None,
        CacheAttributes: dict[str, Any] | None = None,
        NotificationPolicy: str | None = None,
        VPCEndpointDNSName: str | None = None,
        BucketRegion: str | None = None,
        OplocksEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot(
        self,
        *,
        VolumeARN: str,
        SnapshotDescription: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot_from_volume_recovery_point(
        self,
        *,
        VolumeARN: str,
        SnapshotDescription: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stored_iscsi_volume(
        self,
        *,
        GatewayARN: str,
        DiskId: str,
        PreserveExistingData: bool,
        TargetName: str,
        NetworkInterfaceId: str,
        SnapshotId: str | None = None,
        KMSEncrypted: bool | None = None,
        KMSKey: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tape_pool(
        self,
        *,
        PoolName: str,
        StorageClass: str,
        RetentionLockType: str | None = None,
        RetentionLockTimeInDays: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tape_with_barcode(
        self,
        *,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: bool | None = None,
        KMSKey: str | None = None,
        PoolId: str | None = None,
        Worm: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tapes(
        self,
        *,
        GatewayARN: str,
        TapeSizeInBytes: int,
        ClientToken: str,
        NumTapesToCreate: int,
        TapeBarcodePrefix: str,
        KMSEncrypted: bool | None = None,
        KMSKey: str | None = None,
        PoolId: str | None = None,
        Worm: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_automatic_tape_creation_policy(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bandwidth_rate_limit(
        self,
        *,
        GatewayARN: str,
        BandwidthType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cache_report(
        self,
        *,
        CacheReportARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_chap_credentials(
        self,
        *,
        TargetARN: str,
        InitiatorName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_file_share(
        self,
        *,
        FileShareARN: str,
        ForceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_gateway(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot_schedule(
        self,
        *,
        VolumeARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tape(
        self,
        *,
        GatewayARN: str,
        TapeARN: str,
        BypassGovernanceRetention: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tape_archive(
        self,
        *,
        TapeARN: str,
        BypassGovernanceRetention: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tape_pool(
        self,
        *,
        PoolARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_volume(
        self,
        *,
        VolumeARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_availability_monitor_test(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bandwidth_rate_limit(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bandwidth_rate_limit_schedule(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cache(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cache_report(
        self,
        *,
        CacheReportARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cached_iscsi_volumes(
        self,
        *,
        VolumeARNs: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_chap_credentials(
        self,
        *,
        TargetARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_file_system_associations(
        self,
        *,
        FileSystemAssociationARNList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_gateway_information(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_start_time(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_nfs_file_shares(
        self,
        *,
        FileShareARNList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_smb_file_shares(
        self,
        *,
        FileShareARNList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_smb_settings(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshot_schedule(
        self,
        *,
        VolumeARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stored_iscsi_volumes(
        self,
        *,
        VolumeARNs: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tape_archives(
        self,
        *,
        TapeARNs: list[str] | None = None,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tape_recovery_points(
        self,
        *,
        GatewayARN: str,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tapes(
        self,
        *,
        GatewayARN: str,
        TapeARNs: list[str] | None = None,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_upload_buffer(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vtl_devices(
        self,
        *,
        GatewayARN: str,
        VTLDeviceARNs: list[str] | None = None,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_working_storage(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_volume(
        self,
        *,
        VolumeARN: str,
        ForceDetach: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_gateway(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_file_system(
        self,
        *,
        FileSystemAssociationARN: str,
        ForceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def evict_files_failing_upload(
        self,
        *,
        FileShareARN: str,
        ForceRemove: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def join_domain(
        self,
        *,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: str | None = None,
        DomainControllers: list[str] | None = None,
        TimeoutInSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_automatic_tape_creation_policies(
        self,
        *,
        GatewayARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cache_reports(
        self,
        *,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_file_shares(
        self,
        *,
        GatewayARN: str | None = None,
        Limit: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_file_system_associations(
        self,
        *,
        GatewayARN: str | None = None,
        Limit: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_gateways(
        self,
        *,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_local_disks(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tape_pools(
        self,
        *,
        PoolARNs: list[str] | None = None,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tapes(
        self,
        *,
        TapeARNs: list[str] | None = None,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_volume_initiators(
        self,
        *,
        VolumeARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_volume_recovery_points(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_volumes(
        self,
        *,
        GatewayARN: str | None = None,
        Marker: str | None = None,
        Limit: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def notify_when_uploaded(
        self,
        *,
        FileShareARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def refresh_cache(
        self,
        *,
        FileShareARN: str,
        FolderList: list[str] | None = None,
        Recursive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags_from_resource(
        self,
        *,
        ResourceARN: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_cache(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retrieve_tape_archive(
        self,
        *,
        TapeARN: str,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retrieve_tape_recovery_point(
        self,
        *,
        TapeARN: str,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_local_console_password(
        self,
        *,
        GatewayARN: str,
        LocalConsolePassword: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_smb_guest_password(
        self,
        *,
        GatewayARN: str,
        Password: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def shutdown_gateway(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_availability_monitor_test(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_cache_report(
        self,
        *,
        FileShareARN: str,
        Role: str,
        LocationARN: str,
        BucketRegion: str,
        ClientToken: str,
        VPCEndpointDNSName: str | None = None,
        InclusionFilters: list[dict[str, Any]] | None = None,
        ExclusionFilters: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_gateway(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_automatic_tape_creation_policy(
        self,
        *,
        AutomaticTapeCreationRules: list[dict[str, Any]],
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bandwidth_rate_limit(
        self,
        *,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: int | None = None,
        AverageDownloadRateLimitInBitsPerSec: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bandwidth_rate_limit_schedule(
        self,
        *,
        GatewayARN: str,
        BandwidthRateLimitIntervals: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_chap_credentials(
        self,
        *,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_file_system_association(
        self,
        *,
        FileSystemAssociationARN: str,
        UserName: str | None = None,
        Password: str | None = None,
        AuditDestinationARN: str | None = None,
        CacheAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_gateway_information(
        self,
        *,
        GatewayARN: str,
        GatewayName: str | None = None,
        GatewayTimezone: str | None = None,
        CloudWatchLogGroupARN: str | None = None,
        GatewayCapacity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_gateway_software_now(
        self,
        *,
        GatewayARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_maintenance_start_time(
        self,
        *,
        GatewayARN: str,
        HourOfDay: int | None = None,
        MinuteOfHour: int | None = None,
        DayOfWeek: int | None = None,
        DayOfMonth: int | None = None,
        SoftwareUpdatePreferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_nfs_file_share(
        self,
        *,
        FileShareARN: str,
        EncryptionType: str | None = None,
        KMSEncrypted: bool | None = None,
        KMSKey: str | None = None,
        NFSFileShareDefaults: dict[str, Any] | None = None,
        DefaultStorageClass: str | None = None,
        ObjectACL: str | None = None,
        ClientList: list[str] | None = None,
        Squash: str | None = None,
        ReadOnly: bool | None = None,
        GuessMIMETypeEnabled: bool | None = None,
        RequesterPays: bool | None = None,
        FileShareName: str | None = None,
        CacheAttributes: dict[str, Any] | None = None,
        NotificationPolicy: str | None = None,
        AuditDestinationARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_smb_file_share(
        self,
        *,
        FileShareARN: str,
        EncryptionType: str | None = None,
        KMSEncrypted: bool | None = None,
        KMSKey: str | None = None,
        DefaultStorageClass: str | None = None,
        ObjectACL: str | None = None,
        ReadOnly: bool | None = None,
        GuessMIMETypeEnabled: bool | None = None,
        RequesterPays: bool | None = None,
        SMBACLEnabled: bool | None = None,
        AccessBasedEnumeration: bool | None = None,
        AdminUserList: list[str] | None = None,
        ValidUserList: list[str] | None = None,
        InvalidUserList: list[str] | None = None,
        AuditDestinationARN: str | None = None,
        CaseSensitivity: str | None = None,
        FileShareName: str | None = None,
        CacheAttributes: dict[str, Any] | None = None,
        NotificationPolicy: str | None = None,
        OplocksEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_smb_file_share_visibility(
        self,
        *,
        GatewayARN: str,
        FileSharesVisible: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_smb_local_groups(
        self,
        *,
        GatewayARN: str,
        SMBLocalGroups: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_smb_security_strategy(
        self,
        *,
        GatewayARN: str,
        SMBSecurityStrategy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_snapshot_schedule(
        self,
        *,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vtl_device_type(
        self,
        *,
        VTLDeviceARN: str,
        DeviceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
