from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    StrictBool,
)
from .athena_column_nullable import AthenaColumnNullable


class AthenaColumnInfo(BaseModel):
    CatalogName: StrictStr
    SchemaName: StrictStr
    TableName: StrictStr
    Label: StrictStr
    Type: StrictStr
    Precision: StrictInt
    Scale: StrictInt
    Nullable: AthenaColumnNullable
    CaseSensitive: StrictBool = False