from pydantic import BaseModel
from .athena_session_state import AthenaSessionState


class AthenaTerminateSessionResponse(BaseModel):
    State: AthenaSessionState