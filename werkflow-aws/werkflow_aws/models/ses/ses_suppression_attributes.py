from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_suppression_validation_attributes import SESSuppressionValidationAttributes


class SESSuppressionAttributes(BaseModel):
    SuppressedReasons: list[StrictStr] | None = None
    ValidationAttributes: SESSuppressionValidationAttributes | None = None
