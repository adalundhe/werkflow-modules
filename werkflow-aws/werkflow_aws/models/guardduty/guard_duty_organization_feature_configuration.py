from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .guard_duty_organization_additional_configuration import GuardDutyOrganizationAdditionalConfiguration


class GuardDutyOrganizationFeatureConfiguration(BaseModel):
    Name: Literal['S3_DATA_EVENTS', 'EKS_AUDIT_LOGS', 'EBS_MALWARE_PROTECTION', 'RDS_LOGIN_EVENTS', 'LAMBDA_NETWORK_LOGS', 'EKS_RUNTIME_MONITORING', 'RUNTIME_MONITORING', 'AI_PROTECTION'] | None = None
    AutoEnable: Literal['NEW', 'NONE', 'ALL'] | None = None
    AdditionalConfiguration: list[GuardDutyOrganizationAdditionalConfiguration] | None = None
