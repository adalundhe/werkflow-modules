from __future__ import annotations
from pydantic import BaseModel
from .ses_suppression_condition_threshold import SESSuppressionConditionThreshold


class SESSuppressionValidationOptions(BaseModel):
    ConditionThreshold: SESSuppressionConditionThreshold | None = None
