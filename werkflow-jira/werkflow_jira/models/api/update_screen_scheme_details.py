from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .update_screen_types import UpdateScreenTypes


class UpdateScreenSchemeDetails(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    screens: UpdateScreenTypes | None = None
