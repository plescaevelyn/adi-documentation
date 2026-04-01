#!/bin/python3

import json
import sys

def pretty_print(event):
    t = event.get("type")

    if t == "session":
        print(f"\n=== session {event.get('id', '')[:8]} ===")

    elif t == "message" and "message" in event:
        msg = event["message"]
        role = msg.get("role")
        if role == "user":
            content = msg.get("content", "")
            if isinstance(content, list) and content:
                text = content[0].get("text", "") if isinstance(content[0], dict) else str(content)
            else:
                text = str(content)
            print(f"\n[user] {text[:200]}{'...' if len(text) > 200 else ''}")
        elif role == "assistant":
            for c in msg.get("content", []):
                if c.get("type") == "text":
                    print(f"\n[assistant] {c.get('text', '')}")
                elif c.get("type") == "toolCall":
                    print(f"\n  [{c.get('name')}] {json.dumps(c.get('arguments', {}))}")
            usage = msg.get("usage", {})
            if usage.get("output"):
                print(f"  ({usage.get('input', 0)}, {usage.get('output', 0)} tokens)")
        elif role == "toolResult":
            content = msg.get("content", [{}])
            text = content[0].get("text", "") if content and isinstance(content[0], dict) else ""
            err = " ERROR" if msg.get("isError") else ""
            print(f"  [{msg.get('toolName')}]{err} {text[:100]}{'...' if len(text) > 100 else ''}")

    elif t == "message_start":
        msg = event.get("message", {})
        role = msg.get("role")
        if role == "user":
            content = msg.get("content", [{}])
            if content and isinstance(content[0], dict):
                text = content[0].get("text", "")
            else:
                text = str(content)
            print(f"\n[user] {text[:100]}{'...' if len(text) > 100 else ''}")
        elif role == "assistant":
            pass
        elif role == "toolResult":
            name = msg.get("toolName", "")
            print(f"\n[{name}] ", end="", flush=True)

    elif t == "message_end":
        msg = event.get("message", {})
        role = msg.get("role")
        if role == "assistant":
            usage = msg.get("usage", {})
            if usage.get("output"):
                print(f" ({usage.get('input', 0)}, {usage.get('output', 0)} tokens)")
        elif role == "toolResult":
            content = msg.get("content", [{}])
            if content and isinstance(content[0], dict):
                text = content[0].get("text", "")
                print(text[:80] + ("..." if len(text) > 80 else ""))

    elif t == "message_update":
        ae = event.get("assistantMessageEvent", {})
        ae_type = ae.get("type")

        if ae_type == "text_delta":
            delta = ae.get("delta", "")
            print(delta, end="", flush=True)

        elif ae_type == "toolcall_delta":
            delta = ae.get("delta", "")
            print(delta, end="", flush=True)

        elif ae_type == "toolcall_start":
            tc = ae.get("partial", {}).get("content", [{}])[0]
            print(f"\n[{tc.get('name', '')}] ", end="", flush=True)

        elif ae_type == "toolcall_end":
            print()

    elif t == "tool_execution_start":
        print(f"  {event.get('toolName')}", end="", flush=True)

    elif t == "tool_execution_end":
        err = event.get("isError")
        print(" error" if err else " done")

    elif t == "turn_end":
        pass

    elif t == "agent_end":
        print("\n=== agent end ===")

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
            pretty_print(event)
        except json.JSONDecodeError:
            pass

if __name__ == "__main__":
    main()
