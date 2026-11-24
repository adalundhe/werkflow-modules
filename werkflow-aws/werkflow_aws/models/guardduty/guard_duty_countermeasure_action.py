from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_affected_resource import GuardDutyAffectedResource


class GuardDutyCountermeasureAction(BaseModel):
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Priority: StrictStr | None = None
    DefenseTechnique: StrictStr | None = None
    Mitigates: list[StrictStr] | None = None
    CliCommands: list[StrictStr] | None = None
    DispositionId: StrictInt | None = None
    Disposition: StrictStr | None = None
    AffectedResources: list[GuardDutyAffectedResource] | None = None
