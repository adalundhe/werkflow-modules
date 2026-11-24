from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_detection_rule_ec2_requirements import GuardDutyDetectionRuleEc2Requirements
from .guard_duty_detection_rule_ecs_fargate_requirements import GuardDutyDetectionRuleEcsFargateRequirements
from .guard_duty_detection_rule_eks_requirements import GuardDutyDetectionRuleEksRequirements


class GuardDutyDetectionRuleRuntimePlatforms(BaseModel):
    Eks: GuardDutyDetectionRuleEksRequirements | None = None
    Ec2: GuardDutyDetectionRuleEc2Requirements | None = None
    EcsFargate: GuardDutyDetectionRuleEcsFargateRequirements | None = None
