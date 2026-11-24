from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESDkimSigningAttributes(BaseModel):
    DomainSigningSelector: StrictStr | None = None
    DomainSigningPrivateKey: StrictStr | None = None
    NextSigningKeyLength: Literal['RSA_1024_BIT', 'RSA_2048_BIT'] | None = None
    DomainSigningAttributesOrigin: StrictStr | None = None
