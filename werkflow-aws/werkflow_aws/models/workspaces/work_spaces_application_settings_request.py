from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesApplicationSettingsRequest(BaseModel):
    Status: Literal['DISABLED', 'ENABLED']
    SettingsGroup: StrictStr | None = None
