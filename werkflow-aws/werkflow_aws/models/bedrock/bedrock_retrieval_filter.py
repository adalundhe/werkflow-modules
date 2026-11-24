from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .bedrock_filter_attribute import BedrockFilterAttribute


class BedrockRetrievalFilter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    equals: BedrockFilterAttribute | None = None
    notEquals: BedrockFilterAttribute | None = None
    greaterThan: BedrockFilterAttribute | None = None
    greaterThanOrEquals: BedrockFilterAttribute | None = None
    lessThan: BedrockFilterAttribute | None = None
    lessThanOrEquals: BedrockFilterAttribute | None = None
    in_: BedrockFilterAttribute | None = Field(default=None, alias='in')
    notIn: BedrockFilterAttribute | None = None
    startsWith: BedrockFilterAttribute | None = None
    listContains: BedrockFilterAttribute | None = None
    stringContains: BedrockFilterAttribute | None = None
    andAll: list[BedrockRetrievalFilter] | None = None
    orAll: list[BedrockRetrievalFilter] | None = None
