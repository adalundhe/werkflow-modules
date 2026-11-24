from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .comprehend_data_security_config import ComprehendDataSecurityConfig
from .comprehend_tag import ComprehendTag
from .comprehend_task_config import ComprehendTaskConfig


class ComprehendCreateFlywheelRequest(BaseModel):
    FlywheelName: StrictStr
    DataAccessRoleArn: StrictStr
    DataLakeS3Uri: StrictStr
    ActiveModelArn: StrictStr | None = None
    TaskConfig: ComprehendTaskConfig | None = None
    ModelType: Literal['DOCUMENT_CLASSIFIER', 'ENTITY_RECOGNIZER'] | None = None
    DataSecurityConfig: ComprehendDataSecurityConfig | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
