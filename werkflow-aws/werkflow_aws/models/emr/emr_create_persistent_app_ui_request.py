from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .emr_containers_config import EMRContainersConfig as _EMRContainersConfigType
from .emr_tag import EMRTag


class EMRCreatePersistentAppUIRequest(BaseModel):
    TargetResourceArn: StrictStr
    EMRContainersConfig: _EMRContainersConfigType | None = None
    Tags: list[EMRTag] | None = None
    XReferer: StrictStr | None = None
    ProfilerType: Literal['SHS', 'TEZUI', 'YTS'] | None = None
