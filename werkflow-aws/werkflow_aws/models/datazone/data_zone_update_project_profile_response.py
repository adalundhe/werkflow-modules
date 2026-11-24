from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_environment_configuration import DataZoneEnvironmentConfiguration
from .data_zone_resource_tag_parameter import DataZoneResourceTagParameter


class DataZoneUpdateProjectProfileResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    projectResourceTags: list[DataZoneResourceTagParameter] | None = None
    allowCustomProjectResourceTags: StrictBool | None = None
    projectResourceTagsDescription: StrictStr | None = None
    environmentConfigurations: list[DataZoneEnvironmentConfiguration] | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    domainUnitId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
