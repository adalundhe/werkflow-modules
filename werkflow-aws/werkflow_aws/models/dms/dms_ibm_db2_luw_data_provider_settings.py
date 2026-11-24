from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSIbmDb2LuwDataProviderSettings(BaseModel):
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    SslMode: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    EncryptionAlgorithm: StrictInt | None = None
    SecurityMechanism: StrictInt | None = None
    S3Path: StrictStr | None = None
    S3AccessRoleArn: StrictStr | None = None
