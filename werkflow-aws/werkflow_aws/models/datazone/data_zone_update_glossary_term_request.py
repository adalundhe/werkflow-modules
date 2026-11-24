from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_term_relations import DataZoneTermRelations


class DataZoneUpdateGlossaryTermRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    glossaryIdentifier: StrictStr | None = None
    name: StrictStr | None = None
    shortDescription: StrictStr | None = None
    longDescription: StrictStr | None = None
    termRelations: DataZoneTermRelations | None = None
    status: Literal['ENABLED', 'DISABLED'] | None = None
