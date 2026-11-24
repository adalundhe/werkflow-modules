from pydantic import BaseModel, StrictStr
from .athena_session import AthenaSession


class AthenaListSessionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Sessions: list[AthenaSession] | None = None
