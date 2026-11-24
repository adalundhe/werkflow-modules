from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_reserved_node_offering import RedshiftReservedNodeOffering


class RedshiftGetReservedNodeExchangeOfferingsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReservedNodeOfferings: list[RedshiftReservedNodeOffering] | None = None
    ResponseMetadata: dict[str, Any] | None = None
