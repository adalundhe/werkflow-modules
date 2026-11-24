from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruCloudFormationCollectionFilter(BaseModel):
    StackNames: list[StrictStr] | None = None
