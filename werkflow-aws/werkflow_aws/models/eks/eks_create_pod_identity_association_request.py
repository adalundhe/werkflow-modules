from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSCreatePodIdentityAssociationRequest(BaseModel):
    clusterName: StrictStr
    namespace: StrictStr
    serviceAccount: StrictStr
    roleArn: StrictStr
    clientRequestToken: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    disableSessionTags: StrictBool | None = None
    targetRoleArn: StrictStr | None = None
    policy: StrictStr | None = None
