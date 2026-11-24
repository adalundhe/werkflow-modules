from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListDaemonsRequest(BaseModel):
    clusterArn: StrictStr | None = None
    capacityProviderArns: list[StrictStr] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
