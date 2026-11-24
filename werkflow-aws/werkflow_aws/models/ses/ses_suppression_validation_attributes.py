from __future__ import annotations
from pydantic import BaseModel
from .ses_suppression_condition_threshold import SESSuppressionConditionThreshold


class SESSuppressionValidationAttributes(BaseModel):
    ConditionThreshold: SESSuppressionConditionThreshold | None = None
