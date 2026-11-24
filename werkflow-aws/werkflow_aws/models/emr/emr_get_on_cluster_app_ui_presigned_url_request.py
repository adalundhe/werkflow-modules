from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EMRGetOnClusterAppUIPresignedURLRequest(BaseModel):
    ClusterId: StrictStr
    OnClusterAppUIType: Literal['SparkHistoryServer', 'YarnTimelineService', 'TezUI', 'ApplicationMaster', 'JobHistoryServer', 'ResourceManager'] | None = None
    ApplicationId: StrictStr | None = None
    DryRun: StrictBool | None = None
    ExecutionRoleArn: StrictStr | None = None
