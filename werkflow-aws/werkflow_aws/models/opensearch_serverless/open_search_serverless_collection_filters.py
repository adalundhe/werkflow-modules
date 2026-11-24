from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCollectionFilters(BaseModel):
    name: StrictStr | None = None
    status: Literal['CREATING', 'UPDATING', 'DELETING', 'ACTIVE', 'FAILED', 'UPDATE_FAILED'] | None = None
    collectionGroupName: StrictStr | None = None
