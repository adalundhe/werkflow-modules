from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class CloudWatchLogsFieldsData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    data: StrictBytes | Any | None = None
