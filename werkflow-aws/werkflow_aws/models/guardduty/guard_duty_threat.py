from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_item_details import GuardDutyItemDetails
from .guard_duty_item_path import GuardDutyItemPath


class GuardDutyThreat(BaseModel):
    Name: StrictStr | None = None
    Source: StrictStr | None = None
    ItemPaths: list[GuardDutyItemPath] | None = None
    Count: StrictInt | None = None
    Hash: StrictStr | None = None
    ItemDetails: list[GuardDutyItemDetails] | None = None
