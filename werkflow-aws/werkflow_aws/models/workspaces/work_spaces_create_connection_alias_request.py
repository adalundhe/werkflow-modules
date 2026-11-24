from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesCreateConnectionAliasRequest(BaseModel):
    ConnectionString: StrictStr
    Tags: list[WorkSpacesTag] | None = None
