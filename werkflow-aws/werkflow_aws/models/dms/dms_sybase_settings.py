from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSSybaseSettings(BaseModel):
    DatabaseName: StrictStr | None = None
    Password: StrictStr | None = None
    Port: StrictInt | None = None
    ServerName: StrictStr | None = None
    Username: StrictStr | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
