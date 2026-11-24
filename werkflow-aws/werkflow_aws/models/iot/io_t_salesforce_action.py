from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSalesforceAction(BaseModel):
    token: StrictStr | None = None
    url: StrictStr | None = None
