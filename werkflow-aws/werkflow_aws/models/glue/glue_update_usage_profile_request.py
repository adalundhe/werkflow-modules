from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_profile_configuration import GlueProfileConfiguration


class GlueUpdateUsageProfileRequest(BaseModel):
    Name: StrictStr
    Configuration: GlueProfileConfiguration
    Description: StrictStr | None = None
