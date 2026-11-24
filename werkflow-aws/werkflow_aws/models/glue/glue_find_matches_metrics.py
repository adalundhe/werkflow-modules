from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .glue_column_importance import GlueColumnImportance
from .glue_confusion_matrix import GlueConfusionMatrix


class GlueFindMatchesMetrics(BaseModel):
    AreaUnderPRCurve: StrictFloat | StrictInt | None = None
    Precision: StrictFloat | StrictInt | None = None
    Recall: StrictFloat | StrictInt | None = None
    F1: StrictFloat | StrictInt | None = None
    ConfusionMatrix: GlueConfusionMatrix | None = None
    ColumnImportances: list[GlueColumnImportance] | None = None
