from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_profile_configuration import GlueProfileConfiguration


class GlueGetUsageProfileResponse(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Configuration: GlueProfileConfiguration | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
