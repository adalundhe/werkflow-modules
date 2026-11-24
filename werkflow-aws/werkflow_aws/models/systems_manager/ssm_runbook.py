from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_target import SSMTarget
from .ssm_target_location import SSMTargetLocation


class SSMRunbook(BaseModel):
    DocumentName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    TargetParameterName: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    TargetMaps: list[dict[StrictStr, list[StrictStr]]] | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    TargetLocations: list[SSMTargetLocation] | None = None
