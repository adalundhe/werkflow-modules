from __future__ import annotations
from pydantic import BaseModel
from .glue_batch_get_table_optimizer_entry import GlueBatchGetTableOptimizerEntry


class GlueBatchGetTableOptimizerRequest(BaseModel):
    Entries: list[GlueBatchGetTableOptimizerEntry]
