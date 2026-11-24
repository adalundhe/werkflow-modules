from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RedshiftNodeConfigurationOption(BaseModel):
    NodeType: StrictStr | None = None
    NumberOfNodes: StrictInt | None = None
    EstimatedDiskUtilizationPercent: StrictFloat | StrictInt | None = None
    Mode: StrictStr | None = None
