from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightLongFormatText(BaseModel):
    PlainText: StrictStr | None = None
    RichText: StrictStr | None = None
