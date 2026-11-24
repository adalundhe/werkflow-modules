from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseSnowflakeVpcConfiguration(BaseModel):
    PrivateLinkVpceId: StrictStr | None = None
