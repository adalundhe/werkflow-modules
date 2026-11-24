from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_reference_line_dynamic_data_configuration import QuickSightReferenceLineDynamicDataConfiguration
from .quick_sight_reference_line_static_data_configuration import QuickSightReferenceLineStaticDataConfiguration


class QuickSightReferenceLineDataConfiguration(BaseModel):
    StaticConfiguration: QuickSightReferenceLineStaticDataConfiguration | None = None
    DynamicConfiguration: QuickSightReferenceLineDynamicDataConfiguration | None = None
    AxisBinding: StrictStr | None = None
    SeriesType: StrictStr | None = None
