from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_batch_update_partition_request_entry import GlueBatchUpdatePartitionRequestEntry


class GlueBatchUpdatePartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    Entries: list[GlueBatchUpdatePartitionRequestEntry]
    CatalogId: StrictStr | None = None
