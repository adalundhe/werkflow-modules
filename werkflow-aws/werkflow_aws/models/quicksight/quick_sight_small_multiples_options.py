from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .quick_sight_panel_configuration import QuickSightPanelConfiguration
from .quick_sight_small_multiples_axis_properties import QuickSightSmallMultiplesAxisProperties


class QuickSightSmallMultiplesOptions(BaseModel):
    MaxVisibleRows: StrictInt | None = None
    MaxVisibleColumns: StrictInt | None = None
    PanelConfiguration: QuickSightPanelConfiguration | None = None
    XAxis: QuickSightSmallMultiplesAxisProperties | None = None
    YAxis: QuickSightSmallMultiplesAxisProperties | None = None
