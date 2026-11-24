from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_cell_information import DataZoneCellInformation
from .data_zone_environment_config import DataZoneEnvironmentConfig
from .data_zone_git_metadata import DataZoneGitMetadata
from .data_zone_notebook_error import DataZoneNotebookError


class DataZoneUpdateNotebookResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    domainId: StrictStr | None = None
    cellOrder: list[DataZoneCellInformation] | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    lockedBy: StrictStr | None = None
    lockedAt: datetime.datetime | StrictStr | None = None
    lockExpiresAt: datetime.datetime | StrictStr | None = None
    computeId: StrictStr | None = None
    metadata: dict[StrictStr, StrictStr] | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    environmentConfiguration: DataZoneEnvironmentConfig | None = None
    error: DataZoneNotebookError | None = None
    gitMetadata: DataZoneGitMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
