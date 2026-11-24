from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .simple_db_replaceable_attribute import SimpleDBReplaceableAttribute
from .simple_db_update_condition import SimpleDBUpdateCondition


class SimpleDBPutAttributesRequest(BaseModel):
    DomainName: StrictStr
    ItemName: StrictStr
    Attributes: list[SimpleDBReplaceableAttribute]
    Expected: SimpleDBUpdateCondition | None = None
