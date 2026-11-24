from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_authentication_configuration import DataZoneAuthenticationConfiguration
from .data_zone_physical_connection_requirements import DataZonePhysicalConnectionRequirements


class DataZoneGlueConnection(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    connectionType: StrictStr | None = None
    matchCriteria: list[StrictStr] | None = None
    connectionProperties: dict[StrictStr, StrictStr] | None = None
    sparkProperties: dict[StrictStr, StrictStr] | None = None
    athenaProperties: dict[StrictStr, StrictStr] | None = None
    pythonProperties: dict[StrictStr, StrictStr] | None = None
    physicalConnectionRequirements: DataZonePhysicalConnectionRequirements | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    lastConnectionValidationTime: datetime.datetime | StrictStr | None = None
    authenticationConfiguration: DataZoneAuthenticationConfiguration | None = None
    connectionSchemaVersion: StrictInt | None = None
    compatibleComputeEnvironments: list[StrictStr] | None = None
