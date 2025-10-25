s = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

new_s = (s.replace(' ',',')).split(',')

for new in new_s:
    if 'h' in new:
        hours = int(new.replace('h',''))
        total_minutes += hours*60
    elif 'm' in new:
        minutes = int(new.replace('m',''))
        total_minutes += minutes
    elif 's' in new:
        seconds = float(new.replace('s',''))
        total_minutes += seconds/60

print(int(total_minutes))