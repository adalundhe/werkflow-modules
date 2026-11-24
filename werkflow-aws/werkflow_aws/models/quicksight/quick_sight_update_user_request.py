from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightUpdateUserRequest(BaseModel):
    UserName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
    Email: StrictStr
    Role: Literal['ADMIN', 'AUTHOR', 'READER', 'RESTRICTED_AUTHOR', 'RESTRICTED_READER', 'ADMIN_PRO', 'AUTHOR_PRO', 'READER_PRO']
    CustomPermissionsName: StrictStr | None = None
    UnapplyCustomPermissions: StrictBool | None = None
    ExternalLoginFederationProviderType: StrictStr | None = None
    CustomFederationProviderUrl: StrictStr | None = None
    ExternalLoginId: StrictStr | None = None
