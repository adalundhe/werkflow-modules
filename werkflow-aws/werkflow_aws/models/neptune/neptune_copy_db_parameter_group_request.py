from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCopyDBParameterGroupRequest(BaseModel):
    SourceDBParameterGroupIdentifier: StrictStr
    TargetDBParameterGroupIdentifier: StrictStr
    TargetDBParameterGroupDescription: StrictStr
    Tags: list[NeptuneTag] | None = None
