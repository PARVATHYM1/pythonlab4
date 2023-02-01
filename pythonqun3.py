from datetime import datetime
unix = int(input("Enter a unix value:" , ))
readable = datetime.fromtimestamp(unix).strftime("%d %B %Y %H:%M:%S")
print(readable)