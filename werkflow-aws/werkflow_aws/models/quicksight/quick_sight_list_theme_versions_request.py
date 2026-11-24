from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListThemeVersionsRequest(BaseModel):
    AwsAccountId: StrictStr
    ThemeId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
