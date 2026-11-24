from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .guard_duty_detector_additional_configuration import GuardDutyDetectorAdditionalConfiguration


class GuardDutyDetectorFeatureConfiguration(BaseModel):
    Name: Literal['S3_DATA_EVENTS', 'EKS_AUDIT_LOGS', 'EBS_MALWARE_PROTECTION', 'RDS_LOGIN_EVENTS', 'LAMBDA_NETWORK_LOGS', 'EKS_RUNTIME_MONITORING', 'RUNTIME_MONITORING', 'AI_PROTECTION', 'AI_ANALYST'] | None = None
    Status: Literal['ENABLED', 'DISABLED'] | None = None
    AdditionalConfiguration: list[GuardDutyDetectorAdditionalConfiguration] | None = None
