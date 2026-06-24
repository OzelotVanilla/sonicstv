import subprocess

subprocess.run(
    "rm -r ./build/;"
    + "mkdir ./build/;"  # For egg-info to generate
    + " python -m pip install -e . --break-system-packages --config-settings editable_mode=strict",
    shell=True
)
