from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaDeleteNamedQueryRequest(BaseModel):
    NamedQueryId: StrictStr