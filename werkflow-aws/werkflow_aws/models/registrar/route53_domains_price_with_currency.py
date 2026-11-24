from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class Route53DomainsPriceWithCurrency(BaseModel):
    Price: StrictFloat | StrictInt | None = None
    Currency: StrictStr | None = None
    PriceType: StrictStr | None = None
