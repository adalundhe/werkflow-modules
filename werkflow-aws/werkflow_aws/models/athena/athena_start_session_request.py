from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt
)
from .athena_engine_configuration import AthenaEngineConfiguration


class AthenaStartSessionRequest(BaseModel):
    Description: StrictStr | None = None
    WorkGroup: StrictStr
    EngineConfiguration: AthenaEngineConfiguration
    NotebookVersion: StrictStr | None = None
    SessionIdleTimeoutInMinutes: StrictInt | None = None
    ClientRequestToken: StrictStr | None = None
    