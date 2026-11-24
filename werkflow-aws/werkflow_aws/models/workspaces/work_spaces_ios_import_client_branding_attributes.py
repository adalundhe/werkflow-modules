from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class WorkSpacesIosImportClientBrandingAttributes(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Logo: StrictBytes | BinaryIO | StrictStr | None = None
    Logo2x: StrictBytes | BinaryIO | StrictStr | None = None
    Logo3x: StrictBytes | BinaryIO | StrictStr | None = None
    SupportEmail: StrictStr | None = None
    SupportLink: StrictStr | None = None
    ForgotPasswordLink: StrictStr | None = None
    LoginMessage: dict[StrictStr, StrictStr] | None = None
