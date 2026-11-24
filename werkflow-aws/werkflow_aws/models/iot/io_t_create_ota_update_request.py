from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_aws_job_abort_config import IoTAwsJobAbortConfig
from .io_t_aws_job_executions_rollout_config import IoTAwsJobExecutionsRolloutConfig
from .io_t_aws_job_presigned_url_config import IoTAwsJobPresignedUrlConfig
from .io_t_aws_job_timeout_config import IoTAwsJobTimeoutConfig
from .io_tota_update_file import IoTOTAUpdateFile
from .io_t_tag import IoTTag


class IoTCreateOTAUpdateRequest(BaseModel):
    otaUpdateId: StrictStr
    targets: list[StrictStr]
    files: list[IoTOTAUpdateFile]
    roleArn: StrictStr
    description: StrictStr | None = None
    protocols: list[Literal['MQTT', 'HTTP']] | None = None
    targetSelection: Literal['CONTINUOUS', 'SNAPSHOT'] | None = None
    awsJobExecutionsRolloutConfig: IoTAwsJobExecutionsRolloutConfig | None = None
    awsJobPresignedUrlConfig: IoTAwsJobPresignedUrlConfig | None = None
    awsJobAbortConfig: IoTAwsJobAbortConfig | None = None
    awsJobTimeoutConfig: IoTAwsJobTimeoutConfig | None = None
    additionalParameters: dict[StrictStr, StrictStr] | None = None
    tags: list[IoTTag] | None = None
