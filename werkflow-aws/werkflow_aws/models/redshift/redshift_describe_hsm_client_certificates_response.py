from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_hsm_client_certificate import RedshiftHsmClientCertificate


class RedshiftDescribeHsmClientCertificatesResponse(BaseModel):
    Marker: StrictStr | None = None
    HsmClientCertificates: list[RedshiftHsmClientCertificate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
