# -*- coding: utf8 -*-
#This is for caculating the PMI score of ticket

def SeverityPMI(severityId):
    severitylist = {
        #Safety cases
        "16205": 0,
        "17130": 0,
        "24782": 0,
        "26318": 0,
        #Minor (C)
        "17133": 0.5,
        "16208": 0.5,
        "24781": 0.5,
        #Major (B)
        "17132": 1,
        "16207": 1,
        "24780": 1,
        #Critical (A)
        "17131": 2,
        "16206": 2,
        "24779": 2,
        "26319": 2,
    }
    return severitylist[severityId]

def StatusPMI(statusId):
    statuslist = {
        "1": 1, #Open
        "4": 1, #Open
        "10038": 1, #Open
        "10043": 1, #Waiting for information
        "10048": 1, #Wating for approval
        "10049": 1, #Approved
        "10051": 1, #Blocked
        "10056": 1, #Created, waiting approval
        "10057": 1, #Ready for development
        "10058": 1, #Sign off required
        "10209": 1, #New
        "10221": 1, #Triaged
        "10222": 1, #Under Triage
        "3": .75, #In Progress
        "10029": .5, #For Review
        "10036": .5, #Review
        "10046": .5, #In Review
        "10047": .5, #Ready for Review
        "5": .25, #Resolved
        "10042": .25, #In Testing
        "10045": .25, #Ready for testing
        "10189": .25, #Ready for verification
        "10173": .25, #Ready for integration
        "6": 0, #Closed
        "10030": 0, #Released
        "10031": 0, #Verified
        "10033": 0, #Accepted
        "10044": 0, #Done
        "10050": 0, #Not Approved
        "10059": 0, #Ready for deployment
        "10061": 0, #Ticket is rejected
        "10062": 0, #Deployed to production
        "10070": 0, #Rejected
    }
    return statuslist[statusId]

