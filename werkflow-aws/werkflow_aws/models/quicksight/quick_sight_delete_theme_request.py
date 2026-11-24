from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeleteThemeRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
    VersionNumber: StrictInt | None = None
