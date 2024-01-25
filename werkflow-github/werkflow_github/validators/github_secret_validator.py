from pydantic import BaseModel, StrictStr


class GithubSecret(BaseModel):
    key_id: StrictStr
    encrypted_value: StrictStr