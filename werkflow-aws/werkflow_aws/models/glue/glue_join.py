from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_join_column import GlueJoinColumn


class GlueJoin(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    JoinType: StrictStr | None = None
    Columns: list[GlueJoinColumn] | None = None
