from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_body_section_configuration import QuickSightBodySectionConfiguration
from .quick_sight_header_footer_section_configuration import QuickSightHeaderFooterSectionConfiguration
from .quick_sight_section_based_layout_canvas_size_options import QuickSightSectionBasedLayoutCanvasSizeOptions


class QuickSightSectionBasedLayoutConfiguration(BaseModel):
    HeaderSections: list[QuickSightHeaderFooterSectionConfiguration] | None = None
    BodySections: list[QuickSightBodySectionConfiguration] | None = None
    FooterSections: list[QuickSightHeaderFooterSectionConfiguration] | None = None
    CanvasSizeOptions: QuickSightSectionBasedLayoutCanvasSizeOptions | None = None
