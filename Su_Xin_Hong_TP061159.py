#SU XIN HONG
#TP061159 APD1F2106CE
def welcome_page ():
    operation = ''
    print ('Welcome, please choose your operation.')
    print ()
    print ('Enter "register" to register new patient.')
    print ('Enter "vaccine" for vaccine administration.')
    print ('Enter "search" to search for patient record.')
    print ('Enter "statistics" to see for patients statistics.')
    print ('Enter "0" to quit.')
    print ()
    while True: #Ensure no wrong input of operation
        operation = input ('Please enter your operation here: ')
        if (operation != 'register') and (operation != 'vaccine') and (operation != 'search') and (operation != 'statistics') and (operation != '0'):
            print ('Please input the right operation.')
            continue
        else:
            break
    return operation

def registration_age_name_vc ():
        while True: #Ensure no wrong input of vaccine centre
            vaccinationCentre = input ('Please choose your desired vaccination centre ["VC1" or "VC2"]: ')
            if (vaccinationCentre != "VC1") and (vaccinationCentre != "VC2"):
                print ('Please input the right code for vaccination centre.')
                print()
            else:
                break

        name = input ('Please input your name (without space, use "_" to indicate space): ')  
        name = name.replace(' ','_')
        while True: #Ensure no wrong input of age
            try:
                age = int (input('Please input your age: '))
                break
            except:
                print ('Please input your age in numerical form.')
 
        if (age<12):
            print ('Sorry you are too young for vaccine.\n')
            print ('=' * 50)
        return age, name, vaccinationCentre


def registration_operation (age, name, vaccinationCentre):
        eMail = input('Please input your email: ')
        contactNumber = input('Please input your contact number [without space]: ')

        if (age >= 18) and (age <= 45):
            while True: #Ensure no wrong input of vaccine name
                print ('The vaccine suitable for you are "AF", "BV" "CZ", "DM" and "EC".')
                vaccine = input('Please input the vaccine code that you want to have: ')
                if (vaccine != "AF") and (vaccine != "BV") and (vaccine != "CZ") and (vaccine != "DM") and (vaccine != "EC"):
                    print ('Please input the right code for the vaccine.')
                    print ()
                else:
                    break
        
        if (age > 45):
            while True: #Ensure no wrong input of vaccine name
                print ('The vaccine suitable for you are "AF", "BV", "DM" and "EC".')
                vaccine = input('Please input the vaccine code that you want to have: ')
                if (vaccine != "AF") and (vaccine != "BV") and (vaccine != "DM") and (vaccine != "EC"):
                    print ('Please input the right code for the vaccine.')
                    print ()
                else:
                    break

        if (age >= 12) and (age < 18):
            while True: #Ensure no wrong input of vaccine name
                print ('The vaccine suitable for you are "AF" ,"CZ" and "DM".')
                vaccine = input('Please input the vaccine code that you want to have: ')
                if (vaccine != "AF") and (vaccine != "CZ") and (vaccine != "DM"):
                    print ('Please input the right code for the vaccine.')
                    print ()
                else:
                    break

        print ('=' *50)
        if (vaccine == 'EC'):
            dosageRequired = '1Dose'
        else:
            dosageRequired = '2Dose'
        read_patient_information = open("patients.txt", "r")
        patient = read_patient_information.readlines()
        patientAmount = len(patient) - 1
        read_patient_information.close()
        patientCode = str(patientAmount + 1).zfill(4)
        print ('Your code is', patientCode, 'Please remember your code.')

        append_patient_information = open("patients.txt", "a")
        informationInput = '\n' + str(patientCode) + ' ' + name + ' ' + str(age) + ' ' + vaccinationCentre + ' ' + vaccine + ' ' + dosageRequired + ' ' + contactNumber + ' ' + eMail + ' ' + 'NEW'
        append_patient_information.write(informationInput)
        append_patient_information.close()

        print ('Thanks for registering', name, '.', 'Your registered vaccine is', vaccine)
        print ('Your code is ', patientCode)
        input ('Press Enter to continue.') #This is to let the user to have time to look at the information
        print ('=' * 50)

