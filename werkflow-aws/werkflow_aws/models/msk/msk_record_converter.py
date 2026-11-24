from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKRecordConverter(BaseModel):
    ValueConverter: StrictStr | None = None
