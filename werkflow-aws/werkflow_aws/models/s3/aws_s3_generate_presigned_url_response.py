from pydantic import (
    BaseModel,
    AnyHttpUrl
)


class AWSs3GeneratePresignedURLResponse(BaseModel):
    URL: AnyHttpUrl