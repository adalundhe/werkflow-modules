from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTUpdateRoleAliasRequest(BaseModel):
    roleAlias: StrictStr
    roleArn: StrictStr | None = None
    credentialDurationSeconds: StrictInt | None = None
