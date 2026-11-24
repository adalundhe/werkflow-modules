from __future__ import annotations
from pydantic import BaseModel
from .macie_s3_bucket_criteria_for_job import MacieS3BucketCriteriaForJob
from .macie_s3_bucket_definition_for_job import MacieS3BucketDefinitionForJob
from .macie_scoping import MacieScoping


class MacieS3JobDefinition(BaseModel):
    bucketCriteria: MacieS3BucketCriteriaForJob | None = None
    bucketDefinitions: list[MacieS3BucketDefinitionForJob] | None = None
    scoping: MacieScoping | None = None
