from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSUpdateLabelsPayload(BaseModel):
    addOrUpdateLabels: dict[StrictStr, StrictStr] | None = None
    removeLabels: list[StrictStr] | None = None
