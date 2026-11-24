from __future__ import annotations
from pydantic import BaseModel
from .lambda_direct_s3_read import LambdaDirectS3Read


class LambdaS3FilesConfig(BaseModel):
    DirectS3Read: LambdaDirectS3Read | None = None
