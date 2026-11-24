from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_validation_failure import OpenSearchValidationFailure


class OpenSearchDryRunProgressStatus(BaseModel):
    DryRunId: StrictStr | None = None
    DryRunStatus: StrictStr | None = None
    CreationDate: StrictStr | None = None
    UpdateDate: StrictStr | None = None
    ValidationFailures: list[OpenSearchValidationFailure] | None = None
    AcceptedWarnings: list[StrictStr] | None = None
