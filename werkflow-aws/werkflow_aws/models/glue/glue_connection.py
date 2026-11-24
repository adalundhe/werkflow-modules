from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_authentication_configuration import GlueAuthenticationConfiguration
from .glue_physical_connection_requirements import GluePhysicalConnectionRequirements


class GlueConnection(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    MatchCriteria: list[StrictStr] | None = None
    ConnectionProperties: dict[StrictStr, StrictStr] | None = None
    SparkProperties: dict[StrictStr, StrictStr] | None = None
    AthenaProperties: dict[StrictStr, StrictStr] | None = None
    PythonProperties: dict[StrictStr, StrictStr] | None = None
    PhysicalConnectionRequirements: GluePhysicalConnectionRequirements | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    LastConnectionValidationTime: datetime.datetime | StrictStr | None = None
    AuthenticationConfiguration: GlueAuthenticationConfiguration | None = None
    ConnectionSchemaVersion: StrictInt | None = None
    CompatibleComputeEnvironments: list[StrictStr] | None = None
