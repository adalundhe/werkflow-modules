from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaListQueryExecutionsResponse(BaseModel):
    QueryExecutionIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
