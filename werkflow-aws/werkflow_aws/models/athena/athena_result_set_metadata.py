from pydantic import BaseModel
from .athena_column_info import AthenaColumnInfo


class AthenaResultSetMetadata(BaseModel):
    ColumnInfo: list[AthenaColumnInfo]