from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppStreamApplicationSettings(BaseModel):
    Enabled: StrictBool
    SettingsGroup: StrictStr | None = None
