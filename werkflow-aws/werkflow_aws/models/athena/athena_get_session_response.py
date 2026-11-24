from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_engine_configuration import AthenaEngineConfiguration
from .athena_session_configuration import AthenaSessionConfiguration
from .athena_session_status import AthenaSessionStatus
from .athena_session_statistics import AthenaSessionStatistics


class AthenaGetSessionResponse(BaseModel):
    SessionId: StrictStr | None = None
    Description: StrictStr | None = None
    WorkGroup: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    EngineConfiguration: AthenaEngineConfiguration | None = None
    NotebookVersion: StrictStr | None = None
    SessionConfiguration: AthenaSessionConfiguration | None = None
    Status: AthenaSessionStatus | None = None
    Statistics: AthenaSessionStatistics | None = None
