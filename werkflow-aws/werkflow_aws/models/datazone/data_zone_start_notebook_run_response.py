from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_cell_information import DataZoneCellInformation
from .data_zone_compute_config import DataZoneComputeConfig
from .data_zone_environment_config import DataZoneEnvironmentConfig
from .data_zone_network_config import DataZoneNetworkConfig
from .data_zone_notebook_run_error import DataZoneNotebookRunError
from .data_zone_notification_config import DataZoneNotificationConfig
from .data_zone_storage_config import DataZoneStorageConfig
from .data_zone_timeout_config import DataZoneTimeoutConfig
from .data_zone_trigger_source import DataZoneTriggerSource


class DataZoneStartNotebookRunResponse(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    notebookId: StrictStr | None = None
    scheduleId: StrictStr | None = None
    status: StrictStr | None = None
    cellOrder: list[DataZoneCellInformation] | None = None
    metadata: dict[StrictStr, StrictStr] | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    computeConfiguration: DataZoneComputeConfig | None = None
    networkConfiguration: DataZoneNetworkConfig | None = None
    timeoutConfiguration: DataZoneTimeoutConfig | None = None
    environmentConfiguration: DataZoneEnvironmentConfig | None = None
    storageConfiguration: DataZoneStorageConfig | None = None
    notificationConfiguration: DataZoneNotificationConfig | None = None
    triggerSource: DataZoneTriggerSource | None = None
    error: DataZoneNotebookRunError | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    completedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
