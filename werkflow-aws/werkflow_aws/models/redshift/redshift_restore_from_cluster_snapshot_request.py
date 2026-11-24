from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftRestoreFromClusterSnapshotRequest(BaseModel):
    ClusterIdentifier: StrictStr
    SnapshotIdentifier: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    SnapshotClusterIdentifier: StrictStr | None = None
    Port: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    AllowVersionUpgrade: StrictBool | None = None
    ClusterSubnetGroupName: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    OwnerAccount: StrictStr | None = None
    HsmClientCertificateIdentifier: StrictStr | None = None
    HsmConfigurationIdentifier: StrictStr | None = None
    ElasticIp: StrictStr | None = None
    ClusterParameterGroupName: StrictStr | None = None
    ClusterSecurityGroups: list[StrictStr] | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    AutomatedSnapshotRetentionPeriod: StrictInt | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    NodeType: StrictStr | None = None
    EnhancedVpcRouting: StrictBool | None = None
    AdditionalInfo: StrictStr | None = None
    IamRoles: list[StrictStr] | None = None
    MaintenanceTrackName: StrictStr | None = None
    SnapshotScheduleIdentifier: StrictStr | None = None
    NumberOfNodes: StrictInt | None = None
    AvailabilityZoneRelocation: StrictBool | None = None
    AquaConfigurationStatus: Literal['enabled', 'disabled', 'auto'] | None = None
    DefaultIamRoleArn: StrictStr | None = None
    ReservedNodeId: StrictStr | None = None
    TargetReservedNodeOfferingId: StrictStr | None = None
    Encrypted: StrictBool | None = None
    ManageMasterPassword: StrictBool | None = None
    MasterPasswordSecretKmsKeyId: StrictStr | None = None
    IpAddressType: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    CatalogName: StrictStr | None = None
    RedshiftIdcApplicationArn: StrictStr | None = None
