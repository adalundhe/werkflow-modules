from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .bedrock_custom_model_units import BedrockCustomModelUnits
from .bedrock_model_data_source import BedrockModelDataSource


class BedrockGetImportedModelResponse(BaseModel):
    modelArn: StrictStr | None = None
    modelName: StrictStr | None = None
    jobName: StrictStr | None = None
    jobArn: StrictStr | None = None
    modelDataSource: BedrockModelDataSource | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    modelArchitecture: StrictStr | None = None
    modelKmsKeyArn: StrictStr | None = None
    instructSupported: StrictBool | None = None
    customModelUnits: BedrockCustomModelUnits | None = None
    ResponseMetadata: dict[str, Any] | None = None
