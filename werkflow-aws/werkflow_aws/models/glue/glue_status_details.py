from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel
from .glue_view_validation import GlueViewValidation

if TYPE_CHECKING:
    from .glue_table_model import GlueTableModel


class GlueStatusDetails(BaseModel):
    RequestedChange: GlueTableModel | None = None
    ViewValidations: list[GlueViewValidation] | None = None
