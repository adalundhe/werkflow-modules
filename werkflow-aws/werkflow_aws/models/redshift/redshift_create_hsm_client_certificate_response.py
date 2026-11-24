from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_hsm_client_certificate import RedshiftHsmClientCertificate


class RedshiftCreateHsmClientCertificateResponse(BaseModel):
    HsmClientCertificate: RedshiftHsmClientCertificate | None = None
    ResponseMetadata: dict[str, Any] | None = None
