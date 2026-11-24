from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_sync_dataset import CognitoSyncDataset


class CognitoSyncDeleteDatasetResponse(BaseModel):
    Dataset: CognitoSyncDataset | None = None
    ResponseMetadata: dict[str, Any] | None = None
