from __future__ import annotations
from pydantic import BaseModel
from .lex_bedrock_model_specification import LexBedrockModelSpecification
from .lex_data_source_configuration import LexDataSourceConfiguration


class LexQnAIntentConfiguration(BaseModel):
    dataSourceConfiguration: LexDataSourceConfiguration | None = None
    bedrockModelConfiguration: LexBedrockModelSpecification | None = None
