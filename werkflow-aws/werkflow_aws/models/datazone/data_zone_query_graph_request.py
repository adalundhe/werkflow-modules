from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_additional_attributes import DataZoneAdditionalAttributes
from .data_zone_match_clause import DataZoneMatchClause


class DataZoneQueryGraphRequest(BaseModel):
    domainIdentifier: StrictStr
    match: list[DataZoneMatchClause]
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    additionalAttributes: DataZoneAdditionalAttributes | None = None
