from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_access_key_details import GuardDutyAccessKeyDetails
from .guard_duty_bedrock_guardrail_details import GuardDutyBedrockGuardrailDetails
from .guard_duty_container import GuardDutyContainer
from .guard_duty_ebs_snapshot_details import GuardDutyEbsSnapshotDetails
from .guard_duty_ebs_volume_details import GuardDutyEbsVolumeDetails
from .guard_duty_ec2_image_details import GuardDutyEc2ImageDetails
from .guard_duty_ecs_cluster_details import GuardDutyEcsClusterDetails
from .guard_duty_eks_cluster_details import GuardDutyEksClusterDetails
from .guard_duty_instance_details import GuardDutyInstanceDetails
from .guard_duty_kubernetes_details import GuardDutyKubernetesDetails
from .guard_duty_lambda_details import GuardDutyLambdaDetails
from .guard_duty_model_detail import GuardDutyModelDetail
from .guard_duty_rds_db_instance_details import GuardDutyRdsDbInstanceDetails
from .guard_duty_rds_db_user_details import GuardDutyRdsDbUserDetails
from .guard_duty_rds_limitless_db_details import GuardDutyRdsLimitlessDbDetails
from .guard_duty_recovery_point_details import GuardDutyRecoveryPointDetails
from .guard_duty_s3_bucket_detail import GuardDutyS3BucketDetail


class GuardDutyResource(BaseModel):
    AccessKeyDetails: GuardDutyAccessKeyDetails | None = None
    S3BucketDetails: list[GuardDutyS3BucketDetail] | None = None
    InstanceDetails: GuardDutyInstanceDetails | None = None
    EksClusterDetails: GuardDutyEksClusterDetails | None = None
    KubernetesDetails: GuardDutyKubernetesDetails | None = None
    ResourceType: StrictStr | None = None
    EbsVolumeDetails: GuardDutyEbsVolumeDetails | None = None
    EcsClusterDetails: GuardDutyEcsClusterDetails | None = None
    ContainerDetails: GuardDutyContainer | None = None
    LambdaDetails: GuardDutyLambdaDetails | None = None
    RdsDbInstanceDetails: GuardDutyRdsDbInstanceDetails | None = None
    RdsLimitlessDbDetails: GuardDutyRdsLimitlessDbDetails | None = None
    RdsDbUserDetails: GuardDutyRdsDbUserDetails | None = None
    EbsSnapshotDetails: GuardDutyEbsSnapshotDetails | None = None
    Ec2ImageDetails: GuardDutyEc2ImageDetails | None = None
    RecoveryPointDetails: GuardDutyRecoveryPointDetails | None = None
    BedrockGuardrailDetails: GuardDutyBedrockGuardrailDetails | None = None
    ModelDetails: list[GuardDutyModelDetail] | None = None
