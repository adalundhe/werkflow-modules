from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCopyOptionGroupRequest(BaseModel):
    SourceOptionGroupIdentifier: StrictStr
    TargetOptionGroupIdentifier: StrictStr
    TargetOptionGroupDescription: StrictStr
    Tags: list[RDSTagModel] | None = None
