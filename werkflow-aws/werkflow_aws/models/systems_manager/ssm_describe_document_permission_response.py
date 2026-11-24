from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_account_sharing_info import SSMAccountSharingInfo


class SSMDescribeDocumentPermissionResponse(BaseModel):
    AccountIds: list[StrictStr] | None = None
    AccountSharingInfoList: list[SSMAccountSharingInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
