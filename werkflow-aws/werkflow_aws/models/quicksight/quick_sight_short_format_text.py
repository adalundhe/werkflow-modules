from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightShortFormatText(BaseModel):
    PlainText: StrictStr | None = None
    RichText: StrictStr | None = None
