from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCopyDBClusterParameterGroupRequest(BaseModel):
    SourceDBClusterParameterGroupIdentifier: StrictStr
    TargetDBClusterParameterGroupIdentifier: StrictStr
    TargetDBClusterParameterGroupDescription: StrictStr
    Tags: list[RDSTagModel] | None = None
