# -*- coding: utf8 -*-

from jira import JIRA
import datetime,calculatePMI
import influx

UserName='[User Account]'
Password='[Password]'
Server='[Server Address]'

now = datetime.datetime.now()
jira = JIRA(basic_auth=(UserName, Password), options={'server': Server})

NotCloseIssues=jira.search_issues(jql_str='project = Qt_NavUI AND type = Bug AND status != Done')

total_score = 0
odin_score = 0
guanyu_score = 0
mindtree_score = 0
unassigned_score = 0

print "********** Issues List *********"

for item in NotCloseIssues:
    SeverityPMI = 4
    issue = jira.issue(item.key)

    if issue.fields.customfield_10210:
        SeverityPMI = calculatePMI.SeverityPMI(str(issue.fields.customfield_10210.id))
        IssuePMI = SeverityPMI * calculatePMI.StatusPMI(str(issue.fields.status.id))
    else:
        IssuePMI = SeverityPMI * calculatePMI.StatusPMI(str(issue.fields.status.id))

    if str(issue.fields.customfield_10390) == 'Team_Millau':
        mindtree_score = mindtree_score + IssuePMI
    elif str(issue.fields.customfield_10390) == 'Team_GuanYu':
        guanyu_score = guanyu_score + IssuePMI
    elif str(issue.fields.customfield_10390) == 'Team_Odin':
        odin_score = odin_score + IssuePMI
    else:
        unassigned_score = unassigned_score + IssuePMI

    print item.key, issue.fields.customfield_10210, IssuePMI, issue.fields.customfield_10390

total_score = mindtree_score + guanyu_score + odin_score + unassigned_score
taipei_score = guanyu_score + odin_score


print "========== {} PMI ==========".format(now.date())

print "Total Score:", total_score
print "MindTree Score:", mindtree_score
print "GuanYu Score:", guanyu_score
print "Odin Score:", odin_score
print "Taipei Score:", taipei_score
print "Unassigned Score:", unassigned_score


date = str(now.date())

influx.writeDB(date,float(total_score),'total')
influx.writeDB(date,float(mindtree_score),'mindtree')
influx.writeDB(date,float(guanyu_score),'guanyu')
influx.writeDB(date,float(odin_score),'odin')
influx.writeDB(date,float(taipei_score),'taipei')
influx.writeDB(date,float(unassigned_score),'unassigned')
