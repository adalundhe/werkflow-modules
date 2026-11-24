from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_data_transfer_api import AppFlowDataTransferApi


class AppFlowCustomConnectorSourceProperties(BaseModel):
    entityName: StrictStr | None = None
    customProperties: dict[StrictStr, StrictStr] | None = None
    dataTransferApi: AppFlowDataTransferApi | None = None
