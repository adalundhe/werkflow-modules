from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class IoTRoleAliasDescription(BaseModel):
    roleAlias: StrictStr | None = None
    roleAliasArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    owner: StrictStr | None = None
    credentialDurationSeconds: StrictInt | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
