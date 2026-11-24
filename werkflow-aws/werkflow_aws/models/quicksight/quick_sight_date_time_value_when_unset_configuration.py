from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightDateTimeValueWhenUnsetConfiguration(BaseModel):
    ValueWhenUnsetOption: StrictStr | None = None
    CustomValue: datetime.datetime | StrictStr | None = None
