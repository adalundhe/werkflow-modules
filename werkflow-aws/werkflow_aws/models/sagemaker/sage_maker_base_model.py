from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBaseModel(BaseModel):
    HubContentName: StrictStr | None = None
    HubContentVersion: StrictStr | None = None
    RecipeName: StrictStr | None = None
