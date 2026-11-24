from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerImportHubContentRequest(BaseModel):
    HubContentName: StrictStr
    HubContentType: Literal['Model', 'Notebook', 'ModelReference', 'DataSet', 'JsonDoc']
    DocumentSchemaVersion: StrictStr
    HubName: StrictStr
    HubContentDocument: StrictStr
    HubContentVersion: StrictStr | None = None
    HubContentDisplayName: StrictStr | None = None
    HubContentDescription: StrictStr | None = None
    HubContentMarkdown: StrictStr | None = None
    SupportStatus: Literal['Supported', 'Deprecated', 'Restricted'] | None = None
    HubContentSearchKeywords: list[StrictStr] | None = None
    Tags: list[SageMakerTagModel] | None = None
