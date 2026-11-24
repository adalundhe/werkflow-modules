from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSArgoCdNetworkAccessConfigRequest(BaseModel):
    vpceIds: list[StrictStr] | None = None
