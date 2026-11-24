from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSListPodIdentityAssociationsRequest(BaseModel):
    clusterName: StrictStr
    namespace: StrictStr | None = None
    serviceAccount: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
