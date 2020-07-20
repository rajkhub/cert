#Input: 
#gas  = [1,2,3,4,5]
#cost = [3,4,5,1,2]

#Output: 3

#Explanation:
#Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
#Travel to station 4. Your tank = 4 - 1 + 5 = 8
#Travel to station 0. Your tank = 8 - 2 + 1 = 7
#Travel to station 1. Your tank = 7 - 3 + 2 = 6
#Travel to station 2. Your tank = 6 - 4 + 3 = 5
#Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
#Therefore, return 3 as the starting index.


def canCompleteCircuit(self, gas, cost):
    currTank =0 
    pos =0 
    totalGas =0
    totlCost = 0
    for i in range(len(gas)):
        currTank += gas[i] - cost[i]
        totalGas += gas[i]
        totlCost += cost[i]
        
        if currTank <0:
            currTank = 0
            pos = i +1
    if totalGas - totlCost <0:
        return -1
    else:
        return pos



def canCompleteCircuit(self, gas, cost):
    curTank =0
    totalTank =0
    pos=0
    for i in range(len(gas)):
        curTank += gas[i] - cost[i] 
        totalTank += gas[i] - cost[i] 
        
        if curTank <0:
            curTank = 0
            pos = i+1 
        
    if totalTank <0:
        return -1
    else:
        return pos
