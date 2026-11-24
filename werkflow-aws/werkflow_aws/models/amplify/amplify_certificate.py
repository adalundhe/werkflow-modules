from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyCertificate(BaseModel):
    type: StrictStr | None = None
    customCertificateArn: StrictStr | None = None
    certificateVerificationDNSRecord: StrictStr | None = None
