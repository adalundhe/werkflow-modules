from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerDeleteHubContentReferenceRequest(BaseModel):
    HubName: StrictStr
    HubContentType: Literal['Model', 'Notebook', 'ModelReference', 'DataSet', 'JsonDoc']
    HubContentName: StrictStr
