import re

schedule = []
next_id = 1

def menu():
    print("\n" + "=" * 32)
    print("        Weekly Schedule Manager")
    print("=" * 32)
    print("1. Add Time Block")
    print("2. Search Time Block")
    print("3. Sort Time Blocks")
    print("4. Remove Time Block")
    print("5. Display Schedule")
    print("6. Statistics")
    print("7. Fake Data Mode")
    print("8. Exit")
    print("=" * 32)

def valid_time_format(t):
    return re.match(r"^\d{2}:\d{2}$", t)

def time_to_minutes(t):
    return int(t[:2]) * 60 + int(t[3:])

def time_overlaps(start1, end1, start2, end2):
    return not (end1 <= start2 or start1 >= end2)

def add_time_block(schedule, next_id):
    day = input("Enter day (Monday-Sunday): ").strip().capitalize()
    start_time = input("Enter start time (HH:MM): ").strip()
    end_time = input("Enter end time (HH:MM): ").strip()
    title = input("Enter title: ").strip()

    if day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        print("Invalid day.")
        return schedule, next_id

    if not (valid_time_format(start_time) and valid_time_format(end_time)):
        print("Time must be in HH:MM format.")
        return schedule, next_id

    if start_time >= end_time:
        print("Start time must be before end time.")
        return schedule, next_id

    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)

    for block in schedule:
        if block[1] == day:
            existing_start = time_to_minutes(block[2])
            existing_end = time_to_minutes(block[3])
            if time_overlaps(start_minutes, end_minutes, existing_start, existing_end):
                print(f"Conflict with ID {block[0]}: {block[2]}–{block[3]} ({block[4]})")
                return schedule, next_id

    new_block = (next_id, day, start_time, end_time, title)
    schedule.append(new_block)
    print(f"Added: ID {next_id}, {day} {start_time}–{end_time} | {title}")
    next_id += 1
    return schedule, next_id

def search_time_block(schedule):
    if not schedule:
        print("No time blocks to search.")
        return
    term = input("Enter keyword to search: ").strip().lower()
    found = [b for b in schedule if term in b[1].lower() or term in b[2] or term in b[3] or term in b[4].lower()]
    if found:
        print(f"{len(found)} match(es) found:")
        for b in found:
            print(f"ID {b[0]}: {b[1]} {b[2]}–{b[3]} | {b[4]}")
    else:
        print(f"No matches found for '{term}'.")

def sort_time_blocks(schedule):
    if not schedule:
        print("No time blocks to sort.")
        return
    field = input("Sort by (day/start_time/end_time/title): ").strip().lower()
    if field not in ["day", "start_time", "end_time", "title"]:
        print("Invalid sort field.")
        return
    index = {"day": 1, "start_time": 2, "end_time": 3, "title": 4}[field]
    schedule.sort(key=lambda b: (b[index], b[2]) if field == "day" else b[index])
    print(f"Sorted by {field}.")

def remove_time_block(schedule):
    if not schedule:
        print("No time blocks to remove.")
        return
    try:
        block_id = int(input("Enter block ID to remove: "))
    except ValueError:
        print("Invalid ID.")
        return
    for block in schedule:
        if block[0] == block_id:
            schedule.remove(block)
            print(f"Removed ID {block_id}")
            return
    print(f"No block found with ID {block_id}.")

def display_schedule(schedule):
    if not schedule:
        print("No time blocks to display.")
        return
    print("\nSchedule:")
    for b in schedule:
        print(f"ID {b[0]}: {b[1]} {b[2]}–{b[3]} | {b[4]}")

def statistics(schedule):
    if not schedule:
        print("No statistics available.")
        return
    total = len(schedule)
    days = sorted(set(b[1] for b in schedule))
    titles = sorted(set(b[4] for b in schedule))
    print(f"Total blocks: {total}")
    print(f"Scheduled days: {', '.join(days)}")
    print(f"Unique titles: {', '.join(titles)}")

def fake_data_mode(schedule, next_id):
    data = [
        ("Monday", "09:00", "10:00", "Standup"),
        ("Tuesday", "10:00", "11:00", "Design"),
        ("Wednesday", "11:00", "12:00", "Development"),
        ("Thursday", "12:00", "13:00", "Lunch"),
        ("Friday", "13:00", "14:00", "Review"),
        ("Saturday", "14:00", "15:00", "Workout"),
        ("Sunday", "15:00", "16:00", "Reading")
    ]
    for day, start, end, title in data:
        schedule.append((next_id, day, start, end, title))
        print(f"Fake added: ID {next_id}, {day} {start}–{end} | {title}")
        next_id += 1
    return schedule, next_id

def main():
    global schedule, next_id
    while True:
        menu()
        choice = input("Choose (1–8): ").strip()
        if choice == "1":
            schedule, next_id = add_time_block(schedule, next_id)
        elif choice == "2":
            search_time_block(schedule)
        elif choice == "3":
            sort_time_blocks(schedule)
        elif choice == "4":
            remove_time_block(schedule)
        elif choice == "5":
            display_schedule(schedule)
        elif choice == "6":
            statistics(schedule)
        elif choice == "7":
            schedule, next_id = fake_data_mode(schedule, next_id)
        elif choice == "8":
            print("Exiting. Goodbye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
