from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .emr_application import EMRApplication
from .emr_cluster_status import EMRClusterStatus
from .emr_configuration import EMRConfiguration
from .emr_ec2_instance_attributes import EMREc2InstanceAttributes
from .emr_kerberos_attributes import EMRKerberosAttributes
from .emr_monitoring_configuration import EMRMonitoringConfiguration
from .emr_placement_group_config import EMRPlacementGroupConfig
from .emr_tag import EMRTag


class EMRCluster(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: EMRClusterStatus | None = None
    Ec2InstanceAttributes: EMREc2InstanceAttributes | None = None
    InstanceCollectionType: StrictStr | None = None
    LogUri: StrictStr | None = None
    LogEncryptionKmsKeyId: StrictStr | None = None
    RequestedAmiVersion: StrictStr | None = None
    RunningAmiVersion: StrictStr | None = None
    ReleaseLabel: StrictStr | None = None
    AutoTerminate: StrictBool | None = None
    TerminationProtected: StrictBool | None = None
    UnhealthyNodeReplacement: StrictBool | None = None
    VisibleToAllUsers: StrictBool | None = None
    Applications: list[EMRApplication] | None = None
    Tags: list[EMRTag] | None = None
    ServiceRole: StrictStr | None = None
    NormalizedInstanceHours: StrictInt | None = None
    MasterPublicDnsName: StrictStr | None = None
    Configurations: list[EMRConfiguration] | None = None
    SecurityConfiguration: StrictStr | None = None
    AutoScalingRole: StrictStr | None = None
    ScaleDownBehavior: StrictStr | None = None
    CustomAmiId: StrictStr | None = None
    EbsRootVolumeSize: StrictInt | None = None
    RepoUpgradeOnBoot: StrictStr | None = None
    KerberosAttributes: EMRKerberosAttributes | None = None
    ClusterArn: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    StepConcurrencyLevel: StrictInt | None = None
    PlacementGroups: list[EMRPlacementGroupConfig] | None = None
    OSReleaseLabel: StrictStr | None = None
    EbsRootVolumeIops: StrictInt | None = None
    EbsRootVolumeThroughput: StrictInt | None = None
    ExtendedSupport: StrictBool | None = None
    MonitoringConfiguration: EMRMonitoringConfiguration | None = None
    SessionEnabled: StrictBool | None = None
