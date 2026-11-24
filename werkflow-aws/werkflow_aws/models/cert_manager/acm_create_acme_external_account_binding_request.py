from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_expiration import ACMExpiration
from .acm_tag import ACMTag


class ACMCreateAcmeExternalAccountBindingRequest(BaseModel):
    AcmeEndpointArn: StrictStr
    RoleArn: StrictStr
    IdempotencyToken: StrictStr | None = None
    Expiration: ACMExpiration | None = None
    Tags: list[ACMTag] | None = None
