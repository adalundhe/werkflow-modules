from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_human_loop_data_attributes import RekognitionHumanLoopDataAttributes


class RekognitionHumanLoopConfig(BaseModel):
    HumanLoopName: StrictStr
    FlowDefinitionArn: StrictStr
    DataAttributes: RekognitionHumanLoopDataAttributes | None = None
