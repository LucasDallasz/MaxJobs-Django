def profileNotRegistered(profile, job) -> bool:
    jobs = job.application_set.filter(profile=profile, job=job)
    return len(jobs) == 0

def validateApplication(profile, job) -> bool:
    jobs = profile.get_jobs_available()
    return job in jobs 