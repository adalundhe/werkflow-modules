from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetSessionRequest(BaseModel):
    SessionId: StrictStr