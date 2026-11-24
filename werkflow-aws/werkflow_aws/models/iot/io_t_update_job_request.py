from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_abort_config import IoTAbortConfig
from .io_t_job_executions_retry_config import IoTJobExecutionsRetryConfig
from .io_t_job_executions_rollout_config import IoTJobExecutionsRolloutConfig
from .io_t_presigned_url_config import IoTPresignedUrlConfig
from .io_t_timeout_config import IoTTimeoutConfig


class IoTUpdateJobRequest(BaseModel):
    jobId: StrictStr
    description: StrictStr | None = None
    presignedUrlConfig: IoTPresignedUrlConfig | None = None
    jobExecutionsRolloutConfig: IoTJobExecutionsRolloutConfig | None = None
    abortConfig: IoTAbortConfig | None = None
    timeoutConfig: IoTTimeoutConfig | None = None
    namespaceId: StrictStr | None = None
    jobExecutionsRetryConfig: IoTJobExecutionsRetryConfig | None = None
