from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSClusterIssueModel(BaseModel):
    code: StrictStr | None = None
    message: StrictStr | None = None
    resourceIds: list[StrictStr] | None = None
