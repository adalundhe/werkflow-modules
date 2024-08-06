from __future__ import annotations

from typing import Literal

from pydantic import (
    BaseModel,
    StrictBool,
    StrictStr,
    confloat,
    conint,
)


class HeadingAttrs(BaseModel):
    level: conint(gt=0, le=6) = 1
    localId: StrictStr | None = None


class MediaSingleAttrs(BaseModel):
    layout: Literal[
        "wrap-left", "center", "wrap-right", "full-width", "align-start", "align-end"
    ] = "wrap-left"
    width: confloat(le=100.0, gt=0.0) | None
    alt: StrictStr | None = None
    widthType: Literal["pixel", "percentage"] | None = None


class OrderedListAttrs(BaseModel):
    order: conint(ge=1) | None = None


class PanelAttrs(BaseModel):
    panelType: Literal["info", "note", "warning", "success", "error"] = "info"


class ParagraphAttrs(BaseModel):
    localId: StrictStr


class TableAttrs(BaseModel):
    isNumberColumnEnabled: StrictBool = (False,)
    width: conint(ge=1) | None = None
    layout: Literal["center", "align-start"] | None = None
    displayMode: Literal["default", "fixed"] | None = None
