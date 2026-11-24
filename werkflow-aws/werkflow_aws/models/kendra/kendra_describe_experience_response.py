from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_experience_configuration import KendraExperienceConfiguration
from .kendra_experience_endpoint import KendraExperienceEndpoint


class KendraDescribeExperienceResponse(BaseModel):
    Id: StrictStr | None = None
    IndexId: StrictStr | None = None
    Name: StrictStr | None = None
    Endpoints: list[KendraExperienceEndpoint] | None = None
    Configuration: KendraExperienceConfiguration | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
