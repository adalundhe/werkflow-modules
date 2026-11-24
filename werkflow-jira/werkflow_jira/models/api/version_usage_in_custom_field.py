from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class VersionUsageInCustomField(BaseModel):
    customFieldId: StrictInt | None = None
    fieldName: StrictStr | None = None
    issueCountWithVersionInCustomField: StrictInt | None = None
