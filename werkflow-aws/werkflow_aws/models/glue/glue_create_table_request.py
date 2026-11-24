from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_open_table_format_input import GlueOpenTableFormatInput
from .glue_partition_index import GluePartitionIndex
from .glue_table_input import GlueTableInput


class GlueCreateTableRequest(BaseModel):
    DatabaseName: StrictStr
    CatalogId: StrictStr | None = None
    Name: StrictStr | None = None
    TableInput: GlueTableInput | None = None
    PartitionIndexes: list[GluePartitionIndex] | None = None
    TransactionId: StrictStr | None = None
    OpenTableFormatInput: GlueOpenTableFormatInput | None = None
