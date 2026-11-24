from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SESPutEmailIdentityDkimSigningAttributesResponse(BaseModel):
    DkimStatus: StrictStr | None = None
    DkimTokens: list[StrictStr] | None = None
    SigningHostedZone: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
