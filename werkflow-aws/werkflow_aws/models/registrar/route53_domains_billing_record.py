from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class Route53DomainsBillingRecord(BaseModel):
    DomainName: StrictStr | None = None
    Operation: StrictStr | None = None
    InvoiceId: StrictStr | None = None
    BillDate: datetime.datetime | StrictStr | None = None
    Price: StrictFloat | StrictInt | None = None
