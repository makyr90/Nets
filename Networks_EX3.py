import random
import csv
import os

def RTTsimulation(a,b):
	#random.seed(156)
 #1st round
	SampleRTT = [100]
	EstimatedRTT = [100]
	DevRTT = [0]
	Timeout = [100]
	optionslist = [1,2,3,4]
	jump = False
	for i in range(1,200):
		
		if (jump):
			jump = False
			continue

		x = random.uniform(0.7,1.3)
		y = random.uniform(-10,35)
		if (i<20 or ((i-20)%5!=0)):
			SampleRTTtemp =x*SampleRTT[-1] + y
					
		else:
			choice = random.choice(optionslist)
			if  choice == 1:
				SampleRTTtemp = 1.85*SampleRTT[-1] 
			elif choice == 2:
				SampleRTTtemp = 0.65*SampleRTT[-1] 
			elif choice == 3:
				SampleRTTtemp = 1.6*SampleRTT[-1] 
				SampleRTTtemp2 = 0.7*SampleRTTtemp
				EstimatedRTT,SampleRTT,DevRTT,Timeout = Roundupdate(SampleRTT,EstimatedRTT,DevRTT,Timeout,SampleRTTtemp,a,b) 
				EstimatedRTT,SampleRTT,DevRTT,Timeout = Roundupdate(SampleRTT,EstimatedRTT,DevRTT,Timeout,SampleRTTtemp2,a,b) 
				jump = True
				continue
			else:
				SampleRTTtemp = x*SampleRTT[-1] + y

		
		EstimatedRTT,SampleRTT,DevRTT,Timeout = Roundupdate(SampleRTT,EstimatedRTT,DevRTT,Timeout,SampleRTTtemp,a,b) 
	#Part1
	sum = 0
	for i in range(20,199):
		if (Timeout[i] < SampleRTT[i+1]):
			sum+=1
	return(sum)
	#Part 2
	#return Timeout,SampleRTT

	



def Roundupdate(SampleRTT,EstimatedRTT,DevRTT,Timeout,SampleRTTtemp,a,b):

	
	SampleRTT.append(max(round(SampleRTTtemp,2),40))
	EstimatedRTT.append(round((1-a)*EstimatedRTT[-1]+ a*SampleRTT[-1],2))
	DevRTT.append(round((1-b)*DevRTT[-1] + b*abs(SampleRTT[-1] - EstimatedRTT[-1]),2))
	Timeout.append(round(EstimatedRTT[-1]+ 4*DevRTT[-1],2))
	return EstimatedRTT,SampleRTT,DevRTT,Timeout			


#Part1
Seeds =[1234,5678,1011,1213,1415] 

a = 0.125
b = 0.125
sum=0
for i in range(5):
	retransmissions = RTTsimulation(a,b)
	sum+=retransmissions
	random.seed(Seeds[i])
	print("Set "+str(i)+" with alpha= "+str(a)+ " and beta= "+str(b) +" #Retransmissions = "+str(retransmissions))
print("Average #Retransmissions = "+str(sum/5))
 
print("--------------------------------------------------------------------------------")

a = 0.125
b = 0.25
sum=0
for i in range(5):
	retransmissions = RTTsimulation(a,b)
	sum+=retransmissions
	random.seed(Seeds[i])
	print("Set "+str(i)+" with alpha= "+str(a)+ " and beta= "+str(b) +" #Retransmissions = "+str(retransmissions))
print("Average #Retransmissions = "+str(sum/5))
print("--------------------------------------------------------------------------------")


a = 0.125
b = 0.375
sum=0
for i in range(5):
	retransmissions = RTTsimulation(a,b)
	sum+=retransmissions
	random.seed(Seeds[i])
	print("Set "+str(i)+" with alpha= "+str(a)+ " and beta= "+str(b) +" #Retransmissions = "+str(retransmissions))
print("Average #Retransmissions = "+str(sum/5))
print("--------------------------------------------------------------------------------")




a = 0.4
b = 0.25
sum=0
for i in range(5):
	retransmissions = RTTsimulation(a,b)
	sum+=retransmissions
	random.seed(Seeds[i])
	print("Set "+str(i)+" with alpha= "+str(a)+ " and beta= "+str(b) +" #Retransmissions = "+str(retransmissions))
print("Average #Retransmissions = "+str(sum/5))
 
print("--------------------------------------------------------------------------------")

a = 0.125
b = 0.25
sum=0
for i in range(5):
	retransmissions = RTTsimulation(a,b)
	sum+=retransmissions
	random.seed(Seeds[i])
	print("Set "+str(i)+" with alpha= "+str(a)+ " and beta= "+str(b) +" #Retransmissions = "+str(retransmissions))
print("Average #Retransmissions = "+str(sum/5))
print("--------------------------------------------------------------------------------")


a = 0.25
b = 0.25
sum=0
for i in range(5):
	retransmissions = RTTsimulation(a,b)
	sum+=retransmissions
	random.seed(Seeds[i])
	print("Set "+str(i)+" with alpha= "+str(a)+ " and beta= "+str(b) +" #Retransmissions = "+str(retransmissions))
print("Average #Retransmissions = "+str(sum/5))
print("--------------------------------------------------------------------------------")

#Part 2

# wdir = "C:\\Users\\Manolis\\Desktop\\Networks"
# os.chdir(wdir)
# f = open("a0125b0375.csv", 'wt', newline='')
# random.seed(1234)
# Timeout,SampleRTT = RTTsimulation(0.125,0.375)

# try:
#     writer = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow( ('n', 'Timeoutinterval(n-1)', 'SampleRTT(n)',"Succes") )
#     for i in range(99,199):
#         writer.writerow( (i+2, Timeout[i-1], SampleRTT[i],int(Timeout[i-1]>SampleRTT[i]) ))
# finally:
#     f.close()
