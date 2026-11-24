from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateOptionGroupRequest(BaseModel):
    OptionGroupName: StrictStr
    EngineName: StrictStr
    MajorEngineVersion: StrictStr
    OptionGroupDescription: StrictStr
    Tags: list[RDSTagModel] | None = None
