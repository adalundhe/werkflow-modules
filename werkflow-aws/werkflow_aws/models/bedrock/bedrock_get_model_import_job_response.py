from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_model_data_source import BedrockModelDataSource
from .bedrock_vpc_config import BedrockVpcConfig


class BedrockGetModelImportJobResponse(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    importedModelName: StrictStr | None = None
    importedModelArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    modelDataSource: BedrockModelDataSource | None = None
    status: StrictStr | None = None
    failureMessage: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    vpcConfig: BedrockVpcConfig | None = None
    importedModelKmsKeyArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
