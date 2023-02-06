import json
from typing import List, Dict
from sqlite3 import Row
from typing import Optional

from fastapi import Request
from pydantic import BaseModel
from pydantic.main import BaseModel
from fastapi.param_functions import Query
from dataclasses import dataclass
from lnbits.helpers import urlsafe_short_hash


class Relay(BaseModel):
    id: Optional[str] = None
    url: Optional[str] = None
    connected: Optional[bool] = None
    connected_string: Optional[str] = None
    status: Optional[str] = None
    active: Optional[bool] = None
    ping: Optional[int] = None

    def _init__(self):
        if not self.id:
            self.id = urlsafe_short_hash()


class RelayList(BaseModel):
    __root__: List[Relay]


# class nostrKeys(BaseModel):
#     pubkey: str
#     privkey: str

# class nostrNotes(BaseModel):
#     id: str
#     pubkey: str
#     created_at: str
#     kind: int
#     tags: str
#     content: str
#     sig: str

# class nostrCreateRelays(BaseModel):
#     relay: str = Query(None)

# class nostrCreateConnections(BaseModel):
#     pubkey: str = Query(None)
#     relayid: str = Query(None)

# class nostrRelays(BaseModel):
#     id: Optional[str]
#     relay: Optional[str]
#     status: Optional[bool] = False


# class nostrRelaySetList(BaseModel):
#     allowlist: Optional[str]
#     denylist: Optional[str]

# class nostrConnections(BaseModel):
#     id: str
#     pubkey: Optional[str]
#     relayid: Optional[str]

# class nostrSubscriptions(BaseModel):
#     id: str
#     userPubkey: Optional[str]
#     subscribedPubkey: Optional[str]
