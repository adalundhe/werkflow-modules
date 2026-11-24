from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .io_t_validation_error import IoTValidationError


class IoTValidateSecurityProfileBehaviorsResponse(BaseModel):
    valid: StrictBool | None = None
    validationErrors: list[IoTValidationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
