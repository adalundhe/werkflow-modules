from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .emr_application import EMRApplication
from .emr_auto_termination_policy import EMRAutoTerminationPolicy
from .emr_bootstrap_action_config import EMRBootstrapActionConfig
from .emr_configuration import EMRConfiguration
from .emr_job_flow_instances_config import EMRJobFlowInstancesConfig
from .emr_kerberos_attributes import EMRKerberosAttributes
from .emr_managed_scaling_policy import EMRManagedScalingPolicy
from .emr_monitoring_configuration import EMRMonitoringConfiguration
from .emr_placement_group_config import EMRPlacementGroupConfig
from .emr_step_config import EMRStepConfig
from .emr_supported_product_config import EMRSupportedProductConfig
from .emr_tag import EMRTag


class EMRRunJobFlowRequest(BaseModel):
    Name: StrictStr
    Instances: EMRJobFlowInstancesConfig
    LogUri: StrictStr | None = None
    LogEncryptionKmsKeyId: StrictStr | None = None
    AdditionalInfo: StrictStr | None = None
    AmiVersion: StrictStr | None = None
    ReleaseLabel: StrictStr | None = None
    Steps: list[EMRStepConfig] | None = None
    StepExecutionRoleArn: StrictStr | None = None
    BootstrapActions: list[EMRBootstrapActionConfig] | None = None
    SupportedProducts: list[StrictStr] | None = None
    NewSupportedProducts: list[EMRSupportedProductConfig] | None = None
    Applications: list[EMRApplication] | None = None
    Configurations: list[EMRConfiguration] | None = None
    VisibleToAllUsers: StrictBool | None = None
    JobFlowRole: StrictStr | None = None
    ServiceRole: StrictStr | None = None
    Tags: list[EMRTag] | None = None
    SecurityConfiguration: StrictStr | None = None
    AutoScalingRole: StrictStr | None = None
    ScaleDownBehavior: Literal['TERMINATE_AT_INSTANCE_HOUR', 'TERMINATE_AT_TASK_COMPLETION'] | None = None
    CustomAmiId: StrictStr | None = None
    EbsRootVolumeSize: StrictInt | None = None
    RepoUpgradeOnBoot: Literal['SECURITY', 'NONE'] | None = None
    KerberosAttributes: EMRKerberosAttributes | None = None
    StepConcurrencyLevel: StrictInt | None = None
    ManagedScalingPolicy: EMRManagedScalingPolicy | None = None
    PlacementGroupConfigs: list[EMRPlacementGroupConfig] | None = None
    AutoTerminationPolicy: EMRAutoTerminationPolicy | None = None
    OSReleaseLabel: StrictStr | None = None
    EbsRootVolumeIops: StrictInt | None = None
    EbsRootVolumeThroughput: StrictInt | None = None
    ExtendedSupport: StrictBool | None = None
    MonitoringConfiguration: EMRMonitoringConfiguration | None = None
    SessionEnabled: StrictBool | None = None
