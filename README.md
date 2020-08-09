# SyncTwitterPixiv
Use extracted URL,follow accounts in pixiv by selenium in python.

## Preparation
Create .env based on .envsample.


Put chromedriver.exe(the chromedriver version have to be same your chrome browser version) under the current directory.
## Actual battle
First,extract your friend and extract pixiv link from they profile.

    python twpx.py

Second,follow they in your pixiv account by selenium.

    python pxfl.py