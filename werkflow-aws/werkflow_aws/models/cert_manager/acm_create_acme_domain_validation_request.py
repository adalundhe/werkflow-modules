from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_prevalidation_options import ACMPrevalidationOptions
from .acm_tag import ACMTag


class ACMCreateAcmeDomainValidationRequest(BaseModel):
    AcmeEndpointArn: StrictStr
    DomainName: StrictStr
    PrevalidationOptions: ACMPrevalidationOptions
    IdempotencyToken: StrictStr | None = None
    Tags: list[ACMTag] | None = None
