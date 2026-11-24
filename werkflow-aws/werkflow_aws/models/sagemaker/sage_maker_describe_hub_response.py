from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_hub_s3_storage_config import SageMakerHubS3StorageConfig
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeHubResponse(BaseModel):
    HubName: StrictStr | None = None
    HubArn: StrictStr | None = None
    HubDisplayName: StrictStr | None = None
    HubDescription: StrictStr | None = None
    HubSearchKeywords: list[StrictStr] | None = None
    S3StorageConfig: SageMakerHubS3StorageConfig | None = None
    HubStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
