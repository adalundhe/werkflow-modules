from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectImagesLogo(BaseModel):
    Default: StrictStr | None = None
    Favicon: StrictStr | None = None
