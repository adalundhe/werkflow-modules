from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectResourceTag(BaseModel):
    resourceArn: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
