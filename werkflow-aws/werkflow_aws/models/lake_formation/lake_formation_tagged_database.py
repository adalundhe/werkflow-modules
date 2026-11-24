from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_database_resource import LakeFormationDatabaseResource
from .lake_formation_lf_tag_pair import LakeFormationLFTagPair


class LakeFormationTaggedDatabase(BaseModel):
    Database: LakeFormationDatabaseResource | None = None
    LFTags: list[LakeFormationLFTagPair] | None = None
