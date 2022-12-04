# nthu-badminton-book

## How it works?

Read settings 
-> 
Wait until tomorrow 0:00 a.m. 
-> 
Book sessions on latest available day of the week, e.g., Book Thursday's sessions on Sunday 0:00 a.m.

## Usage

1. Config ID, password and sessions to book in `settings.json`.

```json=
{
    "id": "108067414",
    "password": "password",
    "sessions": {
        "Sunday": [],
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [
            "20:00",
            "21:00"
        ],
        "Friday": [],
        "Saturday": []
    }
}
```
> Note: Each ID can book at most two sessions each day of the week

2. `python book.py`
