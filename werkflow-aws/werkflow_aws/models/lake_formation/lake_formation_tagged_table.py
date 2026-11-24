from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_column_lf_tag import LakeFormationColumnLFTag
from .lake_formation_lf_tag_pair import LakeFormationLFTagPair
from .lake_formation_table_resource import LakeFormationTableResource


class LakeFormationTaggedTable(BaseModel):
    Table: LakeFormationTableResource | None = None
    LFTagOnDatabase: list[LakeFormationLFTagPair] | None = None
    LFTagsOnTable: list[LakeFormationLFTagPair] | None = None
    LFTagsOnColumns: list[LakeFormationColumnLFTag] | None = None
