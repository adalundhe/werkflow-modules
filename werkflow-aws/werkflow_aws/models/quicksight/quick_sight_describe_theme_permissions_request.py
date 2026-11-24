from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeThemePermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
