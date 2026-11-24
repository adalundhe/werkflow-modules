from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2NitroTpmInfo(BaseModel):
    SupportedVersions: list[StrictStr] | None = None
