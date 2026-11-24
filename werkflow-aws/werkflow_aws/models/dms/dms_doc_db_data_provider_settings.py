from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDocDbDataProviderSettings(BaseModel):
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    SslMode: StrictStr | None = None
    CertificateArn: StrictStr | None = None
