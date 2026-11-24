from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSPodIdentityAssociationSummary(BaseModel):
    clusterName: StrictStr | None = None
    namespace: StrictStr | None = None
    serviceAccount: StrictStr | None = None
    associationArn: StrictStr | None = None
    associationId: StrictStr | None = None
    ownerArn: StrictStr | None = None
