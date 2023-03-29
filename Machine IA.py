jobs = [
    {"name": "W1", "A1_time": 30, "A2_time": 50},
    {"name": "W2", "A1_time": 0, "A2_time": 40},
    {"name": "W3", "A1_time": 20, "A2_time": 70},
    {"name": "W4", "A1_time": 30, "A2_time": 0},
    {"name": "W5", "A1_time": 50, "A2_time": 20}
]

# Define events
events = []

for job in jobs:
    events.append({"type": "job_available", "job": job, "time": 0})

A1_busy_until = 0
A2_busy_until = 0
completed_jobs = []

# Simulate events
while len(events) > 0:
    events = sorted(events, key=lambda x: (x["time"], x["job"]["name"]))
    event = events.pop(0)
    time = event["time"]
    
    if event["type"] == "job_available":
        job = event["job"]
        if job["A1_time"] == 0 and job["A2_time"] == 0:
            completed_jobs.append((job, time))
        elif job["A1_time"] == 0:
            events.append({"type": "start_job", "job": job, "machine": "A2", "time": A2_busy_until})
        elif job["A2_time"] == 0:
            events.append({"type": "start_job", "job": job, "machine": "A1", "time": A1_busy_until})
        else:
            A1_available_at = max(time, A1_busy_until)
            A2_available_at = max(time, A2_busy_until)
            if A1_available_at + job["A1_time"] <= A2_available_at + job["A2_time"]:
                events.append({"type": "start_job", "job": job, "machine": "A1", "time": A1_available_at})
            else:
                events.append({"type": "start_job", "job": job, "machine": "A2", "time": A2_available_at})
    
    elif event["type"] == "start_job":
        job = event["job"]
        machine = event["machine"]
        if machine == "A1":
            A1_busy_until = time + job["A1_time"]
            events.append({"type": "end_job", "job": job, "machine": machine, "time": A1_busy_until})
        else:
            A2_busy_until = time + job["A2_time"]
            events.append({"type": "end_job", "job": job, "machine": machine, "time": A2_busy_until})
    
    elif event["type"] == "end_job":
        job = event["job"]
        completed_jobs.append((job, time))
        
print("Completed jobs:")
for job, completion_time in completed_jobs:
    print(f"Job {job['name']} completed at time {completion_time}")

total_time = completed_jobs[-1][1]
print(f"Total time: {total_time}")