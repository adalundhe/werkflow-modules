from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .athena_tag_model import AthenaTagModel
from .athena_work_group_configuration import AthenaWorkGroupConfiguration


class AthenaCreateWorkGroupRequest(BaseModel):
    Name: StrictStr
    Configuration: AthenaWorkGroupConfiguration | None = None
    Description: StrictStr | None = None
    Tags: list[AthenaTagModel] | None = None
