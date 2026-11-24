from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_server_certificate_metadata import IAMServerCertificateMetadata


class IAMListServerCertificatesResponse(BaseModel):
    ServerCertificateMetadataList: list[IAMServerCertificateMetadata] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
