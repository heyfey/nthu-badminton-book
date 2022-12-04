# nthu-badminton-book

1. Set sessions to book in `settings.json`

```json=
{
    "sessions": [
        "18:00",
        "19:00"
    ]
}
```

2. `start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"`

3. login with the chrome driver opened in step 2.

![](https://i.imgur.com/T4M3FQd.png)

4. Make you see the following page, and this page is on the first tab

![](https://i.imgur.com/D0sIdns.png)

5. `python book.py`
