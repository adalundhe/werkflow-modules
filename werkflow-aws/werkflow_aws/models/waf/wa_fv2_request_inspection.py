from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_password_field import WAFv2PasswordField
from .wa_fv2_username_field import WAFv2UsernameField


class WAFv2RequestInspection(BaseModel):
    PayloadType: StrictStr | None = None
    UsernameField: WAFv2UsernameField | None = None
    PasswordField: WAFv2PasswordField | None = None
