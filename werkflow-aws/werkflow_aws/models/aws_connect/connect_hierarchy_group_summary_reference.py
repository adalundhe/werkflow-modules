from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectHierarchyGroupSummaryReference(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
