practice_minutes = input('How many practice minutes?')

print('You have', practice_minutes, 'practice minutes.')

practice_hours = (int(practice_minutes) / 60)

hours_remaining = (50 - int(practice_hours)) 

print('You have', round(practice_hours), 'practice hours and you require', hours_remaining, 'more hours to meet your training requirements.')