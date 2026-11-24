from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_tag import QuickSightTag


class QuickSightRegisterUserRequest(BaseModel):
    IdentityType: Literal['IAM', 'QUICKSIGHT', 'IAM_IDENTITY_CENTER']
    Email: StrictStr
    UserRole: Literal['ADMIN', 'AUTHOR', 'READER', 'RESTRICTED_AUTHOR', 'RESTRICTED_READER', 'ADMIN_PRO', 'AUTHOR_PRO', 'READER_PRO']
    AwsAccountId: StrictStr
    Namespace: StrictStr
    IamArn: StrictStr | None = None
    SessionName: StrictStr | None = None
    UserName: StrictStr | None = None
    CustomPermissionsName: StrictStr | None = None
    ExternalLoginFederationProviderType: StrictStr | None = None
    CustomFederationProviderUrl: StrictStr | None = None
    ExternalLoginId: StrictStr | None = None
    Tags: list[QuickSightTag] | None = None
