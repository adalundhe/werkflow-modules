from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightNullValueFormatConfiguration(BaseModel):
    NullString: StrictStr | None = None
