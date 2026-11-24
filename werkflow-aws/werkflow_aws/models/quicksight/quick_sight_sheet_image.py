from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_image_custom_action import QuickSightImageCustomAction
from .quick_sight_image_interaction_options import QuickSightImageInteractionOptions
from .quick_sight_sheet_image_scaling_configuration import QuickSightSheetImageScalingConfiguration
from .quick_sight_sheet_image_source import QuickSightSheetImageSource
from .quick_sight_sheet_image_tooltip_configuration import QuickSightSheetImageTooltipConfiguration


class QuickSightSheetImage(BaseModel):
    SheetImageId: StrictStr | None = None
    Source: QuickSightSheetImageSource | None = None
    Scaling: QuickSightSheetImageScalingConfiguration | None = None
    Tooltip: QuickSightSheetImageTooltipConfiguration | None = None
    ImageContentAltText: StrictStr | None = None
    Interactions: QuickSightImageInteractionOptions | None = None
    Actions: list[QuickSightImageCustomAction] | None = None
