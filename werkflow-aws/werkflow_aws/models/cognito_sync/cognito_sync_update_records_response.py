from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_sync_record import CognitoSyncRecord


class CognitoSyncUpdateRecordsResponse(BaseModel):
    Records: list[CognitoSyncRecord] | None = None
    ResponseMetadata: dict[str, Any] | None = None
