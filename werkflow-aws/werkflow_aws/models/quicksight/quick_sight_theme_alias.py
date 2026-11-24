from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightThemeAlias(BaseModel):
    Arn: StrictStr | None = None
    AliasName: StrictStr | None = None
    ThemeVersionNumber: StrictInt | None = None
