from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_profile_configuration import GlueProfileConfiguration


class GlueCreateUsageProfileRequest(BaseModel):
    Name: StrictStr
    Configuration: GlueProfileConfiguration
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
