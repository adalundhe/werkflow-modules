from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSDeleteMessageBatchResultEntry(BaseModel):
    Id: StrictStr | None = None
