from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_abort_config import IoTAbortConfig
from .io_t_job_executions_retry_config import IoTJobExecutionsRetryConfig
from .io_t_job_executions_rollout_config import IoTJobExecutionsRolloutConfig
from .io_t_presigned_url_config import IoTPresignedUrlConfig
from .io_t_scheduling_config import IoTSchedulingConfig
from .io_t_tag import IoTTag
from .io_t_timeout_config import IoTTimeoutConfig


class IoTCreateJobRequest(BaseModel):
    jobId: StrictStr
    targets: list[StrictStr]
    documentSource: StrictStr | None = None
    document: StrictStr | None = None
    description: StrictStr | None = None
    presignedUrlConfig: IoTPresignedUrlConfig | None = None
    targetSelection: Literal['CONTINUOUS', 'SNAPSHOT'] | None = None
    jobExecutionsRolloutConfig: IoTJobExecutionsRolloutConfig | None = None
    abortConfig: IoTAbortConfig | None = None
    timeoutConfig: IoTTimeoutConfig | None = None
    tags: list[IoTTag] | None = None
    namespaceId: StrictStr | None = None
    jobTemplateArn: StrictStr | None = None
    jobExecutionsRetryConfig: IoTJobExecutionsRetryConfig | None = None
    documentParameters: dict[StrictStr, StrictStr] | None = None
    schedulingConfig: IoTSchedulingConfig | None = None
    destinationPackageVersions: list[StrictStr] | None = None
