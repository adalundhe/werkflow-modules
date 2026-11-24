from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_configuration import DataZoneConfiguration
from .data_zone_connection_credentials import DataZoneConnectionCredentials
from .data_zone_connection_properties_output import DataZoneConnectionPropertiesOutput
from .data_zone_physical_endpoint import DataZonePhysicalEndpoint


class DataZoneGetConnectionResponse(BaseModel):
    connectionCredentials: DataZoneConnectionCredentials | None = None
    configurations: list[DataZoneConfiguration] | None = None
    connectionId: StrictStr | None = None
    description: StrictStr | None = None
    domainId: StrictStr | None = None
    domainUnitId: StrictStr | None = None
    environmentId: StrictStr | None = None
    environmentUserRole: StrictStr | None = None
    name: StrictStr | None = None
    physicalEndpoints: list[DataZonePhysicalEndpoint] | None = None
    projectId: StrictStr | None = None
    props: DataZoneConnectionPropertiesOutput | None = None
    type: StrictStr | None = None
    scope: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
