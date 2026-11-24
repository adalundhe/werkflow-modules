from __future__ import annotations
from pydantic import BaseModel
from .textract_bounding_box_configuration import TextractBoundingBoxConfiguration
from .textract_extraction_granularity import TextractExtractionGranularity
from .textract_output_format import TextractOutputFormat


class TextractExtractionConfiguration(BaseModel):
    BoundingBox: TextractBoundingBoxConfiguration | None = None
    Granularity: TextractExtractionGranularity | None = None
    OutputFormat: TextractOutputFormat | None = None
