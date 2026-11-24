from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_cell_information import DataZoneCellInformation
from .data_zone_environment_config import DataZoneEnvironmentConfig


class DataZoneUpdateNotebookRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    description: StrictStr | None = None
    status: Literal['ACTIVE', 'ARCHIVED', 'SYNC_IN_PROGRESS', 'SYNC_FAILED'] | None = None
    name: StrictStr | None = None
    cellOrder: list[DataZoneCellInformation] | None = None
    type: Literal['DATA', 'SQL'] | None = None
    metadata: dict[StrictStr, StrictStr] | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    environmentConfiguration: DataZoneEnvironmentConfig | None = None
    clientToken: StrictStr | None = None
