from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .athena_work_group_configuration_updates import AthenaWorkGroupConfigurationUpdates


class AthenaUpdateWorkGroupRequest(BaseModel):
    WorkGroup: StrictStr
    Description: StrictStr | None = None
    ConfigurationUpdates: AthenaWorkGroupConfigurationUpdates | None = None
    State: Literal['ENABLED', 'DISABLED'] | None = None
