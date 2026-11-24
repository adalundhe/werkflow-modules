from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCopyDBClusterParameterGroupRequest(BaseModel):
    SourceDBClusterParameterGroupIdentifier: StrictStr
    TargetDBClusterParameterGroupIdentifier: StrictStr
    TargetDBClusterParameterGroupDescription: StrictStr
    Tags: list[NeptuneTag] | None = None
