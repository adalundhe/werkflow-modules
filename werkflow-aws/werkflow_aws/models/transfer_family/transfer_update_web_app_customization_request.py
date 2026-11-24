from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class TransferUpdateWebAppCustomizationRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    WebAppId: StrictStr
    Title: StrictStr | None = None
    LogoFile: StrictBytes | BinaryIO | StrictStr | None = None
    FaviconFile: StrictBytes | BinaryIO | StrictStr | None = None
