from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class ACMExportCertificateRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    CertificateArn: StrictStr
    Passphrase: StrictBytes | BinaryIO | StrictStr
