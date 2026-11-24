from __future__ import annotations
from pydantic import BaseModel
from .app_flow_field_type_details import AppFlowFieldTypeDetails


class AppFlowSupportedFieldTypeDetails(BaseModel):
    v1: AppFlowFieldTypeDetails | None = None
