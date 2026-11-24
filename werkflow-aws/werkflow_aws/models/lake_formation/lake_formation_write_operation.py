from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_add_object_input import LakeFormationAddObjectInput
from .lake_formation_delete_object_input import LakeFormationDeleteObjectInput


class LakeFormationWriteOperation(BaseModel):
    AddObject: LakeFormationAddObjectInput | None = None
    DeleteObject: LakeFormationDeleteObjectInput | None = None
