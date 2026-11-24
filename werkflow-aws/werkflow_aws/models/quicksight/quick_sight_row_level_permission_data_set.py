from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRowLevelPermissionDataSet(BaseModel):
    Namespace: StrictStr | None = None
    Arn: StrictStr | None = None
    PermissionPolicy: StrictStr | None = None
    FormatVersion: StrictStr | None = None
    Status: StrictStr | None = None
