from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .simple_db_replaceable_item import SimpleDBReplaceableItem


class SimpleDBBatchPutAttributesRequest(BaseModel):
    DomainName: StrictStr
    Items: list[SimpleDBReplaceableItem]
