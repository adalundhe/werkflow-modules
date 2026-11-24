from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_server_certificate_metadata import IAMServerCertificateMetadata
from .iam_tag_model import IAMTagModel


class IAMServerCertificate(BaseModel):
    ServerCertificateMetadata: IAMServerCertificateMetadata | None = None
    CertificateBody: StrictStr | None = None
    CertificateChain: StrictStr | None = None
    Tags: list[IAMTagModel] | None = None
