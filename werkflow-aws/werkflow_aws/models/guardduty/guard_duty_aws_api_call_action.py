from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_domain_details import GuardDutyDomainDetails
from .guard_duty_remote_account_details import GuardDutyRemoteAccountDetails
from .guard_duty_remote_ip_details import GuardDutyRemoteIpDetails


class GuardDutyAwsApiCallAction(BaseModel):
    Api: StrictStr | None = None
    CallerType: StrictStr | None = None
    DomainDetails: GuardDutyDomainDetails | None = None
    ErrorCode: StrictStr | None = None
    UserAgent: StrictStr | None = None
    RemoteIpDetails: GuardDutyRemoteIpDetails | None = None
    ServiceName: StrictStr | None = None
    RemoteAccountDetails: GuardDutyRemoteAccountDetails | None = None
    AffectedResources: dict[StrictStr, StrictStr] | None = None
