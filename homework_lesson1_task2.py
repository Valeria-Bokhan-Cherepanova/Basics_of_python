time_sec = int(input("Enter the time in sec: "))
hours = time_sec // 3600
minutes = (time_sec - hours * 3600) // 60 #or minutes = (time_sec // 60) - (hours * 60)
seconds = time_sec - (hours * 3600 + minutes * 60)  #or seconds = time % 60
print(f"The time is:  {hours:02} : {minutes:02} : {seconds:02}")
