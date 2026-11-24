from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class TransferDescribedWebAppCustomization(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Arn: StrictStr | None = None
    WebAppId: StrictStr | None = None
    Title: StrictStr | None = None
    LogoFile: StrictBytes | Any | None = None
    FaviconFile: StrictBytes | Any | None = None
