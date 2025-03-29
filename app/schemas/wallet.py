from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI()


class WalletDB(BaseModel):
    id: int
    balance: int
    energy: int
    bandwidth: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