def vaccination_operation ():
        while True:
            registration = input('Had you done your registration? ["yes" if yes, "no" if no]: ')
            if (registration != 'yes') and (registration != 'no'): #Ensure no wrong input
                print ('Please input the right answer.')
                continue
            elif (registration == 'no'):
                ageNameVc = registration_age_name_vc ()
                name = ageNameVc[1]
                age = ageNameVc[0]
                vaccinationCentre = ageNameVc[2]
                if (age < 12):
                    break
                registration_operation(age, name, vaccinationCentre)
                continue
            elif (registration == 'yes'):
                try: #This is to prevent user enter code that is not registered and crash the program
                    while True:
                        try:
                            patientCode = int(input('What is your ID code: '))
                            break
                        except:
                            print('Please input the right ID code.')

                    read_patient_information = open("patients.txt", "r")
                    allPatientInformation = read_patient_information.readlines() #allPatientInformation is the list of all patients' information
                    read_patient_information.close                  
                    lineInTextFile = int(patientCode) #lineInTextFile is the line number of the patient in the patients.txt file corresponding to the ID code input
                    patientInformation = allPatientInformation[lineInTextFile] #The particular patient's information is extrated out from the list
                    patientNewInformation = patientInformation #The same information is assigned to a new variable to be used later
                    patientInformation = patientInformation.split() #The information of the patient was a string then it is splited to a list
                    patientName = patientInformation [1] #The information in the list is extracted
                    print ('Hello', patientName)
                    registeredVaccine = patientInformation [4]
                    print ('Your vaccine registered is', registeredVaccine)
                    patientStatus = patientInformation [8]
                    print ('Your vaccine status was', patientStatus)

                    patientNewInformation = patientNewInformation.split()
                    #The patient vacccine status were updated
                    if (registeredVaccine == 'EC'):
                        patientNewInformation [8] = 'COMPLETED'
                    elif (patientStatus == 'COMPLETED-D1'):
                        patientNewInformation [8] = 'COMPLETED'
                    elif (patientStatus == 'NEW'):
                        patientNewInformation [8] = 'COMPLETED-D1'
                    elif (patientStatus == 'COMPLETED'):
                        patientNewInformation [8] = 'COMPLETED'

                    read_patient_information = open("patients.txt", "r")
                    patient = read_patient_information.readlines()
                    patientAmount = len(patient) - 1
                    read_patient_information.close()
                    print()
                    #This is to prevent 2 patients information to be continued after another in the text file
                    if (patientAmount != int(patientNewInformation [0])) and (patientNewInformation [8] == 'COMPLETED'):
                        patientNewInformation [8] = 'COMPLETED\n'
                    elif (patientAmount != int(patientNewInformation [0])) and (patientNewInformation [8] == 'COMPLETED-D1'):
                        patientNewInformation [8] = 'COMPLETED-D1\n'

                    allPatientInformation[lineInTextFile] = patientNewInformation #A nested list is created
                    allPatientInformation[lineInTextFile] = ' '.join(allPatientInformation[lineInTextFile]) #The list is joined to let user have a clearer view in the file
                    write_patient_information = open("patients.txt", "w")
                    write_patient_information.writelines(allPatientInformation)
                    write_patient_information.close()
                    print ('='*50)

                    if (patientStatus == 'COMPLETED-D1'):
                        print ("Congratulations, you had completed your vaccine, you don't have to come again.", '\n')
                        input ('Press Enter to continue.') #This is to let the user to have time to look at the information
                        print ('='*50)
                    elif (patientStatus == 'NEW') and (registeredVaccine == 'EC'):
                        print ("Congratulations, you had completed your vaccine, you don't have to come again.", '\n')
                        input ('Press Enter to continue.') #This is to let the user to have time to look at the information
                        print ('='*50)
                    elif (patientStatus == 'NEW') and ((registeredVaccine == 'BV') or (registeredVaccine == 'CZ')):
                        print ('You had completed your first vaccine, please come back in 3 weeks (21 days) to get your second vaccine.', '\n')
                        input ('Press Enter to continue.') #This is to let the user to have time to look at the information
                        print ('='*50)
                    elif (patientStatus == 'NEW') and (registeredVaccine == 'AF'):
                        print ('You had completed your first vaccine, please come back in 2 weeks (14 days) to get your second vaccine.', '\n')
                        input ('Press Enter to continue.') #This is to let the user to have time to look at the information
                        print ('='*50)
                    elif (patientStatus == 'NEW') and (registeredVaccine == 'DM'):
                        print ('You had completed your first vaccine, please come back in 4 weeks (28 days) to get your second vaccine.', '\n')
                        input ('Press Enter to continue.') #This is to let the user to have time to look at the information
                        print ('='*50)
                    elif (patientStatus == 'COMPLETED'):
                        print ('You had already completed your vaccine, why you came?', '\n')
                        input ('Press Enter to continue.') #This is to let the user to have time to look at the information
                        print ('='*50)

                    if (patientStatus == 'NEW'):
                        doseGiven = 'D1'
                    elif (patientStatus == 'COMPLETED-D1'):
                        doseGiven = 'D2'

                    if (patientStatus == 'NEW') or (patientStatus == 'COMPLETED-D1'):
                        record_patient_information = open("vaccination.txt", "a")
                        from datetime import datetime
                        vaccinationTime = datetime.now()
                        vaccinationTime = vaccinationTime.strftime("|%d/%m/%Y||%H:%M:%S|")
                        patientCode = str(patientCode).zfill(4)
                        recordInput = ['\n',patientCode, patientName, registeredVaccine, vaccinationTime, doseGiven]
                        recordInput = ' '.join(recordInput)
                        record_patient_information.write(recordInput)
                        read_patient_information.close()
                    break
                except:
                    print ('Your input code is not registered.')
                    print ('='*50)
                    break

