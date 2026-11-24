from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyKubernetesWorkload(BaseModel):
    ContainerUids: list[StrictStr] | None = None
    Namespace: StrictStr | None = None
    KubernetesResourcesTypes: StrictStr | None = None
