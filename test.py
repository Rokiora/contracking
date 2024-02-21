import datetime
from datetime import timedelta


ustart = datetime.datetime.strptime(input('Enter contract start date (dd-mm-yy): '), "%d-%m-%y").date().strftime("%d-%m-%y")
ureport_due = (datetime.datetime.strptime(ustart, "%d-%m-%y" ) - timedelta(weeks=6)).date().strftime("%d-%m-%y")
print(ureport_due)
                                    
# it works~! just gotta add to user_input.py later~! also reformat! to mm-dd-yy english~!
