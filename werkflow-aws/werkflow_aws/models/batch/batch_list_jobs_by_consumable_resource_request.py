from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_key_values_pair import BatchKeyValuesPair


class BatchListJobsByConsumableResourceRequest(BaseModel):
    consumableResource: StrictStr
    filters: list[BatchKeyValuesPair] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
