from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_server_certificate_metadata import IAMServerCertificateMetadata
from .iam_tag_model import IAMTagModel


class IAMUploadServerCertificateResponse(BaseModel):
    ServerCertificateMetadata: IAMServerCertificateMetadata | None = None
    Tags: list[IAMTagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
