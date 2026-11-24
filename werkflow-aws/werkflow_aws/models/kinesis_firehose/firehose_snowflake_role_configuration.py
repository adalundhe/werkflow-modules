from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FirehoseSnowflakeRoleConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    SnowflakeRole: StrictStr | None = None
