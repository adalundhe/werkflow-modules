from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGroup(BaseModel):
    Arn: StrictStr | None = None
    GroupName: StrictStr | None = None
    Description: StrictStr | None = None
    PrincipalId: StrictStr | None = None
