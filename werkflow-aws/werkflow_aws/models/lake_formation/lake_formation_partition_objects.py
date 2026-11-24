from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_table_object import LakeFormationTableObject


class LakeFormationPartitionObjects(BaseModel):
    PartitionValues: list[StrictStr] | None = None
    Objects: list[LakeFormationTableObject] | None = None
