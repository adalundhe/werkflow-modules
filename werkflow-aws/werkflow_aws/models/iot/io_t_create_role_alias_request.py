from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_tag import IoTTag


class IoTCreateRoleAliasRequest(BaseModel):
    roleAlias: StrictStr
    roleArn: StrictStr
    credentialDurationSeconds: StrictInt | None = None
    tags: list[IoTTag] | None = None
