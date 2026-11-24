from __future__ import annotations

from typing import Annotated, List, Literal

from pydantic import (
    AliasChoices,
    BaseModel,
    Field,
    StrictInt,
    StrictStr,
)


class MediaAttrs(BaseModel):
    id: StrictStr
    type: Literal["file", "link"] = "link"
    width: StrictInt | None = None
    height: StrictInt | None = None
    collection: StrictStr
    occurrenceKey: StrictStr | None = Field(
        default=None,
        validation_alias=AliasChoices("occurrenceKey", "occurenceKey"),
    )
    alt: StrictStr | None = None


class TableCellAttrs(BaseModel):
    background: StrictStr
    colspan: Annotated[int, Field(ge=1)] = 1
    colwidth: List[Annotated[int, Field(ge=1)]] | None = None
    rowspan: Annotated[int, Field(ge=1)] = 1


class TableHeaderAttrs(BaseModel):
    background: StrictStr
    colspan: Annotated[int, Field(ge=1)] = 1
    colwidth: List[Annotated[int, Field(ge=1)]] | None = None
    rowspan: Annotated[int, Field(ge=1)] = 1
