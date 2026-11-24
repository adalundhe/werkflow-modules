from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_compute_config import DataZoneComputeConfig
from .data_zone_network_config import DataZoneNetworkConfig
from .data_zone_notification_config import DataZoneNotificationConfig
from .data_zone_timeout_config import DataZoneTimeoutConfig
from .data_zone_trigger_source import DataZoneTriggerSource


class DataZoneStartNotebookRunRequest(BaseModel):
    domainIdentifier: StrictStr
    owningProjectIdentifier: StrictStr
    notebookIdentifier: StrictStr
    scheduleIdentifier: StrictStr | None = None
    computeConfiguration: DataZoneComputeConfig | None = None
    networkConfiguration: DataZoneNetworkConfig | None = None
    timeoutConfiguration: DataZoneTimeoutConfig | None = None
    notificationConfiguration: DataZoneNotificationConfig | None = None
    triggerSource: DataZoneTriggerSource | None = None
    metadata: dict[StrictStr, StrictStr] | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    clientToken: StrictStr | None = None
