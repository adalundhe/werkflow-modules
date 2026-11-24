from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSUpdateAccessEntryRequest(BaseModel):
    clusterName: StrictStr
    principalArn: StrictStr
    kubernetesGroups: list[StrictStr] | None = None
    clientRequestToken: StrictStr | None = None
    username: StrictStr | None = None
