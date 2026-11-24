from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsRedshiftClusterResizeInfo(BaseModel):
    AllowCancelResize: StrictBool | None = None
    ResizeType: StrictStr | None = None
