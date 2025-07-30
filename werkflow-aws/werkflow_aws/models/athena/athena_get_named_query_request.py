from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetNamedQueryRequest(BaseModel):
    NamedQueryId: StrictStr