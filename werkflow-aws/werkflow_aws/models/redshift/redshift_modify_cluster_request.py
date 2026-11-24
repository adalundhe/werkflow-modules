from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftModifyClusterRequest(BaseModel):
    ClusterIdentifier: StrictStr
    ClusterType: StrictStr | None = None
    NodeType: StrictStr | None = None
    NumberOfNodes: StrictInt | None = None
    ClusterSecurityGroups: list[StrictStr] | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    MasterUserPassword: StrictStr | None = None
    ClusterParameterGroupName: StrictStr | None = None
    AutomatedSnapshotRetentionPeriod: StrictInt | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    ClusterVersion: StrictStr | None = None
    AllowVersionUpgrade: StrictBool | None = None
    HsmClientCertificateIdentifier: StrictStr | None = None
    HsmConfigurationIdentifier: StrictStr | None = None
    NewClusterIdentifier: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    ElasticIp: StrictStr | None = None
    EnhancedVpcRouting: StrictBool | None = None
    MaintenanceTrackName: StrictStr | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    AvailabilityZoneRelocation: StrictBool | None = None
    AvailabilityZone: StrictStr | None = None
    Port: StrictInt | None = None
    ManageMasterPassword: StrictBool | None = None
    MasterPasswordSecretKmsKeyId: StrictStr | None = None
    IpAddressType: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    ExtraComputeForAutomaticOptimization: StrictBool | None = None
