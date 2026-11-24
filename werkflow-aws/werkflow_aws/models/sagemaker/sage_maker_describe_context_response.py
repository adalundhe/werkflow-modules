from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_context_source import SageMakerContextSource
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeContextResponse(BaseModel):
    ContextName: StrictStr | None = None
    ContextArn: StrictStr | None = None
    Source: SageMakerContextSource | None = None
    ContextType: StrictStr | None = None
    Description: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    LineageGroupArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
