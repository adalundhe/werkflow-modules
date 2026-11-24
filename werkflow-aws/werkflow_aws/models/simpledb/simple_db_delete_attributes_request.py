from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .simple_db_attribute import SimpleDBAttribute
from .simple_db_update_condition import SimpleDBUpdateCondition


class SimpleDBDeleteAttributesRequest(BaseModel):
    DomainName: StrictStr
    ItemName: StrictStr
    Attributes: list[SimpleDBAttribute] | None = None
    Expected: SimpleDBUpdateCondition | None = None
