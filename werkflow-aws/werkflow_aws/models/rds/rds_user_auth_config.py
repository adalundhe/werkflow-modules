from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RDSUserAuthConfig(BaseModel):
    Description: StrictStr | None = None
    UserName: StrictStr | None = None
    AuthScheme: Literal['SECRETS'] | None = None
    SecretArn: StrictStr | None = None
    IAMAuth: Literal['DISABLED', 'REQUIRED', 'ENABLED'] | None = None
    ClientPasswordAuthType: Literal['MYSQL_NATIVE_PASSWORD', 'MYSQL_CACHING_SHA2_PASSWORD', 'POSTGRES_SCRAM_SHA_256', 'POSTGRES_MD5', 'SQL_SERVER_AUTHENTICATION'] | None = None
