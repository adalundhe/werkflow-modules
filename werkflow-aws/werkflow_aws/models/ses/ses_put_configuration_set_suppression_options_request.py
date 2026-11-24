from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ses_suppression_validation_options import SESSuppressionValidationOptions


class SESPutConfigurationSetSuppressionOptionsRequest(BaseModel):
    ConfigurationSetName: StrictStr
    SuppressionScope: Literal['ACCOUNT', 'TENANT'] | None = None
    SuppressedReasons: list[Literal['BOUNCE', 'COMPLAINT']] | None = None
    ValidationOptions: SESSuppressionValidationOptions | None = None
