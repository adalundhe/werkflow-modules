from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, Field, StrictBool, StrictStr


class HeadingAttrs(BaseModel):
    level: Annotated[int, Field(gt=0, le=6)] = 1
    localId: StrictStr | None = None


class MediaSingleAttrs(BaseModel):
    layout: Literal[
        "wrap-left", "center", "wrap-right", "full-width", "align-start", "align-end"
    ] = "wrap-left"
    width: Annotated[float, Field(gt=0.0, le=100.0)] | None = None
    alt: StrictStr | None = None
    widthType: Literal["pixel", "percentage"] | None = None


class OrderedListAttrs(BaseModel):
    order: Annotated[int, Field(ge=1)] | None = None


class PanelAttrs(BaseModel):
    panelType: Literal["info", "note", "warning", "success", "error"] = "info"


class ParagraphAttrs(BaseModel):
    localId: StrictStr


class TableAttrs(BaseModel):
    isNumberColumnEnabled: StrictBool = False
    width: Annotated[int, Field(ge=1)] | None = None
    layout: Literal["center", "align-start"] | None = None
    displayMode: Literal["default", "fixed"] | None = None
