from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_table_field_url_configuration import QuickSightTableFieldURLConfiguration


class QuickSightTableFieldOption(BaseModel):
    FieldId: StrictStr | None = None
    Width: StrictStr | None = None
    CustomLabel: StrictStr | None = None
    Visibility: StrictStr | None = None
    URLStyling: QuickSightTableFieldURLConfiguration | None = None