def search_operation ():
        while True:
            try:
                patientCode = int(input('What is your ID code: '))
                break
            except:
                print('Please input the right ID code.')

        try: #This is to prevent user enter code that is not registered and crash the program
            read_patient_information = open("patients.txt", "r")
            allPatientInformation = read_patient_information.readlines()
            read_patient_information.close()
            lineInTextFile = int(patientCode)
            patientInformation = allPatientInformation[lineInTextFile]
            print ('='*50)
            print ('This is the information about the patient.')
            print ('The informations are arranged as sequence below.\n')
            print ('|Code| |Name| |Age| |Vaccine_Centre| |Vaccine_Name| |Dosage_Required| |Contact_No| |E-mail| |Status|')
            print (patientInformation)
            input('Press Enter to continue.') #This is to let the user to have time to look at the information
            print ('='*50)
        except:
            print ('Your input code is not registered.')
            print ('='*50)

def statistics_operation ():
    read_patient_information = open("patients.txt", "r")
    allPatientInformation = read_patient_information.readlines()
    read_patient_information.close()

    VC1Total = 0
    for line in allPatientInformation:
        line = line.split() #nested list is created
        try:
            if (line[3] == 'VC1'):
                VC1Total = VC1Total + 1
        except:
            continue

    VC1Waiting = 0
    for line in allPatientInformation:
        line = line.split() #nested list is created
        try:
            if (line[3] == 'VC1') and (line[8] == 'COMPLETED-D1'):
                VC1Waiting = VC1Waiting + 1
        except:
            continue

    VC1Complete = 0
    for line in allPatientInformation:
        line = line.split() #nested list is created
        try:
            if (line[3] == 'VC1') and (line[8] == 'COMPLETED'):
                VC1Complete = VC1Complete + 1
        except:
            continue

    VC2Total = 0
    for line in allPatientInformation:
        line = line.split() #nested list is created
        try:
            if (line[3] == 'VC2'):
                VC2Total = VC2Total + 1
        except:
            continue

    VC2Waiting = 0
    for line in allPatientInformation:
        line = line.split() #nested list is created
        try:
            if (line[3] == 'VC2') and (line[8] == 'COMPLETED-D1'):
                VC2Waiting = VC2Waiting + 1
        except:
            continue

    VC2Complete = 0
    for line in allPatientInformation:
        line = line.split() #nested list is created
        try:
            if (line[3] == 'VC2') and (line[8] == 'COMPLETED'):
                VC2Complete = VC2Complete + 1
        except:
            continue

    print ('These are the statistics of both vaccinaiton centre.')
    print ('-' * 50)
    print ('vaccination Centre\t\t', 'VC1\t', 'VC2')
    print ('-' * 50)
    print ('Total Patients\t\t\t', VC1Total,'\t', VC2Total,'\t')
    print ('Waiting 2nd Dose Patients\t', VC1Waiting,'\t', VC2Waiting,'\t')
    print ('Completed Patients\t\t', VC1Complete,'\t', VC2Complete,'\t')
    print ('-' * 50)
    input('Press Enter to continue.') #This is to let the user to have time to look at the table
    print ('=' * 50)

def run_application():
    while True:
        operation = welcome_page()
        
        if (operation == 'register'):
            print ('\nYou had chosed registration.')
            ageNameVc = registration_age_name_vc ()
            name = ageNameVc[1]
            age = ageNameVc[0]
            vaccinationCentre = ageNameVc[2]
            if (age < 12):
                continue
            registration_operation(age, name, vaccinationCentre)

        if (operation == 'vaccine'):
            print ('\nYou had chosed vaccine administration.')
            vaccination_operation()

        if (operation == 'search'):
            print ('\nYou had chosed to search for patients record.')
            search_operation()

        if (operation == 'statistics'):
            print ('\nYou had chosed to see patient statistics.')
            statistics_operation()

        if (operation == '0'):
            print ('\nThank you !')
            break

run_application()