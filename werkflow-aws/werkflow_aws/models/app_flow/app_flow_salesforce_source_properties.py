from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowSalesforceSourceProperties(BaseModel):
    object: StrictStr | None = None
    enableDynamicFieldUpdate: StrictBool | None = None
    includeDeletedRecords: StrictBool | None = None
    dataTransferApi: StrictStr | None = None
