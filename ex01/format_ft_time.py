from datetime import datetime

now = datetime.now()
ts = datetime.timestamp(now)
formated_ts = ("{:,}".format(ts))
scientific_format = "{:.2e}".format(ts) 
print ("Seconds since January, 1, 1970:", formated_ts, "or", scientific_format, "in scientific notation")
print(now.strftime("%b %d %Y"))
