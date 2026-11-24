from pydantic import BaseModel, StrictInt, StrictStr
from .athena_result_set import AthenaResultSet


class AthenaGetQueryResultsResponse(BaseModel):
    UpdateCount: StrictInt | None = None
    ResultSet: AthenaResultSet | None = None
    NextToken: StrictStr | None = None
