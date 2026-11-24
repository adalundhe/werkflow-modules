from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_hub_s3_storage_config import SageMakerHubS3StorageConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateHubRequest(BaseModel):
    HubName: StrictStr
    HubDescription: StrictStr
    HubDisplayName: StrictStr | None = None
    HubSearchKeywords: list[StrictStr] | None = None
    S3StorageConfig: SageMakerHubS3StorageConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
