from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_suppression_validation_options import SESSuppressionValidationOptions


class SESSuppressionOptions(BaseModel):
    SuppressedReasons: list[StrictStr] | None = None
    SuppressionScope: StrictStr | None = None
    ValidationOptions: SESSuppressionValidationOptions | None = None
