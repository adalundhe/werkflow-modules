from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_configuration_object import GlueConfigurationObject


class GlueProfileConfiguration(BaseModel):
    SessionConfiguration: dict[StrictStr, GlueConfigurationObject] | None = None
    JobConfiguration: dict[StrictStr, GlueConfigurationObject] | None = None
