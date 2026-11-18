# Backup Proof

Show the age of the latest completed Mac backup and the time left before it becomes overdue.

A quiet Time Machine menu can mean a recent backup or a drive that has been away all day. This display gives the age of the last completed copy and the time left under your own freshness rule.

## Check the latest completed copy

1. Make the Time Machine destination available to your Mac and set a maximum age in hours.
2. Read **BACKUP AGE**. The rear shows the timestamp macOS supplied for the last completed copy and the configured threshold.
3. Turn once to **TIME LEFT**. The example shows two hours of margin against a 24-hour limit.

![Backup age shows 22.0 hours and the next page shows 2.0 hours left.](media/guide/inspect-backup-margin.gif)

## Recheck after reconnecting a drive

1. Reconnect or mount the destination. Use Time Machine itself if you need to start a backup.
2. Once a copy has completed, turn back to the age page and click to fetch the companion reading. Check the timestamp as well as the decimal hours.
3. If the age exceeds your limit, the margin page reads **OVERDUE BY** and shows the amount over the limit.

![The time-left view returns to the 22.0-hour age of the last completed copy.](media/guide/return-to-backup-age.gif)

## Example from the emulator

With a 24-hour limit, a 22-hour-old backup leaves two hours. At 26 hours the same copy would be two hours overdue. An inaccessible destination is reported as unavailable rather than being treated as a new backup. The recording used a controlled backup timestamp supplied to the adapter.

## Set up the source

Set max_hours to your preferred freshness limit. The host reads tmutil latestbackup -t. Connect or mount the Time Machine destination so macOS can find its latest completed copy. A missing or inaccessible destination is reported as unavailable. The app does not start a backup.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run in the emulator

Open BUSY Bar Emulator. From this repository, run:

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

Press **Back** to exit.

The GIFs are excerpts from the emulator recording. Each front-display pixel is shown at 9× its original width and height. The end frames pause for reading.

[Full recording](media/controls.mp4) · [Rear display](screenshots/back-1.png) · [Firmware test](EMULATOR-QA.md) · [MIT license](LICENSE)
