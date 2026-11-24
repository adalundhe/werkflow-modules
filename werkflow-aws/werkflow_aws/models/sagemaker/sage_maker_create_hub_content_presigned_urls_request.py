from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_presigned_url_access_config import SageMakerPresignedUrlAccessConfig


class SageMakerCreateHubContentPresignedUrlsRequest(BaseModel):
    HubName: StrictStr
    HubContentType: Literal['Model', 'Notebook', 'ModelReference', 'DataSet', 'JsonDoc']
    HubContentName: StrictStr
    HubContentVersion: StrictStr | None = None
    AccessConfig: SageMakerPresignedUrlAccessConfig | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
