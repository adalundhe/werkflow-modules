from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTServerCertificateSummary(BaseModel):
    serverCertificateArn: StrictStr | None = None
    serverCertificateStatus: StrictStr | None = None
    serverCertificateStatusDetail: StrictStr | None = None
