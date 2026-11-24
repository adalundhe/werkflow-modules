from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ses_suppression_validation_attributes import SESSuppressionValidationAttributes


class SESPutAccountSuppressionAttributesRequest(BaseModel):
    SuppressedReasons: list[Literal['BOUNCE', 'COMPLAINT']] | None = None
    ValidationAttributes: SESSuppressionValidationAttributes | None = None
