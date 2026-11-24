from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_table_optimizer_configuration import GlueTableOptimizerConfiguration


class GlueUpdateTableOptimizerRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
    Type: Literal['compaction', 'retention', 'orphan_file_deletion']
    TableOptimizerConfiguration: GlueTableOptimizerConfiguration
