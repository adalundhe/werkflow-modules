from __future__ import annotations

from typing import Literal

from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
    conint,
    conlist,
)


class MediaAttrs(BaseModel):
    id: StrictStr
    type: Literal["file", "link"] = "link"
    width: StrictInt | None = None
    height: StrictInt | None = None
    collection: StrictStr
    occurenceKey: StrictStr | None = None
    alt: StrictStr | None = None


class TableCellAttrs(BaseModel):
    background: StrictStr
    colspan: conint(ge=1) = 1
    colwidth: conlist(conint(ge=1)) | None = None
    rowspan: conint(ge=1) = 1


class TableHeaderAttrs(BaseModel):
    background: StrictStr
    colspan: conint(ge=1) = 1
    colwidth: conlist(conint(ge=1)) | None = None
    rowspan: conint(ge=1) = 1
