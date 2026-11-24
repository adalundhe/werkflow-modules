from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_dns_context import GuardDutyDnsContext
from .guard_duty_enrichment import GuardDutyEnrichment
from .guard_duty_network_anomaly import GuardDutyNetworkAnomaly
from .guard_duty_network_counts import GuardDutyNetworkCounts
from .guard_duty_network_ports import GuardDutyNetworkPorts
from .guard_duty_network_traffic import GuardDutyNetworkTraffic


class GuardDutyNetworkActivity(BaseModel):
    Protocol: StrictStr | None = None
    Direction: StrictStr | None = None
    Method: StrictStr | None = None
    Blocked: StrictStr | None = None
    Platform: StrictStr | None = None
    Ports: GuardDutyNetworkPorts | None = None
    Traffic: GuardDutyNetworkTraffic | None = None
    Anomaly: GuardDutyNetworkAnomaly | None = None
    Dns: GuardDutyDnsContext | None = None
    Counts: GuardDutyNetworkCounts | None = None
    Enrichment: GuardDutyEnrichment | None = None
