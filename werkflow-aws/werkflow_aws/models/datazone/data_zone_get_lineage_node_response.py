from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_form_output import DataZoneFormOutput
from .data_zone_lineage_node_reference import DataZoneLineageNodeReference


class DataZoneGetLineageNodeResponse(BaseModel):
    domainId: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    id: StrictStr | None = None
    typeName: StrictStr | None = None
    typeRevision: StrictStr | None = None
    sourceIdentifier: StrictStr | None = None
    eventTimestamp: datetime.datetime | StrictStr | None = None
    formsOutput: list[DataZoneFormOutput] | None = None
    upstreamNodes: list[DataZoneLineageNodeReference] | None = None
    downstreamNodes: list[DataZoneLineageNodeReference] | None = None
    ResponseMetadata: dict[str, Any] | None = None
