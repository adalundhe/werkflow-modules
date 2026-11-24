from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPaletteCanvas(BaseModel):
    ContainerBackground: StrictStr | None = None
    PageBackground: StrictStr | None = None
    ActiveBackground: StrictStr | None = None
