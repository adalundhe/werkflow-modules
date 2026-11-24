from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .comprehend_data_security_config import ComprehendDataSecurityConfig
from .comprehend_task_config import ComprehendTaskConfig


class ComprehendFlywheelProperties(BaseModel):
    FlywheelArn: StrictStr | None = None
    ActiveModelArn: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    TaskConfig: ComprehendTaskConfig | None = None
    DataLakeS3Uri: StrictStr | None = None
    DataSecurityConfig: ComprehendDataSecurityConfig | None = None
    Status: StrictStr | None = None
    ModelType: StrictStr | None = None
    Message: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LatestFlywheelIteration: StrictStr | None = None
