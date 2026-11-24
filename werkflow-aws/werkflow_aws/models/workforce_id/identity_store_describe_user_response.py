from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .identity_store_address import IdentityStoreAddress
from .identity_store_attribute_value import IdentityStoreAttributeValue
from .identity_store_email import IdentityStoreEmail
from .identity_store_external_id import IdentityStoreExternalId
from .identity_store_name import IdentityStoreName
from .identity_store_phone_number import IdentityStorePhoneNumber
from .identity_store_photo import IdentityStorePhoto
from .identity_store_role import IdentityStoreRole


class IdentityStoreDescribeUserResponse(BaseModel):
    IdentityStoreId: StrictStr | None = None
    UserId: StrictStr | None = None
    UserArn: StrictStr | None = None
    Revision: StrictStr | None = None
    UserName: StrictStr | None = None
    ExternalIds: list[IdentityStoreExternalId] | None = None
    Name: IdentityStoreName | None = None
    DisplayName: StrictStr | None = None
    NickName: StrictStr | None = None
    ProfileUrl: StrictStr | None = None
    Emails: list[IdentityStoreEmail] | None = None
    Addresses: list[IdentityStoreAddress] | None = None
    PhoneNumbers: list[IdentityStorePhoneNumber] | None = None
    UserType: StrictStr | None = None
    Title: StrictStr | None = None
    PreferredLanguage: StrictStr | None = None
    Locale: StrictStr | None = None
    Timezone: StrictStr | None = None
    UserStatus: StrictStr | None = None
    Photos: list[IdentityStorePhoto] | None = None
    Website: StrictStr | None = None
    Birthdate: StrictStr | None = None
    Roles: list[IdentityStoreRole] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    UpdatedBy: StrictStr | None = None
    Extensions: dict[StrictStr, IdentityStoreAttributeValue] | None = None
    ResponseMetadata: dict[str, Any] | None = None
