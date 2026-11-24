from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_additional_info import GuardDutyAdditionalInfo


class GuardDutyItemDetails(BaseModel):
    ResourceArn: StrictStr | None = None
    ItemPath: StrictStr | None = None
    Hash: StrictStr | None = None
    AdditionalInfo: GuardDutyAdditionalInfo | None = None
