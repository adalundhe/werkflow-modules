from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCollectionConfiguration(BaseModel):
    CollectionName: StrictStr | None = None
    CollectionParameters: dict[StrictStr, StrictStr] | None = None
