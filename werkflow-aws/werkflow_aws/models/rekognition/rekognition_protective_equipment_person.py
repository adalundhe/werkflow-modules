from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_protective_equipment_body_part import RekognitionProtectiveEquipmentBodyPart


class RekognitionProtectiveEquipmentPerson(BaseModel):
    BodyParts: list[RekognitionProtectiveEquipmentBodyPart] | None = None
    BoundingBox: RekognitionBoundingBox | None = None
    Confidence: StrictFloat | StrictInt | None = None
    Id: StrictInt | None = None
