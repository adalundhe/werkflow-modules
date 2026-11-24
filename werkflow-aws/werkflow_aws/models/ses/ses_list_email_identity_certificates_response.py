from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_identity_certificate import SESIdentityCertificate


class SESListEmailIdentityCertificatesResponse(BaseModel):
    Certificates: list[SESIdentityCertificate] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
