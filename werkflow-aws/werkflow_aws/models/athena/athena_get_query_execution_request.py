from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetQueryExecutionRequest(BaseModel):
    QueryExecutionId: StrictStr
    