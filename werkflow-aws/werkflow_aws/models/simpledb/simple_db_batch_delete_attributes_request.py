from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .simple_db_deletable_item import SimpleDBDeletableItem


class SimpleDBBatchDeleteAttributesRequest(BaseModel):
    DomainName: StrictStr
    Items: list[SimpleDBDeletableItem]
