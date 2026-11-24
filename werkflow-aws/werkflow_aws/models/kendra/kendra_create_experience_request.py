from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_experience_configuration import KendraExperienceConfiguration


class KendraCreateExperienceRequest(BaseModel):
    Name: StrictStr
    IndexId: StrictStr
    RoleArn: StrictStr | None = None
    Configuration: KendraExperienceConfiguration | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
