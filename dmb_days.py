import asyncio
from datetime import datetime, timedelta

async def demobilization(callup_date: str) -> int:
    callup = datetime.strptime(callup_date, "%d.%m.%Y").date()
    dmb_date = callup +  timedelta(days=365)
    today = datetime.today().date() 
    return  (dmb_date - today).days - 1
  
    
    
