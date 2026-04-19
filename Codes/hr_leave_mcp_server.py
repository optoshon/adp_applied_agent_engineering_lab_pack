
import json
import os
from mcp.server.fastmcp import FastMCP

LEAVE_DB_PATH = "/home/ec2-user/SageMaker/leave_requests.json"

mcp = FastMCP("HR Leave MCP Server")


def load_requests():
    if not os.path.exists(LEAVE_DB_PATH):
        return []
    with open(LEAVE_DB_PATH, "r") as f:
        return json.load(f)


def save_requests(data):
    with open(LEAVE_DB_PATH, "w") as f:
        json.dump(data, f, indent=2)


@mcp.tool(description="Apply leave for an employee")
def apply_leave(employee_id: str = "EMP001", days: int = 1, reason: str = "Not specified") -> str:
    requests = load_requests()

    record = {
        "employee_id": employee_id,
        "days": days,
        "reason": reason
    }
    requests.append(record)
    save_requests(requests)

    return f"Leave applied successfully for {days} day(s) for employee {employee_id}. Reason: {reason}"


@mcp.tool(description="Get leave summary and leave history for an employee")
def get_leave_summary(employee_id: str = "EMP001") -> str:
    requests = load_requests()
    employee_records = [r for r in requests if r["employee_id"] == employee_id]

    if not employee_records:
        return f"No leave applications found for employee {employee_id}."

    total_days = sum(r["days"] for r in employee_records)

    lines = [f"Employee {employee_id} has applied for a total of {total_days} day(s) of leave."]
    lines.append("Leave history:")

    for i, record in enumerate(employee_records, start=1):
        lines.append(f"{i}. {record['days']} day(s) - Reason: {record['reason']}")

    return "\\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
