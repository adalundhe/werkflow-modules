from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_entity_persona_configuration import KendraEntityPersonaConfiguration


class KendraAssociatePersonasToEntitiesRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
    Personas: list[KendraEntityPersonaConfiguration]
