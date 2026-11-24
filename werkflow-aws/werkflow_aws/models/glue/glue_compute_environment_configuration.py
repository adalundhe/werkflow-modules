from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_property import GlueProperty


class GlueComputeEnvironmentConfiguration(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ComputeEnvironment: StrictStr | None = None
    SupportedAuthenticationTypes: list[StrictStr] | None = None
    ConnectionOptions: dict[StrictStr, GlueProperty] | None = None
    ConnectionPropertyNameOverrides: dict[StrictStr, StrictStr] | None = None
    ConnectionOptionNameOverrides: dict[StrictStr, StrictStr] | None = None
    ConnectionPropertiesRequiredOverrides: list[StrictStr] | None = None
    PhysicalConnectionPropertiesRequired: StrictBool | None = None
