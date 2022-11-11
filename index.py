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

 # Candidates for Auditor----------------------------------
    aud1_no = 1
    aud2_no = 2
    aud3_no = 3
    aud1_name = "Tanya Hwande  from arts"
    aud2_name = "Sharlene Tavasiya  from sciences"
    aud3_name = "Marry Jeredza  from commercials"
    aud_1 = 0
    aud_2 = 0
    aud_3 = 0
    # Candidates for Treasurer----------------------------------
    tre1_no = 1
    tre2_no = 2
    tre3_no = 3
    tre1_name = "Bryan Hombe from arts"
    tre2_name = "Adrian Rumba  from sciences"
    tre3_name = "Ritchmond Gore from arts"
    tre_1 = 0
    tre_2 = 0
    tre_3 = 0
    # Candidates for Media Information----------------------------------
    media1_no = 1
    media2_no = 2
    media3_no = 3
    media1_name = "Daniel Chirugwi  from arts"
    media2_name = "Agnes Sigudu  from sciences"
    media3_name = "John Marata  from commercials"
    media_1 = 0
    media_2 = 0
    media_3 = 0
    # Candidates for First Year Representative----------------------------------
    f_rep1_no = 1
    f_rep2_no = 2
    f_rep3_no = 3
    f_rep1_name = "Osward Nhema from Form 4b1"
    f_rep2_name = "Edward Gasiri from 4b2"
    f_rep3_name = "Drake Bazuzu from 4b3"
    f_rep_1 = 0
    f_rep_2 = 0
    f_rep_3 = 0
    # Candidates for Second Year Representative----------------------------------
    s_rep1_no = 1
    s_rep2_no = 2
    s_rep3_no = 3
    s_rep1_name = "Walter Chikumba from 3b1"
    s_rep2_name = "Marshal Mereki from 3b2"
    s_rep3_name = "Roronoa Zororo from 4b3"
    s_rep_1 = 0
    s_rep_2 = 0
    s_rep_3 = 0
    # Candidates for Third Year Representative----------------------------------
    t_rep1_no = 1
    t_rep2_no = 2
    t_rep3_no = 3
    t_rep1_name = "Gilbert Chironzi from 2b1"
    t_rep2_name = "Mohammad Ali Abudula fro 2b2"
    t_rep3_name = "Jonga Jonga from 2b3"
    t_rep_1 = 0
    t_rep_2 = 0
    t_rep_3 = 0
    # Candidates for Fourth Year Representative----------------------------------
    frt_rep1_no = 1
    frt_rep2_no = 2
    frt_rep3_no = 3
    frt_rep1_name = "Charlotte Katambo from 1b1"
    frt_rep2_name = "Raidzai Jozoro from 1b2"
    frt_rep3_name = "Jean Magodo fro  1b3"
    frt_rep_1 = 0
    frt_rep_2 = 0
    frt_rep_3 = 0

    def welcome(obj):
        today = date.today()
        datetime = today.strftime("%B %d, %Y")
        print("-------------------------------------------------------------------------------------")
        print("                      Jameson High School(JMS)                                       ")
        
        print("                          Main Hall " + datetime + "                             ")
        print("======================================================================================")
        print("************* Welcome to Jameson High School Students Elections for 2022 *************")

    def loading(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rAnalyzing ID...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(2)
        done = True

    def error_loading(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rAnalyzing ID...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(5)
        done = True

    def loading_result(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rPlease wait while reading the result...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(8)
        done = True
