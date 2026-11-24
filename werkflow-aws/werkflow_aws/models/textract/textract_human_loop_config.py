from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_human_loop_data_attributes import TextractHumanLoopDataAttributes


class TextractHumanLoopConfig(BaseModel):
    HumanLoopName: StrictStr
    FlowDefinitionArn: StrictStr
    DataAttributes: TextractHumanLoopDataAttributes | None = None
