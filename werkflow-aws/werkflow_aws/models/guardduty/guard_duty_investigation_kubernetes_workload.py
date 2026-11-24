from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyInvestigationKubernetesWorkload(BaseModel):
    WorkloadType: StrictStr | None = None
    WorkloadName: StrictStr | None = None
    Containers: StrictStr | None = None
    Volumes: StrictStr | None = None
    SecurityContext: StrictStr | None = None
