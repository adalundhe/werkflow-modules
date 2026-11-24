from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_geometry import ComprehendGeometry
from .comprehend_relationships_list_item import ComprehendRelationshipsListItem


class ComprehendBlock(BaseModel):
    Id: StrictStr | None = None
    BlockType: StrictStr | None = None
    Text: StrictStr | None = None
    Page: StrictInt | None = None
    Geometry: ComprehendGeometry | None = None
    Relationships: list[ComprehendRelationshipsListItem] | None = None
