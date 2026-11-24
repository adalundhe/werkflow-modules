from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDescribeAttachedFilesConfigurationRequest(BaseModel):
    InstanceId: StrictStr
    AttachmentScope: Literal['EMAIL', 'CHAT', 'CASE', 'TASK']
