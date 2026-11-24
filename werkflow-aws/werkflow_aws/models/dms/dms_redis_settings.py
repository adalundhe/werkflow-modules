from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSRedisSettings(BaseModel):
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    SslSecurityProtocol: StrictStr | None = None
    AuthType: StrictStr | None = None
    AuthUserName: StrictStr | None = None
    AuthPassword: StrictStr | None = None
    SslCaCertificateArn: StrictStr | None = None
