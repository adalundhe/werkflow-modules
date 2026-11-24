from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_custom_parameter import DataZoneCustomParameter


class DataZoneUpdateEnvironmentProfileResponse(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    awsAccountId: StrictStr | None = None
    awsAccountRegion: StrictStr | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    environmentBlueprintId: StrictStr | None = None
    projectId: StrictStr | None = None
    userParameters: list[DataZoneCustomParameter] | None = None
    ResponseMetadata: dict[str, Any] | None = None
