from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_transform_parameters import GlueTransformParameters


class GlueUpdateMLTransformRequest(BaseModel):
    TransformId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Parameters: GlueTransformParameters | None = None
    Role: StrictStr | None = None
    GlueVersion: StrictStr | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    WorkerType: Literal['Standard', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'G.025X', 'Z.2X', 'G.12X', 'G.16X', 'R.1X', 'R.2X', 'R.4X', 'R.8X'] | None = None
    NumberOfWorkers: StrictInt | None = None
    Timeout: StrictInt | None = None
    MaxRetries: StrictInt | None = None
