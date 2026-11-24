from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cognito_sync_record import CognitoSyncRecord


class CognitoSyncListRecordsResponse(BaseModel):
    Records: list[CognitoSyncRecord] | None = None
    NextToken: StrictStr | None = None
    Count: StrictInt | None = None
    DatasetSyncCount: StrictInt | None = None
    LastModifiedBy: StrictStr | None = None
    MergedDatasetNames: list[StrictStr] | None = None
    DatasetExists: StrictBool | None = None
    DatasetDeletedAfterRequestedSyncCount: StrictBool | None = None
    SyncSessionToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
