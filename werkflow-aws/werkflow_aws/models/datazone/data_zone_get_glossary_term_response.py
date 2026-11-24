from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_term_relations import DataZoneTermRelations


class DataZoneGetGlossaryTermResponse(BaseModel):
    domainId: StrictStr | None = None
    glossaryId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    shortDescription: StrictStr | None = None
    longDescription: StrictStr | None = None
    termRelations: DataZoneTermRelations | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    usageRestrictions: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
