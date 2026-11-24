from __future__ import annotations
from pydantic import BaseModel
from .ecr_aws_ecr_container_image_details import ECRAwsEcrContainerImageDetails


class ECRResourceDetails(BaseModel):
    awsEcrContainerImage: ECRAwsEcrContainerImageDetails | None = None
