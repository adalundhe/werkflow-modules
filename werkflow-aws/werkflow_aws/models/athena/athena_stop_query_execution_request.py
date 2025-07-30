from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaStopQueryExecutionRequest(BaseModel):
    QueryExecutionId: StrictStr