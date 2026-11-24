from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessOAuth2ClientCredentialConfiguration(BaseModel):
    secretArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    authorizationUrl: StrictStr | None = None
    tokenUrl: StrictStr | None = None
