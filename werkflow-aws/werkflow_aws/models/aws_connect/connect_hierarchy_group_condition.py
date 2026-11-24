from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectHierarchyGroupCondition(BaseModel):
    Value: StrictStr | None = None
    HierarchyGroupMatchType: Literal['EXACT', 'WITH_CHILD_GROUPS'] | None = None
