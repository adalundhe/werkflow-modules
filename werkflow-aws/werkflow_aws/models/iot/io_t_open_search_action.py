from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTOpenSearchAction(BaseModel):
    roleArn: StrictStr | None = None
    endpoint: StrictStr | None = None
    index: StrictStr | None = None
    type: StrictStr | None = None
    id: StrictStr | None = None
