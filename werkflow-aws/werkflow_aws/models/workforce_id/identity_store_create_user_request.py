from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .identity_store_address import IdentityStoreAddress
from .identity_store_attribute_value import IdentityStoreAttributeValue
from .identity_store_email import IdentityStoreEmail
from .identity_store_name import IdentityStoreName
from .identity_store_phone_number import IdentityStorePhoneNumber
from .identity_store_photo import IdentityStorePhoto
from .identity_store_role import IdentityStoreRole


class IdentityStoreCreateUserRequest(BaseModel):
    IdentityStoreId: StrictStr
    UserName: StrictStr | None = None
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
    Photos: list[IdentityStorePhoto] | None = None
    Website: StrictStr | None = None
    Birthdate: StrictStr | None = None
    Roles: list[IdentityStoreRole] | None = None
    Extensions: dict[StrictStr, IdentityStoreAttributeValue] | None = None
