from __future__ import annotations
from pydantic import BaseModel
from .batch_eks_access_entry import BatchEksAccessEntry


class BatchEksConfigurationUpdate(BaseModel):
    accessEntry: BatchEksAccessEntry | None = None
