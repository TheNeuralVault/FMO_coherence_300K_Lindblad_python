#!/usr/bin/env python3
import subprocess, datetime
print("========================================")
print(f"{datetime.datetime.now()} | FMO_COHERENCE_300K_LINDBLAD_PYTHON MONITOR WAKING UP")
try:
    res = subprocess.run(['python3', 'organ_core.py'], capture_output=True, text=True)
    if res.returncode == 0:
        print("STATUS: OPTIMAL. Organ alignment perfect.")
        print(res.stdout.strip())
    else:
        print("CRITICAL: Matrix collapse.")
        print(res.stderr.strip())
except Exception as e:
    print(f"SYSTEM ERROR: {e}")
