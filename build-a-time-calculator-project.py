** start of main.py **

def add_time(start, duration, day = ''):
    days_of_week = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 7
    }

    new_time = ''
    new_day = ''
    day_num = 0

    if day:
        new_day = day.lower()

    if new_day:
        day_num = days_of_week[new_day]

    time_initials = start[5:].strip()
    
    index_of_start_colon = start.index(':')

    left_part_start = int(start[:index_of_start_colon])
    right_part_start = int(start[index_of_start_colon+1:5])
    
    index_of_dur_colon = duration.index(':')

    left_part_dur = int(duration[:index_of_dur_colon])
    right_part_dur = int(duration.split(':')[1])

    new_right_part = right_part_start + right_part_dur
    
    minutes_to_hours = 0
    
    if new_right_part >= 60:
        minutes_to_hours += new_right_part // 60
        new_right_part = new_right_part % 60
    
    new_left_part = (left_part_start + left_part_dur + minutes_to_hours) % 24

    days_count = (left_part_start + left_part_dur + minutes_to_hours) // 24
    
    str_left_part = str(new_left_part)
    str_right_part = str(new_right_part)

    if len(str_right_part) < 2:
        str_right_part = '0' + str_right_part
    
    if time_initials == 'AM':
        if new_left_part == 0:
            new_time = '12' + ':' + str_right_part + ' AM'
        elif new_left_part > 0 and new_left_part < 12:
            new_time = str_left_part + ':' + str_right_part + ' AM'
        elif new_left_part == 12:
            new_time = str_left_part + ':' + str_right_part + ' PM'
        else:
            str_left_part = str(new_left_part % 12)
            new_time = str_left_part + ':' + str_right_part + ' PM'
    else:
        if new_left_part == 0:
            new_time = '12' + ':' + str_right_part + ' PM'
        elif new_left_part > 0 and new_left_part < 12:
            new_time = str_left_part + ':' + str_right_part + ' PM'
        elif new_left_part == 12:
            days_count += 1
            new_time = str_left_part + ':' + str_right_part + ' AM'
        else:
            days_count += 1
            str_left_part = str(new_left_part % 12)
            new_time = str_left_part + ':' + str_right_part + ' AM'

    current_day = (days_count + day_num) % 7
    if day: 
        if current_day == 0:
            new_time += ", Sunday"
        elif current_day == 1:
            new_time += ", Monday"
        elif current_day == 2:
            new_time += ", Tuesday"
        elif current_day == 3:
            new_time += ", Wednesday"
        elif current_day == 4:
            new_time += ", Thursday"
        elif current_day == 5:
            new_time += ", Friday"
        elif current_day == 6:
            new_time += ", Saturday"

    if days_count == 1:
        new_time += ' (next day)'
    if days_count > 1:
        new_time += f' ({days_count} days later)'

    return new_time

print(add_time('3:30 PM', '2:12'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('8:16 PM', '466:02', 'tuesday'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))

** end of main.py **

