from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .iam_delegation_permission import IAMDelegationPermission


class IAMCreateDelegationRequestRequest(BaseModel):
    Description: StrictStr
    Permissions: IAMDelegationPermission
    RequestorWorkflowId: StrictStr
    NotificationChannel: StrictStr
    SessionDuration: StrictInt
    OwnerAccountId: StrictStr | None = None
    RequestMessage: StrictStr | None = None
    RedirectUrl: StrictStr | None = None
    OnlySendByOwner: StrictBool | None = None
