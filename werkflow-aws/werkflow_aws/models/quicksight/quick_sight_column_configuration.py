from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_colors_configuration import QuickSightColorsConfiguration
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_decal_settings_configuration import QuickSightDecalSettingsConfiguration
from .quick_sight_format_configuration import QuickSightFormatConfiguration


class QuickSightColumnConfiguration(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    FormatConfiguration: QuickSightFormatConfiguration | None = None
    Role: StrictStr | None = None
    ColorsConfiguration: QuickSightColorsConfiguration | None = None
    DecalSettingsConfiguration: QuickSightDecalSettingsConfiguration | None = None
