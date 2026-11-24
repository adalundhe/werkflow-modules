from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_kpi_field_wells import QuickSightKPIFieldWells
from .quick_sight_kpi_options import QuickSightKPIOptions
from .quick_sight_kpi_sort_configuration import QuickSightKPISortConfiguration
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightKPIConfiguration(BaseModel):
    FieldWells: QuickSightKPIFieldWells | None = None
    SortConfiguration: QuickSightKPISortConfiguration | None = None
    KPIOptions: QuickSightKPIOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
