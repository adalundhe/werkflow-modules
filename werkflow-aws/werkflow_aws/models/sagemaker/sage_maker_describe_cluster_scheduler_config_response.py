from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_scheduler_config import SageMakerSchedulerConfig
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeClusterSchedulerConfigResponse(BaseModel):
    ClusterSchedulerConfigArn: StrictStr | None = None
    ClusterSchedulerConfigId: StrictStr | None = None
    Name: StrictStr | None = None
    ClusterSchedulerConfigVersion: StrictInt | None = None
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
    StatusDetails: dict[StrictStr, StrictStr] | None = None
    ClusterArn: StrictStr | None = None
    SchedulerConfig: SageMakerSchedulerConfig | None = None
    Description: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
