from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchGetIterableFormsRequest(BaseModel):
    AssetIdentifier: StrictStr
    IterableFormName: StrictStr
    ItemIdentifiers: list[StrictStr]
