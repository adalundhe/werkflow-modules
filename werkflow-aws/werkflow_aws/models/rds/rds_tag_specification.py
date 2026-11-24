from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag import RDSTag


class RDSTagSpecification(BaseModel):
    ResourceType: StrictStr | None = None
    Tags: list[RDSTag] | None = None
