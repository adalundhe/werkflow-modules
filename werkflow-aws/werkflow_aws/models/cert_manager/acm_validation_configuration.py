from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_validation_challenge import ACMValidationChallenge


class ACMValidationConfiguration(BaseModel):
    ValidationMethod: StrictStr | None = None
    ValidationChallenge: ACMValidationChallenge | None = None
    ValidationStatus: StrictStr | None = None
