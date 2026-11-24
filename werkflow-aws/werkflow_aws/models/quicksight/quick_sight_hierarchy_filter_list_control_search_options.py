from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightHierarchyFilterListControlSearchOptions(BaseModel):
    Visibility: StrictStr | None = None
