from pydantic import BaseModel
from .athena_result_set import AthenaResultSet
from .athena_result_set_metadata import AthenaResultSetMetadata


class AthenaResultSet(BaseModel):
    Rows: list[AthenaResultSet]
    ResultSetMetadata: AthenaResultSetMetadata