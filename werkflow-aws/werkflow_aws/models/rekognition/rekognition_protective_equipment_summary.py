from __future__ import annotations
from pydantic import BaseModel, StrictInt


class RekognitionProtectiveEquipmentSummary(BaseModel):
    PersonsWithRequiredEquipment: list[StrictInt] | None = None
    PersonsWithoutRequiredEquipment: list[StrictInt] | None = None
    PersonsIndeterminate: list[StrictInt] | None = None
