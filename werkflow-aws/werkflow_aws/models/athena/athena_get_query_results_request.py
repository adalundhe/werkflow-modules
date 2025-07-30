from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)
from .athena_query_result_type import AthenaQueryResultType


class AthenaGetQueryResultsRequest(BaseModel):
    QueryExecutionId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    QueryResultType: AthenaQueryResultType | None = None