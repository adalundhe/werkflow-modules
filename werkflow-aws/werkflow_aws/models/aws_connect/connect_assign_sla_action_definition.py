from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_case_sla_configuration import ConnectCaseSlaConfiguration


class ConnectAssignSlaActionDefinition(BaseModel):
    SlaAssignmentType: StrictStr | None = None
    CaseSlaConfiguration: ConnectCaseSlaConfiguration | None = None
