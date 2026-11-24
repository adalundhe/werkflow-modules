from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_change_progress_stage import OpenSearchChangeProgressStage
from .open_search_cloned_blue_green_upgrade_details import OpenSearchClonedBlueGreenUpgradeDetails
from .open_search_validation_failure import OpenSearchValidationFailure


class OpenSearchChangeProgressStatusDetails(BaseModel):
    ChangeId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    PendingProperties: list[StrictStr] | None = None
    CompletedProperties: list[StrictStr] | None = None
    TotalNumberOfStages: StrictInt | None = None
    ChangeProgressStages: list[OpenSearchChangeProgressStage] | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    ConfigChangeStatus: StrictStr | None = None
    InitiatedBy: StrictStr | None = None
    ClonedBlueGreenUpgradeDetails: OpenSearchClonedBlueGreenUpgradeDetails | None = None
    ValidationFailures: list[OpenSearchValidationFailure] | None = None
    AcceptedWarnings: list[StrictStr] | None = None
