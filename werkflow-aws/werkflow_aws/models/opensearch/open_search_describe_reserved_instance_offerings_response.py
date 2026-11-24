from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_reserved_instance_offering import OpenSearchReservedInstanceOffering


class OpenSearchDescribeReservedInstanceOfferingsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ReservedInstanceOfferings: list[OpenSearchReservedInstanceOffering] | None = None
    ResponseMetadata: dict[str, Any] | None = None
