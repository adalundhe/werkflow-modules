from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_suppression_confidence_threshold import SESSuppressionConfidenceThreshold


class SESSuppressionConditionThreshold(BaseModel):
    ConditionThresholdEnabled: StrictStr | None = None
    OverallConfidenceThreshold: SESSuppressionConfidenceThreshold | None = None
