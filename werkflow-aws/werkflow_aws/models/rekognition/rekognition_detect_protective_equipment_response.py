from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_protective_equipment_person import RekognitionProtectiveEquipmentPerson
from .rekognition_protective_equipment_summary import RekognitionProtectiveEquipmentSummary


class RekognitionDetectProtectiveEquipmentResponse(BaseModel):
    ProtectiveEquipmentModelVersion: StrictStr | None = None
    Persons: list[RekognitionProtectiveEquipmentPerson] | None = None
    Summary: RekognitionProtectiveEquipmentSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
