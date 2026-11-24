from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSMicrosoftSqlServerDataProviderSettings(BaseModel):
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    SslMode: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    S3Path: StrictStr | None = None
    S3AccessRoleArn: StrictStr | None = None
