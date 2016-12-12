import math 
import random

def lossprob(cwnd):
	prob =  0.6*(1-math.exp((-cwnd/25)))
	if  (prob >= random.random()):
		return True
	else:
		return False





def cwndsize(incr):
	a = 0.125
	b = 0.25
	cwnd = 10
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
	
	sum=10
	count =0
	for i in range(10,199):
		winprob = lossprob(cwnd)
		
		if (winprob or (Timeout[i] < SampleRTT[i+1])) :
			cwnd = math.floor(cwnd/2)
			count+=1
			#print(cwnd)
			
		else:
			cwnd+=incr
		
	print(count)


def Roundupdate(SampleRTT,EstimatedRTT,DevRTT,Timeout,SampleRTTtemp,a,b):

	
	SampleRTT.append(max(round(SampleRTTtemp,2),40))
	EstimatedRTT.append(round((1-a)*EstimatedRTT[-1]+ a*SampleRTT[-1],2))
	DevRTT.append(round((1-b)*DevRTT[-1] + b*abs(SampleRTT[-1] - EstimatedRTT[-1]),2))
	Timeout.append(round(EstimatedRTT[-1]+ 4*DevRTT[-1],2))
	return EstimatedRTT,SampleRTT,DevRTT,Timeout		




cwndsize(10)
#print(lossprob(200))