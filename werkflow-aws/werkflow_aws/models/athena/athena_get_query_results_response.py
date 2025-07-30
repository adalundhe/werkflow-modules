from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)
from .athena_result_set import AthenaResultSet


class AthenaGetQueryResultsResponse(BaseModel):
    UpdateCount: StrictInt
    ResultSet: AthenaResultSet
    NextToken: StrictStr