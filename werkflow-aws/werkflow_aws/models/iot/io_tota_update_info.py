from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .io_t_aws_job_executions_rollout_config import IoTAwsJobExecutionsRolloutConfig
from .io_t_aws_job_presigned_url_config import IoTAwsJobPresignedUrlConfig
from .io_t_error_info import IoTErrorInfo
from .io_tota_update_file import IoTOTAUpdateFile


class IoTOTAUpdateInfo(BaseModel):
    otaUpdateId: StrictStr | None = None
    otaUpdateArn: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    targets: list[StrictStr] | None = None
    protocols: list[StrictStr] | None = None
    awsJobExecutionsRolloutConfig: IoTAwsJobExecutionsRolloutConfig | None = None
    awsJobPresignedUrlConfig: IoTAwsJobPresignedUrlConfig | None = None
    targetSelection: StrictStr | None = None
    otaUpdateFiles: list[IoTOTAUpdateFile] | None = None
    otaUpdateStatus: StrictStr | None = None
    awsIotJobId: StrictStr | None = None
    awsIotJobArn: StrictStr | None = None
    errorInfo: IoTErrorInfo | None = None
    additionalParameters: dict[StrictStr, StrictStr] | None = None
