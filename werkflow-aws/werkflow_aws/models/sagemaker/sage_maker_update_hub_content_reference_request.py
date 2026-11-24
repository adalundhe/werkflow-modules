from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerUpdateHubContentReferenceRequest(BaseModel):
    HubName: StrictStr
    HubContentName: StrictStr
    HubContentType: Literal['Model', 'Notebook', 'ModelReference', 'DataSet', 'JsonDoc']
    MinVersion: StrictStr | None = None
