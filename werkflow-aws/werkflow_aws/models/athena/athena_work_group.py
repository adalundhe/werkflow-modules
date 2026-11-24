from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .athena_work_group_configuration import AthenaWorkGroupConfiguration


class AthenaWorkGroup(BaseModel):
    Name: StrictStr | None = None
    State: StrictStr | None = None
    Configuration: AthenaWorkGroupConfiguration | None = None
    Description: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    IdentityCenterApplicationArn: StrictStr | None = None
