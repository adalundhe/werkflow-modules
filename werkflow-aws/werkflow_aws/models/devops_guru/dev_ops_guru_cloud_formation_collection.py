from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruCloudFormationCollection(BaseModel):
    StackNames: list[StrictStr] | None = None
