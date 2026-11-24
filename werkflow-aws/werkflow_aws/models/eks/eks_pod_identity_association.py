from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class EKSPodIdentityAssociation(BaseModel):
    clusterName: StrictStr | None = None
    namespace: StrictStr | None = None
    serviceAccount: StrictStr | None = None
    roleArn: StrictStr | None = None
    associationArn: StrictStr | None = None
    associationId: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    modifiedAt: datetime.datetime | StrictStr | None = None
    ownerArn: StrictStr | None = None
    disableSessionTags: StrictBool | None = None
    targetRoleArn: StrictStr | None = None
    externalId: StrictStr | None = None
    policy: StrictStr | None = None
