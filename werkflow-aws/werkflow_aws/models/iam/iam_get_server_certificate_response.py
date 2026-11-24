from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_server_certificate import IAMServerCertificate


class IAMGetServerCertificateResponse(BaseModel):
    ServerCertificate: IAMServerCertificate | None = None
    ResponseMetadata: dict[str, Any] | None = None
