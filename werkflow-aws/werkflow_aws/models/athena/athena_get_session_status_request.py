from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetSessionStatusRequest(BaseModel):
    SessionId: StrictStr