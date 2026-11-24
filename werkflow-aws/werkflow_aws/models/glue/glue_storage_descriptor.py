from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_column import GlueColumn
from .glue_order import GlueOrder
from .glue_schema_reference import GlueSchemaReference
from .glue_ser_de_info import GlueSerDeInfo
from .glue_skewed_info import GlueSkewedInfo


class GlueStorageDescriptor(BaseModel):
    Columns: list[GlueColumn] | None = None
    Location: StrictStr | None = None
    AdditionalLocations: list[StrictStr] | None = None
    InputFormat: StrictStr | None = None
    OutputFormat: StrictStr | None = None
    Compressed: StrictBool | None = None
    NumberOfBuckets: StrictInt | None = None
    SerdeInfo: GlueSerDeInfo | None = None
    BucketColumns: list[StrictStr] | None = None
    SortColumns: list[GlueOrder] | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    SkewedInfo: GlueSkewedInfo | None = None
    StoredAsSubDirectories: StrictBool | None = None
    SchemaReference: GlueSchemaReference | None = None
