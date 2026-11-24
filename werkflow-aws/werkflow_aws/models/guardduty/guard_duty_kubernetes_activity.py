from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_enrichment import GuardDutyEnrichment
from .guard_duty_investigation_kubernetes_workload import GuardDutyInvestigationKubernetesWorkload
from .guard_duty_kubernetes_anomaly import GuardDutyKubernetesAnomaly
from .guard_duty_kubernetes_api_call import GuardDutyKubernetesApiCall


class GuardDutyKubernetesActivity(BaseModel):
    ApiCall: GuardDutyKubernetesApiCall | None = None
    Anomaly: GuardDutyKubernetesAnomaly | None = None
    Workload: GuardDutyInvestigationKubernetesWorkload | None = None
    Enrichment: GuardDutyEnrichment | None = None
