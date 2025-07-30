from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_engine_configuration import AthenaEngineConfiguration
from .athena_session_configuration import AthenaSessionConfiguration
from .athena_session_status import AthenaSessionStatus
from .athena_session_statistics import AthenaSessionStatistics


class AthenaGetSessionResponse(BaseModel):
    SessionId: StrictStr
    Description: StrictStr | None = None
    WorkGroup: StrictStr | None = None
    EngineVersion: StrictStr
    EngineConfiguration: AthenaEngineConfiguration
    NotebookVersion: StrictStr
    SessionConfiguration: AthenaSessionConfiguration
    Status: AthenaSessionStatus
    Statistics: AthenaSessionStatistics
