from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_archive_distribution import GuardDutyArchiveDistribution
from .guard_duty_finding_type_count import GuardDutyFindingTypeCount
from .guard_duty_resource_distribution import GuardDutyResourceDistribution
from .guard_duty_severity_breakdown import GuardDutySeverityBreakdown
from .guard_duty_tactic_coverage import GuardDutyTacticCoverage
from .guard_duty_type_distribution import GuardDutyTypeDistribution


class GuardDutyDistribution(BaseModel):
    Dimension: StrictStr | None = None
    TotalFindings: StrictInt | None = None
    SeverityBreakdown: GuardDutySeverityBreakdown | None = None
    FindingTypes: list[GuardDutyTypeDistribution] | None = None
    TopFindingTypes: list[GuardDutyFindingTypeCount] | None = None
    Resources: list[GuardDutyResourceDistribution] | None = None
    AttackVectors: list[GuardDutyTacticCoverage] | None = None
    Archive: GuardDutyArchiveDistribution | None = None
