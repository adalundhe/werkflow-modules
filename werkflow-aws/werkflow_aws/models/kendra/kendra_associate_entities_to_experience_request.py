from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_entity_configuration import KendraEntityConfiguration


class KendraAssociateEntitiesToExperienceRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
    EntityList: list[KendraEntityConfiguration]
