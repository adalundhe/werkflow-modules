from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AppFlowConnectorDetail(BaseModel):
    connectorDescription: StrictStr | None = None
    connectorName: StrictStr | None = None
    connectorOwner: StrictStr | None = None
    connectorVersion: StrictStr | None = None
    applicationType: StrictStr | None = None
    connectorType: StrictStr | None = None
    connectorLabel: StrictStr | None = None
    registeredAt: datetime.datetime | StrictStr | None = None
    registeredBy: StrictStr | None = None
    connectorProvisioningType: StrictStr | None = None
    connectorModes: list[StrictStr] | None = None
    supportedDataTransferTypes: list[StrictStr] | None = None
