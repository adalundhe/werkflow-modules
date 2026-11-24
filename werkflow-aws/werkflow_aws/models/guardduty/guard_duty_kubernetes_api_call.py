from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyKubernetesApiCall(BaseModel):
    ClusterName: StrictStr | None = None
    Username: StrictStr | None = None
    UserGroups: StrictStr | None = None
    UserId: StrictStr | None = None
    Verb: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceName: StrictStr | None = None
    Namespace: StrictStr | None = None
    RequestUri: StrictStr | None = None
    StatusCode: StrictInt | None = None
    SourceIps: StrictStr | None = None
    UserAgent: StrictStr | None = None
    EventCount: StrictInt | None = None
