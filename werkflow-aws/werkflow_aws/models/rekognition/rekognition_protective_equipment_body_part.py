from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_equipment_detection import RekognitionEquipmentDetection


class RekognitionProtectiveEquipmentBodyPart(BaseModel):
    Name: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    EquipmentDetections: list[RekognitionEquipmentDetection] | None = None
