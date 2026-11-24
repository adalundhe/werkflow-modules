from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMCertificates(BaseModel):
    ClusterCsr: StrictStr | None = None
    HsmCertificate: StrictStr | None = None
    AwsHardwareCertificate: StrictStr | None = None
    ManufacturerHardwareCertificate: StrictStr | None = None
    ClusterCertificate: StrictStr | None = None
