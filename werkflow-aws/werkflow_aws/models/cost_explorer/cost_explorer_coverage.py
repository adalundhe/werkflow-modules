from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_coverage_cost import CostExplorerCoverageCost
from .cost_explorer_coverage_hours import CostExplorerCoverageHours
from .cost_explorer_coverage_normalized_units import CostExplorerCoverageNormalizedUnits


class CostExplorerCoverage(BaseModel):
    CoverageHours: CostExplorerCoverageHours | None = None
    CoverageNormalizedUnits: CostExplorerCoverageNormalizedUnits | None = None
    CoverageCost: CostExplorerCoverageCost | None = None
