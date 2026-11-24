from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ACMCreateAcmeDomainValidationResponse(BaseModel):
    AcmeDomainValidationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
