from astropy import time
t = time.Time("2025-09-09 22:09:00", format="iso", scale="utc")
print(t.tt)