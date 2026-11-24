from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSCreateAccessEntryRequest(BaseModel):
    clusterName: StrictStr
    principalArn: StrictStr
    kubernetesGroups: list[StrictStr] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    clientRequestToken: StrictStr | None = None
    username: StrictStr | None = None
    type: StrictStr | None = None
