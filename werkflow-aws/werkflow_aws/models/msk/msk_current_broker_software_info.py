from pydantic import BaseModel, StrictStr, StrictInt


class MSKCurrentBrokerSoftwareInfo(BaseModel):
    ConfigurationArn: StrictStr
    ConfigurationRevision: StrictInt
    KafkaVersion: StrictStr