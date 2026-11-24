from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowAuthParameter(BaseModel):
    key: StrictStr | None = None
    isRequired: StrictBool | None = None
    label: StrictStr | None = None
    description: StrictStr | None = None
    isSensitiveField: StrictBool | None = None
    connectorSuppliedValues: list[StrictStr] | None = None
