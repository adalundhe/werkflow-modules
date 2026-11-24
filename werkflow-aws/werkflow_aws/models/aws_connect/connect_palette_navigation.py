from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectPaletteNavigation(BaseModel):
    Background: StrictStr | None = None
    TextBackgroundHover: StrictStr | None = None
    TextBackgroundActive: StrictStr | None = None
    Text: StrictStr | None = None
    TextHover: StrictStr | None = None
    TextActive: StrictStr | None = None
    InvertActionsColors: StrictBool | None = None
