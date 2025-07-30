from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_query_execution_context import AthenaQueryExecutionContext
from .athena_result_configuration import AthenaResultConfigruation
from .athena_result_reuse_configuration import AthenaResultReuseConfiguration


class AthenaStartQueryExecutionRequest(BaseModel):
    QueryString: StrictStr
    ClientRequestToken: StrictStr | None = None
    QueryExecutionContext: AthenaQueryExecutionContext | None = None
    ResultConfiguration: AthenaResultConfigruation | None = None
    WorkGroup: StrictStr | None = None
    ExecutionParameters: list[StrictStr] | None = None
    ResultReuseConfiguration: AthenaResultReuseConfiguration | None = None
