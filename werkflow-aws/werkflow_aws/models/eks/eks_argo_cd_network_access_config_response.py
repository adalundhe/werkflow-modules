from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSArgoCdNetworkAccessConfigResponse(BaseModel):
    vpceIds: list[StrictStr] | None = None
