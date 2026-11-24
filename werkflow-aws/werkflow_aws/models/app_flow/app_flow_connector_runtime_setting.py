from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowConnectorRuntimeSetting(BaseModel):
    key: StrictStr | None = None
    dataType: StrictStr | None = None
    isRequired: StrictBool | None = None
    label: StrictStr | None = None
    description: StrictStr | None = None
    scope: StrictStr | None = None
    connectorSuppliedValueOptions: list[StrictStr] | None = None
