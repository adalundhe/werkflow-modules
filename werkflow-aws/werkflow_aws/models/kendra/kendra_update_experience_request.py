from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_experience_configuration import KendraExperienceConfiguration


class KendraUpdateExperienceRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
    Name: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Configuration: KendraExperienceConfiguration | None = None
    Description: StrictStr | None = None
