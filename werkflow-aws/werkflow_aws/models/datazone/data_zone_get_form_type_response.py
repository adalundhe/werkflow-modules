from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_import import DataZoneImport
from .data_zone_model import DataZoneModel


class DataZoneGetFormTypeResponse(BaseModel):
    domainId: StrictStr | None = None
    name: StrictStr | None = None
    revision: StrictStr | None = None
    model: DataZoneModel | None = None
    owningProjectId: StrictStr | None = None
    originDomainId: StrictStr | None = None
    originProjectId: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    description: StrictStr | None = None
    imports: list[DataZoneImport] | None = None
    ResponseMetadata: dict[str, Any] | None = None
