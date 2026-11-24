from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .iam_delegation_permission import IAMDelegationPermission


class IAMDelegationRequest(BaseModel):
    DelegationRequestId: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    Description: StrictStr | None = None
    RequestMessage: StrictStr | None = None
    Permissions: IAMDelegationPermission | None = None
    PermissionPolicy: StrictStr | None = None
    RolePermissionRestrictionArns: list[StrictStr] | None = None
    OwnerId: StrictStr | None = None
    ApproverId: StrictStr | None = None
    State: StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    RequestorId: StrictStr | None = None
    RequestorName: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    SessionDuration: StrictInt | None = None
    RedirectUrl: StrictStr | None = None
    Notes: StrictStr | None = None
    RejectionReason: StrictStr | None = None
    OnlySendByOwner: StrictBool | None = None
    UpdatedTime: datetime.datetime | StrictStr | None = None
