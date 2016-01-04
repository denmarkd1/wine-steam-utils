# wine-steam-utils
Utilities to Windows Steam games run in WINE


#wine-steam-game
wine-steam-game is a script that will start the Windows version of Steam in WINE in silent mode (no popups), then launch a specified game.  It will check whether the game is alive every 5 seconds, and when the game is shutdown, the script closes WINE Steam with it.

Usage: wine-steam-game <appid> <gameexe>

Example (Rocket League): wine-steam-game 252950 RocketLeague.exe

This will launch WINE Steam, open Rocket League, then close WINE Steam when Rocket League is closed.  You will manually have to find the EXE name for each game, as of right now I have not found a way to automatically pull it.


#steamscraper.py
REQUIRES [steamapiwrapper](https://github.com/naiyt/steamapiwrapper) to either be installed or be in the same directory as steamscraper.py.  This will pull all of the screenshots used as steam backgrounds from Steam itself.  This is useful if you have a WINE game launched through Steam as a non-steam game, as you can use the actual backgrounds for the game and not the ugly flat colors.

Usage: python steamscraper.py <appid>

Example (Rocket League): python steamscraper.py 252950

The screenshots will be downloaded into a folder named after the specified game.

To make the specified screenshots your background, you must:
1. Run the non-steam game and take a screenshot with the Steam overlay
2. Use the "Show On Disk" button to navigate into the screenshot folder of the non-steam game
3. Delete everything in there and paste all the screenshots you want to use
4. Restart Steam
5. Hit "View Screenshot Library" for the game you want to have backgrouds for.
6. The screenshots will update with the images you downloaded.  It will give a "Missing Screenshot" for the original screenshot you took, use Steam to delete that screenshot.  It will not cause issues.
