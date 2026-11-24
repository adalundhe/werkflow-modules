from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_abort_config import IoTAbortConfig
from .io_t_job_executions_retry_config import IoTJobExecutionsRetryConfig
from .io_t_job_executions_rollout_config import IoTJobExecutionsRolloutConfig
from .io_t_maintenance_window import IoTMaintenanceWindow
from .io_t_presigned_url_config import IoTPresignedUrlConfig
from .io_t_tag import IoTTag
from .io_t_timeout_config import IoTTimeoutConfig


class IoTCreateJobTemplateRequest(BaseModel):
    jobTemplateId: StrictStr
    description: StrictStr
    jobArn: StrictStr | None = None
    documentSource: StrictStr | None = None
    document: StrictStr | None = None
    presignedUrlConfig: IoTPresignedUrlConfig | None = None
    jobExecutionsRolloutConfig: IoTJobExecutionsRolloutConfig | None = None
    abortConfig: IoTAbortConfig | None = None
    timeoutConfig: IoTTimeoutConfig | None = None
    tags: list[IoTTag] | None = None
    jobExecutionsRetryConfig: IoTJobExecutionsRetryConfig | None = None
    maintenanceWindows: list[IoTMaintenanceWindow] | None = None
    destinationPackageVersions: list[StrictStr] | None = None
