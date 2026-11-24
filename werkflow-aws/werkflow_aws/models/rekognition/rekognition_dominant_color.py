from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionDominantColor(BaseModel):
    Red: StrictInt | None = None
    Blue: StrictInt | None = None
    Green: StrictInt | None = None
    HexCode: StrictStr | None = None
    CSSColor: StrictStr | None = None
    SimplifiedColor: StrictStr | None = None
    PixelPercent: StrictFloat | StrictInt | None = None
