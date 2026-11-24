from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_remote_ip_details import GuardDutyRemoteIpDetails


class GuardDutyKubernetesApiCallAction(BaseModel):
    RequestUri: StrictStr | None = None
    Verb: StrictStr | None = None
    Resource: StrictStr | None = None
    Subresource: StrictStr | None = None
    Namespace: StrictStr | None = None
    ResourceName: StrictStr | None = None
    SourceIps: list[StrictStr] | None = None
    UserAgent: StrictStr | None = None
    RemoteIpDetails: GuardDutyRemoteIpDetails | None = None
    StatusCode: StrictInt | None = None
    Parameters: StrictStr | None = None
