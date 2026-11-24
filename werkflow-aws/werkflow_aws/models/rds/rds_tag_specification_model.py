from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSTagSpecificationModel(BaseModel):
    ResourceType: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
