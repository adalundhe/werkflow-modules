from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class RDSCertificate(BaseModel):
    CertificateIdentifier: StrictStr | None = None
    CertificateType: StrictStr | None = None
    Thumbprint: StrictStr | None = None
    ValidFrom: datetime.datetime | StrictStr | None = None
    ValidTill: datetime.datetime | StrictStr | None = None
    CertificateArn: StrictStr | None = None
    CustomerOverride: StrictBool | None = None
    CustomerOverrideValidTill: datetime.datetime | StrictStr | None = None
