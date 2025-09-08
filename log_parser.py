import json

def parse_logs(logfile):
    with open(logfile, "r") as f:
        lines = f.readlines()

    errors = [line.strip() for line in lines if "ERROR" in line]

    result = {"errors": errors}
    return result

if __name__ == "__main__":
    data = parse_logs("app.log")
    print(json.dumps(data, indent=4))
