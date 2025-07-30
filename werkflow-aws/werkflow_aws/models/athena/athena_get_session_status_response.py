from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_session_status import AthenaSessionStatus


class AthenaGetSessionStatusResponse(BaseModel):
    SessionId: StrictStr
    Status: AthenaSessionStatus