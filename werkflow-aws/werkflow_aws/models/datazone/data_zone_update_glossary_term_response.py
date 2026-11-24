from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_term_relations import DataZoneTermRelations


class DataZoneUpdateGlossaryTermResponse(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    glossaryId: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    shortDescription: StrictStr | None = None
    longDescription: StrictStr | None = None
    termRelations: DataZoneTermRelations | None = None
    usageRestrictions: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
