from __future__ import annotations
from pydantic import BaseModel
from .open_search_natural_language_query_generation_options_output import OpenSearchNaturalLanguageQueryGenerationOptionsOutput
from .open_search_s3_vectors_engine import OpenSearchS3VectorsEngine
from .open_search_serverless_vector_acceleration import OpenSearchServerlessVectorAcceleration


class OpenSearchAIMLOptionsOutput(BaseModel):
    NaturalLanguageQueryGenerationOptions: OpenSearchNaturalLanguageQueryGenerationOptionsOutput | None = None
    S3VectorsEngine: OpenSearchS3VectorsEngine | None = None
    ServerlessVectorAcceleration: OpenSearchServerlessVectorAcceleration | None = None
