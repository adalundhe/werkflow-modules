from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class FSxClient(ABC):

    @abstractmethod
    def associate_file_system_aliases(
        self,
        *,
        FileSystemId: str,
        Aliases: list[str],
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_data_repository_task(
        self,
        *,
        TaskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_backup(
        self,
        *,
        SourceBackupId: str,
        ClientRequestToken: str | None = None,
        SourceRegion: str | None = None,
        KmsKeyId: str | None = None,
        CopyTags: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_snapshot_and_update_volume(
        self,
        *,
        VolumeId: str,
        SourceSnapshotARN: str,
        ClientRequestToken: str | None = None,
        CopyStrategy: str | None = None,
        Options: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_and_attach_s3_access_point(
        self,
        *,
        Name: str,
        Type: str,
        ClientRequestToken: str | None = None,
        OpenZFSConfiguration: dict[str, Any] | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
        S3AccessPoint: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_backup(
        self,
        *,
        FileSystemId: str | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        VolumeId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster_peer(
        self,
        *,
        FileSystemId: str,
        PeerAddresses: list[str],
        PassphraseSecretArn: str,
        AllowedSvmMode: str,
        ClientRequestToken: str | None = None,
        PeerClusterName: str | None = None,
        AllowedSvmIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_repository_association(
        self,
        *,
        FileSystemId: str,
        DataRepositoryPath: str,
        FileSystemPath: str | None = None,
        BatchImportMetaDataOnCreate: bool | None = None,
        ImportedFileChunkSize: int | None = None,
        S3: dict[str, Any] | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_repository_task(
        self,
        *,
        Type: str,
        FileSystemId: str,
        Report: dict[str, Any],
        Paths: list[str] | None = None,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CapacityToRelease: int | None = None,
        ReleaseConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_file_cache(
        self,
        *,
        FileCacheType: str,
        FileCacheTypeVersion: str,
        StorageCapacity: int,
        SubnetIds: list[str],
        ClientRequestToken: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CopyTagsToDataRepositoryAssociations: bool | None = None,
        KmsKeyId: str | None = None,
        LustreConfiguration: dict[str, Any] | None = None,
        DataRepositoryAssociations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_file_system(
        self,
        *,
        FileSystemType: str,
        SubnetIds: list[str],
        ClientRequestToken: str | None = None,
        StorageCapacity: int | None = None,
        StorageType: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
        WindowsConfiguration: dict[str, Any] | None = None,
        LustreConfiguration: dict[str, Any] | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
        FileSystemTypeVersion: str | None = None,
        OpenZFSConfiguration: dict[str, Any] | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_file_system_from_backup(
        self,
        *,
        BackupId: str,
        SubnetIds: list[str],
        ClientRequestToken: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        WindowsConfiguration: dict[str, Any] | None = None,
        LustreConfiguration: dict[str, Any] | None = None,
        StorageType: str | None = None,
        KmsKeyId: str | None = None,
        FileSystemTypeVersion: str | None = None,
        OpenZFSConfiguration: dict[str, Any] | None = None,
        StorageCapacity: int | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapmirror_policy(
        self,
        *,
        Name: str,
        ClientRequestToken: str | None = None,
        FileSystemId: str | None = None,
        StorageVirtualMachineId: str | None = None,
        SnapshotCopyMode: str | None = None,
        RetentionRules: list[dict[str, Any]] | None = None,
        TransferSchedule: str | None = None,
        NetworkCompressionEnabled: bool | None = None,
        ThrottleInKbps: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapmirror_relationship(
        self,
        *,
        Source: dict[str, Any],
        Destination: dict[str, Any],
        ClientRequestToken: str | None = None,
        PolicyId: str | None = None,
        TransferSchedule: str | None = None,
        ThrottleInKbps: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot(
        self,
        *,
        Name: str,
        VolumeId: str,
        ClientRequestToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot_policy(
        self,
        *,
        Name: str,
        Schedules: list[dict[str, Any]],
        ClientRequestToken: str | None = None,
        FileSystemId: str | None = None,
        StorageVirtualMachineId: str | None = None,
        Enabled: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_storage_virtual_machine(
        self,
        *,
        FileSystemId: str,
        Name: str,
        ActiveDirectoryConfiguration: dict[str, Any] | None = None,
        ClientRequestToken: str | None = None,
        SvmAdminPassword: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        RootVolumeSecurityStyle: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_storage_virtual_machine_peer(
        self,
        *,
        StorageVirtualMachineId: str,
        PeerSvmName: str,
        Applications: list[str],
        ClientRequestToken: str | None = None,
        PeerClusterName: str | None = None,
        PeerSvmAlias: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_volume(
        self,
        *,
        VolumeType: str,
        Name: str,
        ClientRequestToken: str | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        OpenZFSConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_volume_from_backup(
        self,
        *,
        BackupId: str,
        Name: str,
        ClientRequestToken: str | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_backup(
        self,
        *,
        BackupId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster_peer(
        self,
        *,
        ClusterPeerId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_repository_association(
        self,
        *,
        AssociationId: str,
        ClientRequestToken: str | None = None,
        DeleteDataInFileSystem: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_file_cache(
        self,
        *,
        FileCacheId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_file_system(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str | None = None,
        WindowsConfiguration: dict[str, Any] | None = None,
        LustreConfiguration: dict[str, Any] | None = None,
        OpenZFSConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapmirror_policy(
        self,
        *,
        SnapmirrorPolicyId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapmirror_relationship(
        self,
        *,
        SnapmirrorRelationshipId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot(
        self,
        *,
        SnapshotId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot_policy(
        self,
        *,
        SnapshotPolicyId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_storage_virtual_machine(
        self,
        *,
        StorageVirtualMachineId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_storage_virtual_machine_peer(
        self,
        *,
        StorageVirtualMachinePeerId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_volume(
        self,
        *,
        VolumeId: str,
        ClientRequestToken: str | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
        OpenZFSConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_backups(
        self,
        *,
        BackupIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_peers(
        self,
        *,
        ClusterPeerIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_repository_associations(
        self,
        *,
        AssociationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_repository_tasks(
        self,
        *,
        TaskIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_file_caches(
        self,
        *,
        FileCacheIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_file_system_aliases(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_file_systems(
        self,
        *,
        FileSystemIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_s3_access_point_attachments(
        self,
        *,
        Names: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_shared_vpc_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapmirror_policies(
        self,
        *,
        SnapmirrorPolicyIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapmirror_relationships(
        self,
        *,
        SnapmirrorRelationshipIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshot_policies(
        self,
        *,
        SnapshotPolicyIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshots(
        self,
        *,
        SnapshotIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IncludeShared: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_storage_virtual_machine_peers(
        self,
        *,
        StorageVirtualMachinePeerIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_storage_virtual_machines(
        self,
        *,
        StorageVirtualMachineIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_volumes(
        self,
        *,
        VolumeIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_and_delete_s3_access_point(
        self,
        *,
        Name: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_file_system_aliases(
        self,
        *,
        FileSystemId: str,
        Aliases: list[str],
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceARN: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def release_file_system_nfs_v3_locks(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_volume_from_snapshot(
        self,
        *,
        VolumeId: str,
        SnapshotId: str,
        ClientRequestToken: str | None = None,
        Options: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_misconfigured_state_recovery(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceARN: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceARN: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_peer(
        self,
        *,
        ClusterPeerId: str,
        ClientRequestToken: str | None = None,
        PeerClusterName: str | None = None,
        PeerAddresses: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_repository_association(
        self,
        *,
        AssociationId: str,
        ClientRequestToken: str | None = None,
        ImportedFileChunkSize: int | None = None,
        S3: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_file_cache(
        self,
        *,
        FileCacheId: str,
        ClientRequestToken: str | None = None,
        LustreConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_file_system(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str | None = None,
        StorageCapacity: int | None = None,
        WindowsConfiguration: dict[str, Any] | None = None,
        LustreConfiguration: dict[str, Any] | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
        OpenZFSConfiguration: dict[str, Any] | None = None,
        StorageType: str | None = None,
        FileSystemTypeVersion: str | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_shared_vpc_configuration(
        self,
        *,
        EnableFsxRouteTableUpdatesFromParticipantAccounts: str | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_snapmirror_policy(
        self,
        *,
        SnapmirrorPolicyId: str,
        ClientRequestToken: str | None = None,
        RetentionRules: list[dict[str, Any]] | None = None,
        TransferSchedule: str | None = None,
        NetworkCompressionEnabled: bool | None = None,
        ThrottleInKbps: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_snapmirror_relationship(
        self,
        *,
        SnapmirrorRelationshipId: str,
        ClientRequestToken: str | None = None,
        PolicyId: str | None = None,
        TransferSchedule: str | None = None,
        ThrottleInKbps: int | None = None,
        State: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_snapshot(
        self,
        *,
        SnapshotId: str,
        ClientRequestToken: str | None = None,
        Name: str | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_snapshot_policy(
        self,
        *,
        SnapshotPolicyId: str,
        ClientRequestToken: str | None = None,
        Enabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_storage_virtual_machine(
        self,
        *,
        StorageVirtualMachineId: str,
        ActiveDirectoryConfiguration: dict[str, Any] | None = None,
        ClientRequestToken: str | None = None,
        SvmAdminPassword: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_storage_virtual_machine_peer(
        self,
        *,
        StorageVirtualMachinePeerId: str,
        ClientRequestToken: str | None = None,
        Applications: list[str] | None = None,
        PeerSvmAlias: str | None = None,
        State: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_volume(
        self,
        *,
        VolumeId: str,
        ClientRequestToken: str | None = None,
        OntapConfiguration: dict[str, Any] | None = None,
        Name: str | None = None,
        OpenZFSConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
