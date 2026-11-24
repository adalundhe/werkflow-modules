from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_path_type import QuickSightDataPathType


class QuickSightDataPathValue(BaseModel):
    FieldId: StrictStr | None = None
    FieldValue: StrictStr | None = None
    DataPathType: QuickSightDataPathType | None = None
