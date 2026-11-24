from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesIosClientBrandingAttributes(BaseModel):
    LogoUrl: StrictStr | None = None
    Logo2xUrl: StrictStr | None = None
    Logo3xUrl: StrictStr | None = None
    SupportEmail: StrictStr | None = None
    SupportLink: StrictStr | None = None
    ForgotPasswordLink: StrictStr | None = None
    LoginMessage: dict[StrictStr, StrictStr] | None = None
