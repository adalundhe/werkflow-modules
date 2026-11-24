from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSDescribeCapacityProvidersRequest(BaseModel):
    capacityProviders: list[StrictStr] | None = None
    cluster: StrictStr | None = None
    include: list[Literal['TAGS']] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
