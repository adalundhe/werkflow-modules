from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexObfuscationSetting(BaseModel):
    obfuscationSettingType: StrictStr | None = None
