from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueBlueprintRun(BaseModel):
    BlueprintName: StrictStr | None = None
    RunId: StrictStr | None = None
    WorkflowName: StrictStr | None = None
    State: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    RollbackErrorMessage: StrictStr | None = None
    Parameters: StrictStr | None = None
    RoleArn: StrictStr | None = None
