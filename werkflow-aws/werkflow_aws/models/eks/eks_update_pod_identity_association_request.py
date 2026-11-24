from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSUpdatePodIdentityAssociationRequest(BaseModel):
    clusterName: StrictStr
    associationId: StrictStr
    roleArn: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
    disableSessionTags: StrictBool | None = None
    targetRoleArn: StrictStr | None = None
    policy: StrictStr | None = None
