from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightItemsLimitConfiguration(BaseModel):
    ItemsLimit: StrictInt | None = None
    OtherCategories: StrictStr | None = None
