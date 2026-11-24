from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .bedrock_data_retention_storage_configuration import BedrockDataRetentionStorageConfiguration


class BedrockPutProjectDataRetentionStorageRequest(BaseModel):
    projectIdentifier: StrictStr
    modelProvider: Literal['anthropic', 'openai']
    storageDestination: Literal['customer_managed', 'amazon_managed']
    storageConfiguration: BedrockDataRetentionStorageConfiguration | None = None
