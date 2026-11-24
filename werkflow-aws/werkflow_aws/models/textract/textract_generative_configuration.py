from __future__ import annotations
from pydantic import BaseModel
from .textract_figure_caption_configuration import TextractFigureCaptionConfiguration
from .textract_summarization_configuration import TextractSummarizationConfiguration


class TextractGenerativeConfiguration(BaseModel):
    Summarization: TextractSummarizationConfiguration | None = None
    FigureCaption: TextractFigureCaptionConfiguration | None = None
