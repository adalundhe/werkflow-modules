from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_abort_config import IoTAbortConfig
from .io_t_job_executions_retry_config import IoTJobExecutionsRetryConfig
from .io_t_job_executions_rollout_config import IoTJobExecutionsRolloutConfig
from .io_t_job_process_details import IoTJobProcessDetails
from .io_t_presigned_url_config import IoTPresignedUrlConfig
from .io_t_scheduled_job_rollout import IoTScheduledJobRollout
from .io_t_scheduling_config import IoTSchedulingConfig
from .io_t_timeout_config import IoTTimeoutConfig


class IoTJob(BaseModel):
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    targetSelection: StrictStr | None = None
    status: StrictStr | None = None
    forceCanceled: StrictBool | None = None
    reasonCode: StrictStr | None = None
    comment: StrictStr | None = None
    targets: list[StrictStr] | None = None
    description: StrictStr | None = None
    presignedUrlConfig: IoTPresignedUrlConfig | None = None
    jobExecutionsRolloutConfig: IoTJobExecutionsRolloutConfig | None = None
    abortConfig: IoTAbortConfig | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    completedAt: datetime.datetime | StrictStr | None = None
    jobProcessDetails: IoTJobProcessDetails | None = None
    timeoutConfig: IoTTimeoutConfig | None = None
    namespaceId: StrictStr | None = None
    jobTemplateArn: StrictStr | None = None
    jobExecutionsRetryConfig: IoTJobExecutionsRetryConfig | None = None
    documentParameters: dict[StrictStr, StrictStr] | None = None
    isConcurrent: StrictBool | None = None
    schedulingConfig: IoTSchedulingConfig | None = None
    scheduledJobRollouts: list[IoTScheduledJobRollout] | None = None
    destinationPackageVersions: list[StrictStr] | None = None
