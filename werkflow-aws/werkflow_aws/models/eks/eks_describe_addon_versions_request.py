from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSDescribeAddonVersionsRequest(BaseModel):
    kubernetesVersion: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    addonName: StrictStr | None = None
    types: list[StrictStr] | None = None
    publishers: list[StrictStr] | None = None
    owners: list[StrictStr] | None = None
