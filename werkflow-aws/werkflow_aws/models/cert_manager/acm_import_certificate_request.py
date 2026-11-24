from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .acm_tag import ACMTag


class ACMImportCertificateRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Certificate: StrictBytes | BinaryIO | StrictStr
    PrivateKey: StrictBytes | BinaryIO | StrictStr
    CertificateArn: StrictStr | None = None
    CertificateChain: StrictBytes | BinaryIO | StrictStr | None = None
    Tags: list[ACMTag] | None = None
