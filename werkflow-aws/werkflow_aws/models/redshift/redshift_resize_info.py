from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftResizeInfo(BaseModel):
    ResizeType: StrictStr | None = None
    AllowCancelResize: StrictBool | None = None
