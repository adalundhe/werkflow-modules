from __future__ import annotations
from pydantic import BaseModel, StrictBool


class OpenSearchSoftwareUpdateOptions(BaseModel):
    AutoSoftwareUpdateEnabled: StrictBool | None = None
    UseLatestServiceSoftwareForBlueGreen: StrictBool | None = None
