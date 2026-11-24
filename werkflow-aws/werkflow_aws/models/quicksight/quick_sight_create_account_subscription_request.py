from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightCreateAccountSubscriptionRequest(BaseModel):
    AuthenticationMethod: Literal['IAM_AND_QUICKSIGHT', 'IAM_ONLY', 'ACTIVE_DIRECTORY', 'IAM_IDENTITY_CENTER']
    AwsAccountId: StrictStr
    AccountName: StrictStr
    NotificationEmail: StrictStr
    Edition: Literal['STANDARD', 'ENTERPRISE', 'ENTERPRISE_AND_Q'] | None = None
    ActiveDirectoryName: StrictStr | None = None
    Realm: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    AdminGroup: list[StrictStr] | None = None
    AuthorGroup: list[StrictStr] | None = None
    ReaderGroup: list[StrictStr] | None = None
    AdminProGroup: list[StrictStr] | None = None
    AuthorProGroup: list[StrictStr] | None = None
    ReaderProGroup: list[StrictStr] | None = None
    FirstName: StrictStr | None = None
    LastName: StrictStr | None = None
    EmailAddress: StrictStr | None = None
    ContactNumber: StrictStr | None = None
    IAMIdentityCenterInstanceArn: StrictStr | None = None
