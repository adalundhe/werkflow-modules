from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .polly_validation_exception_field import PollyValidationExceptionField


class PollyValidationException(BaseModel):
    message: StrictStr | None = None
    reason: StrictStr | None = None
    fields: list[PollyValidationExceptionField] | None = None
