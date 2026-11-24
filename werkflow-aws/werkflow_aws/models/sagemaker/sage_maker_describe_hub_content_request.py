from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerDescribeHubContentRequest(BaseModel):
    HubName: StrictStr
    HubContentType: Literal['Model', 'Notebook', 'ModelReference', 'DataSet', 'JsonDoc']
    HubContentName: StrictStr
    HubContentVersion: StrictStr | None = None
