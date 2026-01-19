#!/usr/bin/env python3
"""Container runtime parser for Podman JSON output."""

import json
import sys
from typing import Any, Dict, List, Union


def parse_containers(json_data: str):
    """Parse Podman container JSON and display info."""
    try:
        containers: List[Dict[str, Any]] = json.loads(json_data)

        if not containers:
            print("No containers running")
            return 0

        print(f"Running containers: {len(containers)}")
        for container in containers:
            name = container.get("Names", ["Unknown"])[0]
            image = container.get("Image", "Unknown")
            status = container.get("State", "Unknown")
            ports: Union[List[Dict[str, Any]], Dict[str, Any], None] = container.get(
                "Ports"
            )

            print(f"  • {name}")
            print(f"    Image: {image}")
            print(f"    Status: {status}")
            if ports:
                if isinstance(ports, list) and ports:
                    port_info: Dict[str, Any] = ports[0]
                elif isinstance(ports, dict):
                    port_info = ports
                else:
                    port_info = {}

                print(
                    f"    Ports:{port_info.get('host_port', 'N/A')} -> {port_info.get('container_port', 'N/A')}"
                )

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        return -1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            data = f.read()
    else:
        data = sys.stdin.read()

    parse_containers(data)
