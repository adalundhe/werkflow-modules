from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_address_field import WAFv2AddressField
from .wa_fv2_email_field import WAFv2EmailField
from .wa_fv2_password_field import WAFv2PasswordField
from .wa_fv2_phone_number_field import WAFv2PhoneNumberField
from .wa_fv2_username_field import WAFv2UsernameField


class WAFv2RequestInspectionACFP(BaseModel):
    PayloadType: StrictStr | None = None
    UsernameField: WAFv2UsernameField | None = None
    PasswordField: WAFv2PasswordField | None = None
    EmailField: WAFv2EmailField | None = None
    PhoneNumberFields: list[WAFv2PhoneNumberField] | None = None
    AddressFields: list[WAFv2AddressField] | None = None
