from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_access_key import GuardDutyAccessKey
from .guard_duty_autoscaling_auto_scaling_group import GuardDutyAutoscalingAutoScalingGroup
from .guard_duty_bedrock_guardrail_resource import GuardDutyBedrockGuardrailResource
from .guard_duty_cloudformation_stack import GuardDutyCloudformationStack
from .guard_duty_container_finding_resource import GuardDutyContainerFindingResource
from .guard_duty_ec2_image import GuardDutyEc2Image
from .guard_duty_ec2_instance import GuardDutyEc2Instance
from .guard_duty_ec2_launch_template import GuardDutyEc2LaunchTemplate
from .guard_duty_ec2_network_interface import GuardDutyEc2NetworkInterface
from .guard_duty_ec2_vpc import GuardDutyEc2Vpc
from .guard_duty_ecs_cluster import GuardDutyEcsCluster
from .guard_duty_ecs_task import GuardDutyEcsTask
from .guard_duty_eks_cluster import GuardDutyEksCluster
from .guard_duty_iam_instance_profile_v2 import GuardDutyIamInstanceProfileV2
from .guard_duty_kubernetes_workload import GuardDutyKubernetesWorkload
from .guard_duty_s3_bucket import GuardDutyS3Bucket
from .guard_duty_s3_object import GuardDutyS3Object


class GuardDutyResourceData(BaseModel):
    S3Bucket: GuardDutyS3Bucket | None = None
    Ec2Instance: GuardDutyEc2Instance | None = None
    AccessKey: GuardDutyAccessKey | None = None
    Ec2NetworkInterface: GuardDutyEc2NetworkInterface | None = None
    S3Object: GuardDutyS3Object | None = None
    EksCluster: GuardDutyEksCluster | None = None
    KubernetesWorkload: GuardDutyKubernetesWorkload | None = None
    Container: GuardDutyContainerFindingResource | None = None
    EcsCluster: GuardDutyEcsCluster | None = None
    EcsTask: GuardDutyEcsTask | None = None
    IamInstanceProfile: GuardDutyIamInstanceProfileV2 | None = None
    AutoscalingAutoScalingGroup: GuardDutyAutoscalingAutoScalingGroup | None = None
    Ec2LaunchTemplate: GuardDutyEc2LaunchTemplate | None = None
    Ec2Vpc: GuardDutyEc2Vpc | None = None
    Ec2Image: GuardDutyEc2Image | None = None
    CloudformationStack: GuardDutyCloudformationStack | None = None
    BedrockGuardrail: GuardDutyBedrockGuardrailResource | None = None
