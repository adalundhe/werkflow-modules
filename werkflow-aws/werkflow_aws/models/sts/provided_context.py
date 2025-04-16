from pydantic import BaseModel, StrictStr


class ProvidedContext(BaseModel):
    ProviderArn: StrictStr
    ContextAssertion: StrictStr