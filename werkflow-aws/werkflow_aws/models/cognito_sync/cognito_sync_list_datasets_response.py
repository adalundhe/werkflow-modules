from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .cognito_sync_dataset import CognitoSyncDataset


class CognitoSyncListDatasetsResponse(BaseModel):
    Datasets: list[CognitoSyncDataset] | None = None
    Count: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
