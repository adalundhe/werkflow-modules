from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateClusterRequest(BaseModel):
    ClusterIdentifier: StrictStr
    NodeType: StrictStr
    MasterUsername: StrictStr
    DBName: StrictStr | None = None
    ClusterType: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    ClusterSecurityGroups: list[StrictStr] | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    ClusterSubnetGroupName: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    ClusterParameterGroupName: StrictStr | None = None
    AutomatedSnapshotRetentionPeriod: StrictInt | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    Port: StrictInt | None = None
    ClusterVersion: StrictStr | None = None
    AllowVersionUpgrade: StrictBool | None = None
    NumberOfNodes: StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
    Encrypted: StrictBool | None = None
    HsmClientCertificateIdentifier: StrictStr | None = None
    HsmConfigurationIdentifier: StrictStr | None = None
    ElasticIp: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
    KmsKeyId: StrictStr | None = None
    EnhancedVpcRouting: StrictBool | None = None
    AdditionalInfo: StrictStr | None = None
    IamRoles: list[StrictStr] | None = None
    MaintenanceTrackName: StrictStr | None = None
    SnapshotScheduleIdentifier: StrictStr | None = None
    AvailabilityZoneRelocation: StrictBool | None = None
    AquaConfigurationStatus: Literal['enabled', 'disabled', 'auto'] | None = None
    DefaultIamRoleArn: StrictStr | None = None
    LoadSampleData: StrictStr | None = None
    ManageMasterPassword: StrictBool | None = None
    MasterPasswordSecretKmsKeyId: StrictStr | None = None
    IpAddressType: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    RedshiftIdcApplicationArn: StrictStr | None = None
    CatalogName: StrictStr | None = None
    ExtraComputeForAutomaticOptimization: StrictBool | None = None
