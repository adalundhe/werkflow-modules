from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowConnectorEntity(BaseModel):
    name: StrictStr | None = None
    label: StrictStr | None = None
    hasNestedEntities: StrictBool | None = None
