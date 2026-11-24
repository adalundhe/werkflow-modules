from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCopyDBParameterGroupRequest(BaseModel):
    SourceDBParameterGroupIdentifier: StrictStr
    TargetDBParameterGroupIdentifier: StrictStr
    TargetDBParameterGroupDescription: StrictStr
    Tags: list[RDSTagModel] | None = None
