from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionProtectiveEquipmentSummarizationAttributes(BaseModel):
    MinConfidence: StrictFloat | StrictInt
    RequiredEquipmentTypes: list[Literal['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']]
