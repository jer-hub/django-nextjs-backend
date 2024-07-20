from datetime import datetime
from pydantic import EmailStr
from .models import WaitListEntry
from ninja import Schema


class WaitListEntryListSchema(Schema):
    email: EmailStr

class WaitListEntryDetailsSchema(Schema):
    email: EmailStr
    updated: datetime
