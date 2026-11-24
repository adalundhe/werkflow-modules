from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .bedrock_data_retention_storage_configuration import BedrockDataRetentionStorageConfiguration


class BedrockPutOrganizationDataRetentionStorageRequest(BaseModel):
    modelProvider: Literal['anthropic', 'openai']
    storageDestination: Literal['customer_managed', 'amazon_managed']
    storageConfiguration: BedrockDataRetentionStorageConfiguration | None = None
