from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyFargateDetails(BaseModel):
    Issues: list[StrictStr] | None = None
    ManagementType: StrictStr | None = None
