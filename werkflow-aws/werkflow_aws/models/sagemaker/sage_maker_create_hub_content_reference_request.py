from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateHubContentReferenceRequest(BaseModel):
    HubName: StrictStr
    SageMakerPublicHubContentArn: StrictStr
    HubContentName: StrictStr | None = None
    MinVersion: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
