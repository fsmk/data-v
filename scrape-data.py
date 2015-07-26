import csv
femaleCount =0
maleCount =0
hardwareCount=0
sysadCount =0
androidCount = 0

firstYears = 0 
secondYears=0
thirdYears=0 
fourthYears=0


with open('data-fsmk.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if(row['Gender'].lower()=='female'):
		        femaleCount+=1
		if(row['Gender'].lower()=='male'):
		        maleCount+=1 
		if(row['Track']=='hardware'):
			hardwareCount+=1; 
		if(row['Track']=='sysad'):
			sysadCount+=1; 
		if(row['Track']=='android'):
			androidCount+=1;

		if(row['Sem']=='1' or row['Sem']=='2' or row['Sem']=='3'):
			firstYears+=1

		if(row['Sem']=='4' or row['Sem']=='5'):
			secondYears+=1

		if(row['Sem']=='6' or row['Sem']=='7'):
			thirdYears+=1
		
		if(row['Sem']=='8' or row['Sem']==' '):
			fourthYears+=1				 		              	
		        

print "femaleCount = "
print femaleCount

print "maleCount = "
print maleCount

print "hardwareCount = "
print hardwareCount

print "androidCount ="
print androidCount

print "sysadCount ="
print sysadCount

print "firstYears"
print firstYears


print "secondYears"
print secondYears

print "thirdYears"
print thirdYears

print "fourthYears"
print fourthYears