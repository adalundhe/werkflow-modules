from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_form_entry_output import DataZoneFormEntryOutput


class DataZoneGetAssetTypeResponse(BaseModel):
    domainId: StrictStr | None = None
    name: StrictStr | None = None
    revision: StrictStr | None = None
    description: StrictStr | None = None
    formsOutput: dict[StrictStr, DataZoneFormEntryOutput] | None = None
    owningProjectId: StrictStr | None = None
    originDomainId: StrictStr | None = None
    originProjectId: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
