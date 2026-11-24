from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .screen_types import ScreenTypes


class ScreenSchemeDetails(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    screens: ScreenTypes | None = None
