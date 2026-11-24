from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_data_retention_storage_configuration import BedrockDataRetentionStorageConfiguration


class BedrockGetAccountDataRetentionStorageResponse(BaseModel):
    scope: StrictStr | None = None
    modelProvider: StrictStr | None = None
    storageDestination: StrictStr | None = None
    storageConfiguration: BedrockDataRetentionStorageConfiguration | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    kmsKeyStatus: StrictStr | None = None
    s3BucketStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
