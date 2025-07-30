from pydantic import BaseModel
from .athena_query_execution import AthenaQueryExecution


class AthenaGetQueryExecutionResponse(BaseModel):
    QueryExecution: AthenaQueryExecution