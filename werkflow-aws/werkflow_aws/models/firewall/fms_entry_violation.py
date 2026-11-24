from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_entry_description import FMSEntryDescription


class FMSEntryViolation(BaseModel):
    ExpectedEntry: FMSEntryDescription | None = None
    ExpectedEvaluationOrder: StrictStr | None = None
    ActualEvaluationOrder: StrictStr | None = None
    EntryAtExpectedEvaluationOrder: FMSEntryDescription | None = None
    EntriesWithConflicts: list[FMSEntryDescription] | None = None
    EntryViolationReasons: list[StrictStr] | None = None
