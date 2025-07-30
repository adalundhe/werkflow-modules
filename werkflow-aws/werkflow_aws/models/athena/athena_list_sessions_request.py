from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)
from .athena_session_state import AthenaSessionState


class AthenaListSessionsRequest(BaseModel):
    WorkGroup: StrictStr
    StateFilter: AthenaSessionState | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None