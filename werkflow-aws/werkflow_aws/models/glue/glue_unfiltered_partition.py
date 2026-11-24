from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_partition import GluePartition


class GlueUnfilteredPartition(BaseModel):
    Partition: GluePartition | None = None
    AuthorizedColumns: list[StrictStr] | None = None
    IsRegisteredWithLakeFormation: StrictBool | None = None
