from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_auth_configuration import GlueAuthConfiguration
from .glue_capabilities import GlueCapabilities
from .glue_compute_environment_configuration import GlueComputeEnvironmentConfiguration
from .glue_property import GlueProperty
from .glue_rest_configuration import GlueRestConfiguration


class GlueDescribeConnectionTypeResponse(BaseModel):
    ConnectionType: StrictStr | None = None
    Description: StrictStr | None = None
    Capabilities: GlueCapabilities | None = None
    ConnectionProperties: dict[StrictStr, GlueProperty] | None = None
    ConnectionOptions: dict[StrictStr, GlueProperty] | None = None
    AuthenticationConfiguration: GlueAuthConfiguration | None = None
    ComputeEnvironmentConfigurations: dict[StrictStr, GlueComputeEnvironmentConfiguration] | None = None
    PhysicalConnectionRequirements: dict[StrictStr, GlueProperty] | None = None
    AthenaConnectionProperties: dict[StrictStr, GlueProperty] | None = None
    PythonConnectionProperties: dict[StrictStr, GlueProperty] | None = None
    SparkConnectionProperties: dict[StrictStr, GlueProperty] | None = None
    RestConfiguration: GlueRestConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
