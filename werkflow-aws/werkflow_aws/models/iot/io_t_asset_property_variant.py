from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAssetPropertyVariant(BaseModel):
    stringValue: StrictStr | None = None
    integerValue: StrictStr | None = None
    doubleValue: StrictStr | None = None
    booleanValue: StrictStr | None = None
