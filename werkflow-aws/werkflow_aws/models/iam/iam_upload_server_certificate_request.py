from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_tag_model import IAMTagModel


class IAMUploadServerCertificateRequest(BaseModel):
    ServerCertificateName: StrictStr
    CertificateBody: StrictStr
    PrivateKey: StrictStr
    Path: StrictStr | None = None
    CertificateChain: StrictStr | None = None
    Tags: list[IAMTagModel] | None = None
