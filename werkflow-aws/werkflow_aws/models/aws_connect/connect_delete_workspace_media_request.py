from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDeleteWorkspaceMediaRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    MediaType: Literal['IMAGE_LOGO_LIGHT_FAVICON', 'IMAGE_LOGO_DARK_FAVICON', 'IMAGE_LOGO_LIGHT_HORIZONTAL', 'IMAGE_LOGO_DARK_HORIZONTAL']
