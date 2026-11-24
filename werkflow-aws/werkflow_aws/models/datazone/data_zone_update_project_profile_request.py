from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_environment_configuration import DataZoneEnvironmentConfiguration
from .data_zone_resource_tag_parameter import DataZoneResourceTagParameter


class DataZoneUpdateProjectProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: Literal['ENABLED', 'DISABLED'] | None = None
    projectResourceTags: list[DataZoneResourceTagParameter] | None = None
    allowCustomProjectResourceTags: StrictBool | None = None
    projectResourceTagsDescription: StrictStr | None = None
    environmentConfigurations: list[DataZoneEnvironmentConfiguration] | None = None
    domainUnitIdentifier: StrictStr | None = None
