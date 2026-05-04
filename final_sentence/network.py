"""Socket helpers for the multiplayer lobby."""

import json
import socket


def send_json(sock, payload):
    # Send a JSON line through a socket.
    try:
        sock.sendall((json.dumps(payload) + "\n").encode("utf-8"))
        return True
    except OSError:
        return False


def read_json_lines(sock, callback):
    # Read JSON lines from a socket.
    buffer = ""
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                break
            buffer += data.decode("utf-8")
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                if line.strip():
                    callback(json.loads(line))
    except (OSError, json.JSONDecodeError):
        pass


def get_local_ip():
    # Find the LAN-facing local IP.
    try:
        probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        probe.connect(("8.8.8.8", 80))
        ip = probe.getsockname()[0]
        probe.close()
        return ip
    except OSError:
        return "127.0.0.1"

