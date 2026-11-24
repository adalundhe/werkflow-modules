from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .dms_tag import DMSTag


class DMSImportCertificateRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    CertificateIdentifier: StrictStr
    CertificatePem: StrictStr | None = None
    CertificateWallet: StrictBytes | BinaryIO | StrictStr | None = None
    Tags: list[DMSTag] | None = None
    KmsKeyId: StrictStr | None = None
