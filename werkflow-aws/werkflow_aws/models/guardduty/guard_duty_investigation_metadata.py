from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_product import GuardDutyProduct


class GuardDutyInvestigationMetadata(BaseModel):
    Version: StrictStr | None = None
    Product: GuardDutyProduct | None = None
