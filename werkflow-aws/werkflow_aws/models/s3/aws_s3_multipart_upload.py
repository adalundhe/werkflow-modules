from pydantic import BaseModel, Field
from .aws_s3_multipart_upload_part import AWSs3MultipartUploadPart

class AWSs3MultipartUpload(BaseModel):
    Parts: list[AWSs3MultipartUploadPart] = Field(min_length=1)
