from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaStartQueryExecutionResponse(BaseModel):
    QueryExecutionId: StrictStr