from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSSybaseAseDataProviderSettings(BaseModel):
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    SslMode: StrictStr | None = None
    EncryptPassword: StrictBool | None = None
    CertificateArn: StrictStr | None = None
