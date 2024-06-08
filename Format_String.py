# assume this CONFIG holds sensitive information
CONFIG = {
    "KEY": "abcdefg"
}
  
class PeopleInfo:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
  
# case 1: st obtained from user
jobId = input()
print("Job ID: {}".format(jobId))