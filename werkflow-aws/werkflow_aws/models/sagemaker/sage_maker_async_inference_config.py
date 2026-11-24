from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_async_inference_client_config import SageMakerAsyncInferenceClientConfig
from .sage_maker_async_inference_output_config import SageMakerAsyncInferenceOutputConfig


class SageMakerAsyncInferenceConfig(BaseModel):
    ClientConfig: SageMakerAsyncInferenceClientConfig | None = None
    OutputConfig: SageMakerAsyncInferenceOutputConfig | None = None
