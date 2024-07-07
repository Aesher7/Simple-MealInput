# Get the current time in hours and minutes from the user
current_time = float(input("Enter the current time (in hours, e.g., 13.25 for 13:15): "))

# Get the number of hours to wait for the alarm
wait_hours = float(input("Enter the number of hours to wait for the alarm: "))

# Calculate the total time in hours
total_time = current_time + wait_hours

# Extract the whole number part for hours and the fractional part for minutes
total_hours = int(total_time) % 24
total_minutes = (total_time - int(total_time)) * 60

# If total_minutes exceeds 60, adjust hours and minutes accordingly
if total_minutes >= 60:
    total_hours = (total_hours + int(total_minutes / 60)) % 24
    total_minutes = total_minutes % 60

# Display the alarm time
print(f"The alarm will go off at: {total_hours:02d}:{int(total_minutes):02d}")
