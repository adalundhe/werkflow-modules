from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueConfusionMatrix(BaseModel):
    NumTruePositives: StrictInt | None = None
    NumFalsePositives: StrictInt | None = None
    NumTrueNegatives: StrictInt | None = None
    NumFalseNegatives: StrictInt | None = None
