"""Measure elapsed time since the latest completed Time Machine backup."""
import re,subprocess,time
from datetime import datetime
from serve import page
INTERVAL=120
def latest():
    r=subprocess.run(["tmutil","latestbackup","-t"],capture_output=True,text=True,timeout=10)
    if r.returncode:raise ValueError("No accessible completed Time Machine backup")
    matches=re.findall(r"(?<!\d)(\d{4}-\d\d-\d\d-\d{6})(?!\d)",r.stdout)
    if matches:return datetime.strptime(matches[-1],"%Y-%m-%d-%H%M%S").timestamp()
    raw=r.stdout.strip()
    if raw.isdigit() and len(raw)==10:return float(raw)
    raise ValueError("Time Machine did not return a dated backup")
def snapshot(o,m):
    when=latest();hours=max(0,(time.time()-when)/3600);limit=float(o.get("max_hours",24))
    if limit<=0:raise ValueError("Choose a positive maximum age")
    slack=limit-hours
    return dict(state="Fresh backup" if slack>=0 else "Backup overdue",key=str(slack<0),alert=slack<0,pages=[
        page("BACKUP AGE",f"{hours:.1f}h",datetime.fromtimestamp(when).strftime("%Y-%m-%d %H:%M"),f"Limit {limit:g} hours",fraction=hours/limit),
        page("TIME LEFT" if slack>=0 else "OVERDUE BY",f"{abs(slack):.1f}h","Age of last completed copy","No backup is started")])
