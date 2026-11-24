from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .athena_engine_version_model import AthenaEngineVersionModel


class AthenaWorkGroupSummary(BaseModel):
    Name: StrictStr | None = None
    State: StrictStr | None = None
    Description: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EngineVersion: AthenaEngineVersionModel | None = None
    IdentityCenterApplicationArn: StrictStr | None = None
