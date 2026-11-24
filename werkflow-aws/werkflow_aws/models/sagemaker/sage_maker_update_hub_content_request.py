from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerUpdateHubContentRequest(BaseModel):
    HubName: StrictStr
    HubContentName: StrictStr
    HubContentType: Literal['Model', 'Notebook', 'ModelReference', 'DataSet', 'JsonDoc']
    HubContentVersion: StrictStr
    HubContentDisplayName: StrictStr | None = None
    HubContentDescription: StrictStr | None = None
    HubContentMarkdown: StrictStr | None = None
    HubContentSearchKeywords: list[StrictStr] | None = None
    SupportStatus: Literal['Supported', 'Deprecated', 'Restricted'] | None = None
