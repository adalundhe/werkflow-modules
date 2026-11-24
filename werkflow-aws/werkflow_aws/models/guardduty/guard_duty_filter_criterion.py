from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .guard_duty_filter_condition import GuardDutyFilterCondition


class GuardDutyFilterCriterion(BaseModel):
    CriterionKey: Literal['EC2_INSTANCE_ARN', 'SCAN_ID', 'ACCOUNT_ID', 'GUARDDUTY_FINDING_ID', 'SCAN_START_TIME', 'SCAN_STATUS', 'SCAN_TYPE'] | None = None
    FilterCondition: GuardDutyFilterCondition | None = None
