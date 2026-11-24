from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateThemeAliasRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
    AliasName: StrictStr
    ThemeVersionNumber: StrictInt
