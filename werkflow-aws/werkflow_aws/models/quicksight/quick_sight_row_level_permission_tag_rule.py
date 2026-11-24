from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRowLevelPermissionTagRule(BaseModel):
    TagKey: StrictStr | None = None
    ColumnName: StrictStr | None = None
    TagMultiValueDelimiter: StrictStr | None = None
    MatchAllValue: StrictStr | None = None
