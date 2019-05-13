#!/usr/bin/env python3.7

import os

# What happens when variable isn't present?  We get an exception.  Using getenv with deefault solves this...
# stage = os.environ["STAGE"].upper()
stage = os.getenv("STAGE", default="dev").upper()

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! = " + output

print(output)
