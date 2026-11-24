from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruUpdateCloudFormationCollectionFilter(BaseModel):
    StackNames: list[StrictStr] | None = None
