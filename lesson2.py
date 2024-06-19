#simple calendar
from datetime import datetime

today = datetime.now()
date = today.strftime("%d.%m.%Y")
print('Today is ',date)
