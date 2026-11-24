from typing import Any
from pydantic import BaseModel


class AWSS3DeleteBucketResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None


AWSS3DeleteBucketReponse = AWSS3DeleteBucketResponse
