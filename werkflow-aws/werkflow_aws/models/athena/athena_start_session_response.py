from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_session_state import AthenaSessionState


class AthenaStartSessionResponse(BaseModel):
    SessionId: StrictStr | None = None
    State: AthenaSessionState | None = None
