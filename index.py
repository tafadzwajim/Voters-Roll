from datetime import date
import itertools
import threading
import time
import sys

#For ID Registration-------------
students_id = list(range(1000000))
num_of_stud = len(students_id)

class election():

    #Candidates for President----------------------------------
    p1_no = 1
    p2_no = 2
    p3_no = 3
    p1_name = "John Chimurenga from arts"
    p2_name = "chipo Chinengundu from sciences"
    p3_name = "Joyce Tekere from commercials"
    pres_1 = 0
    pres_2 = 0
    pres_3 = 0
    # Candidates for Vice President----------------------------------
    vp1_no = 1
    vp2_no = 2
    vp3_no = 3
    vp1_name = "Manuel Gudo  from arts"
    vp2_name = "Ellen kazhanje  from sciences"
    vp3_name = "Telica Jonga from commercials"
    vpres_1 = 0
    vpres_2 = 0
    vpres_3 = 0
    # Candidates for Secretary----------------------------------
    sec1_no = 1
    sec2_no = 2
    sec3_no = 3
    sec1_name = "Nick Zunde  from arts"
    sec2_name = "Albert Dube from sciences"
    sec3_name = "Garikai Sadza  from commercials"
    sec_1 = 0
    sec_2 = 0
    sec_3 = 0

