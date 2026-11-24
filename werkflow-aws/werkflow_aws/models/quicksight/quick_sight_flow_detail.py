from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_sensitive_document import QuickSightSensitiveDocument
from .quick_sight_step_alias_mapping import QuickSightStepAliasMapping


class QuickSightFlowDetail(BaseModel):
    Arn: StrictStr | None = None
    FlowId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    PublishState: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
    FlowDefinition: QuickSightSensitiveDocument | None = None
    StepAliases: list[QuickSightStepAliasMapping] | None = None
