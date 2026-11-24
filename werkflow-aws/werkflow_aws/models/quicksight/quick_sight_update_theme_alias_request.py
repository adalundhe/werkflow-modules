from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateThemeAliasRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
    AliasName: StrictStr
    ThemeVersionNumber: StrictInt
