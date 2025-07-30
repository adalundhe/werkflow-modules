import datetime
from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_session_state import AthenaSessionState


class AthenaSessionStatus(BaseModel):
    StartDateTime: datetime.datetime
    LastModifiedDateTime: datetime.datetime
    EndDateTime: datetime.datetime
    IdleSinceDateTime: datetime.datetime
    State: AthenaSessionState
    StateChangeReason: StrictStr
