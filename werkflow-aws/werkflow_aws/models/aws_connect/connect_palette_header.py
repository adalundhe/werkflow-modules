from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectPaletteHeader(BaseModel):
    Background: StrictStr | None = None
    Text: StrictStr | None = None
    TextHover: StrictStr | None = None
    InvertActionsColors: StrictBool | None = None
