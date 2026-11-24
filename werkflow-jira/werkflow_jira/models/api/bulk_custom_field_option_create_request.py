from __future__ import annotations
from pydantic import BaseModel
from .custom_field_option_create import CustomFieldOptionCreate


class BulkCustomFieldOptionCreateRequest(BaseModel):
    options: list[CustomFieldOptionCreate] | None = None
