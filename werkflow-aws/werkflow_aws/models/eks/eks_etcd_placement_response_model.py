from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSEtcdPlacementResponseModel(BaseModel):
    spreadLevel: StrictStr | None = None
