from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_find_matches_parameters import GlueFindMatchesParameters


class GlueTransformParameters(BaseModel):
    TransformType: StrictStr | None = None
    FindMatchesParameters: GlueFindMatchesParameters | None = None
