from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_engine_version import AthenaEngineVersion
from .athena_session_status import AthenaSessionStatus


class AthenaSession(BaseModel):
    SessionId: StrictStr
    Description: StrictStr | None = None
    EngineVersion: AthenaEngineVersion
    NotebookVersion: StrictStr
    Status: AthenaSessionStatus
