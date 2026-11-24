from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_authentication_configuration_input import GlueAuthenticationConfigurationInput
from .glue_physical_connection_requirements import GluePhysicalConnectionRequirements


class GlueConnectionInput(BaseModel):
    Name: StrictStr
    ConnectionType: StrictStr
    ConnectionProperties: dict[StrictStr, StrictStr]
    Description: StrictStr | None = None
    MatchCriteria: list[StrictStr] | None = None
    SparkProperties: dict[StrictStr, StrictStr] | None = None
    AthenaProperties: dict[StrictStr, StrictStr] | None = None
    PythonProperties: dict[StrictStr, StrictStr] | None = None
    PhysicalConnectionRequirements: GluePhysicalConnectionRequirements | None = None
    AuthenticationConfiguration: GlueAuthenticationConfigurationInput | None = None
    ValidateCredentials: StrictBool | None = None
    ValidateForComputeEnvironments: list[Literal['SPARK', 'ATHENA', 'PYTHON']] | None = None
