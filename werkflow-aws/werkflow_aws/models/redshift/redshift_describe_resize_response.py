from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RedshiftDescribeResizeResponse(BaseModel):
    TargetNodeType: StrictStr | None = None
    TargetNumberOfNodes: StrictInt | None = None
    TargetClusterType: StrictStr | None = None
    Status: StrictStr | None = None
    ImportTablesCompleted: list[StrictStr] | None = None
    ImportTablesInProgress: list[StrictStr] | None = None
    ImportTablesNotStarted: list[StrictStr] | None = None
    AvgResizeRateInMegaBytesPerSecond: StrictFloat | StrictInt | None = None
    TotalResizeDataInMegaBytes: StrictInt | None = None
    ProgressInMegaBytes: StrictInt | None = None
    ElapsedTimeInSeconds: StrictInt | None = None
    EstimatedTimeToCompletionInSeconds: StrictInt | None = None
    ResizeType: StrictStr | None = None
    Message: StrictStr | None = None
    TargetEncryptionType: StrictStr | None = None
    DataTransferProgressPercent: StrictFloat | StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
