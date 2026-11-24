from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_error_detail import GlueErrorDetail


class GlueBatchUpdatePartitionFailureEntry(BaseModel):
    PartitionValueList: list[StrictStr] | None = None
    ErrorDetail: GlueErrorDetail | None = None
