from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_prevalidation_options import ACMPrevalidationOptions


class ACMUpdateAcmeDomainValidationRequest(BaseModel):
    AcmeDomainValidationArn: StrictStr
    PrevalidationOptions: ACMPrevalidationOptions | None = None
