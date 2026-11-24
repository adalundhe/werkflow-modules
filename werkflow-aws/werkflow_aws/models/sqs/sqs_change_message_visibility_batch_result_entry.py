from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSChangeMessageVisibilityBatchResultEntry(BaseModel):
    Id: StrictStr | None = None
