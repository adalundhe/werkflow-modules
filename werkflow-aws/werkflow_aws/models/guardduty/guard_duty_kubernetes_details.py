from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_kubernetes_user_details import GuardDutyKubernetesUserDetails
from .guard_duty_kubernetes_workload_details import GuardDutyKubernetesWorkloadDetails


class GuardDutyKubernetesDetails(BaseModel):
    KubernetesUserDetails: GuardDutyKubernetesUserDetails | None = None
    KubernetesWorkloadDetails: GuardDutyKubernetesWorkloadDetails | None = None
