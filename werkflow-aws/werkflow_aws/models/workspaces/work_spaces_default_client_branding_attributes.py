from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDefaultClientBrandingAttributes(BaseModel):
    LogoUrl: StrictStr | None = None
    SupportEmail: StrictStr | None = None
    SupportLink: StrictStr | None = None
    ForgotPasswordLink: StrictStr | None = None
    LoginMessage: dict[StrictStr, StrictStr] | None = None
