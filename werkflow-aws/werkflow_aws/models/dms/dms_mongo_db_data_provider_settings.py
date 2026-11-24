from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSMongoDbDataProviderSettings(BaseModel):
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    SslMode: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    AuthType: StrictStr | None = None
    AuthSource: StrictStr | None = None
    AuthMechanism: StrictStr | None = None
