from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDescribeThemeRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
    VersionNumber: StrictInt | None = None
    AliasName: StrictStr | None = None
