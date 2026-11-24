from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockRFTHyperParameters(BaseModel):
    epochCount: StrictInt | None = None
    batchSize: StrictInt | None = None
    learningRate: StrictFloat | StrictInt | None = None
    maxPromptLength: StrictInt | None = None
    trainingSamplePerPrompt: StrictInt | None = None
    inferenceMaxTokens: StrictInt | None = None
    reasoningEffort: StrictStr | None = None
    evalInterval: StrictInt | None = None
