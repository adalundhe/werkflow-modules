from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_import import DataZoneImport
from .data_zone_model import DataZoneModel


class DataZoneFormTypeData(BaseModel):
    domainId: StrictStr | None = None
    name: StrictStr | None = None
    revision: StrictStr | None = None
    model: DataZoneModel | None = None
    status: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    originDomainId: StrictStr | None = None
    originProjectId: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    description: StrictStr | None = None
    imports: list[DataZoneImport] | None = None
