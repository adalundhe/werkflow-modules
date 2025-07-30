from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaTerminateSessionRequest(BaseModel):
    SessionId: StrictStr