from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_session import AthenaSession


class AthenaListSessionsResponse(BaseModel):
    NextToken: StrictStr
    Sessions: list[AthenaSession]