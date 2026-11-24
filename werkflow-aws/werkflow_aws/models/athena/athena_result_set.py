from pydantic import BaseModel
from .athena_result_set_metadata import AthenaResultSetMetadata
from .athena_row import AthenaRow


class AthenaResultSet(BaseModel):
    Rows: list[AthenaRow] | None = None
    ResultSetMetadata: AthenaResultSetMetadata | None = None
