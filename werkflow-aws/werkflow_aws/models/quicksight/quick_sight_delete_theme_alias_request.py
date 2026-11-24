from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteThemeAliasRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
    AliasName: StrictStr
