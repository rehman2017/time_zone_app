from datetime import datetime
from zoneinfo import ZoneInfo

def get_current_time(timezone: str) -> str:
    """Returns the current time in the given timezone."""
    return datetime.now(ZoneInfo(timezone)).strftime('%d-%b-%Y %I:%M %p')

def convert_time(from_tz: str, to_tz: str, input_time: str) -> str:
    """Converts a given time from one timezone to another."""
    input_dt = datetime.strptime(input_time, "%H:%M").replace(
        year=datetime.today().year, month=datetime.today().month, day=datetime.today().day,
        tzinfo=ZoneInfo(from_tz)
    )
    converted_dt = input_dt.astimezone(ZoneInfo(to_tz))
    return converted_dt.strftime('%d-%b-%Y %I:%M %p')

TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney",
    "America/Los_Angeles", "Europe/Berlin", "Asia/Dubai", "Asia/Kolkata", "Africa/Cairo"
]

def main():
    print("\nTIME ZONE CONVERTER\n---------------------")
    print("Available Time Zones:")
    for i, tz in enumerate(TIME_ZONES, 1):
        print(f"{i}. {tz}")
    
    # Display current time for selected timezone
    tz_choice = int(input("\nSelect a timezone to view current time (1-10): ")) - 1
    if 0 <= tz_choice < len(TIME_ZONES):
        print(f"Current time in {TIME_ZONES[tz_choice]}: {get_current_time(TIME_ZONES[tz_choice])}")
    else:
        print("Invalid choice!")

    # Time Conversion
    from_tz = TIME_ZONES[int(input("\nSelect source timezone (1-10): ")) - 1]
    to_tz = TIME_ZONES[int(input("Select target timezone (1-10): ")) - 1]
    input_time = input("Enter time in HH:MM format (24-hour): ")
    try:
        converted_time = convert_time(from_tz, to_tz, input_time)
        print(f"Converted Time from {from_tz} to {to_tz}: {converted_time}")
    except ValueError:
        print("Invalid time format! Use HH:MM (24-hour format).")

if __name__ == "__main__":
    main()
