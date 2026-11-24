from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_expression import CostExplorerExpression


class CostExplorerAnomalyMonitor(BaseModel):
    MonitorArn: StrictStr | None = None
    MonitorName: StrictStr | None = None
    CreationDate: StrictStr | None = None
    LastUpdatedDate: StrictStr | None = None
    LastEvaluatedDate: StrictStr | None = None
    MonitorType: StrictStr | None = None
    MonitorDimension: StrictStr | None = None
    MonitorSpecification: CostExplorerExpression | None = None
    DimensionalValueCount: StrictInt | None = None
