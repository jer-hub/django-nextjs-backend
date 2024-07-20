from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from waitlist.models import WaitListEntry
from waitlist.schemas import WaitListEntryDetailsSchema, WaitListEntryListSchema

router = Router()

@router.get("", response=List[WaitListEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitListEntry.objects.all()
    return qs

@router.get("{pk}/", response=WaitListEntryDetailsSchema)
def get_waitlist_entry(request, pk:int):
    obj = get_object_or_404(WaitListEntry, id=pk)
    return obj