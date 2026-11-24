from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSUserAuthConfigInfo(BaseModel):
    Description: StrictStr | None = None
    UserName: StrictStr | None = None
    AuthScheme: StrictStr | None = None
    SecretArn: StrictStr | None = None
    IAMAuth: StrictStr | None = None
    ClientPasswordAuthType: StrictStr | None = None
