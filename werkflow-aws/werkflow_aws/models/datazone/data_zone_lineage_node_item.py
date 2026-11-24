from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_form_output import DataZoneFormOutput


class DataZoneLineageNodeItem(BaseModel):
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
    upstreamLineageNodeIds: list[StrictStr] | None = None
    downstreamLineageNodeIds: list[StrictStr] | None = None
