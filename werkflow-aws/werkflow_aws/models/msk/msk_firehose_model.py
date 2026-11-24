from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKFirehoseModel(BaseModel):
    DeliveryStream: StrictStr | None = None
    Enabled: StrictBool | None = None
