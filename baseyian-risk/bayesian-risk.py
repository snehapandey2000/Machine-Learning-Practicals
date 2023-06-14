# w1 covid, 
# w2 non-covid

p_w1 = int(input("Enter a priori percentage of covid patients : "))/100
p_w2 = int(input("Enter a priori percentage of non covid patients : "))/100

print("p_w1 = ",p_w1)
print("p_w2 = ",p_w2)

# loss matrix
# a1(alpha1) = medication
# a2(alpha2) = non-medication

a1 = "medication"
a2 = "non-medication"

print("")
print("a1 = ",a1)
print("a2 = ",a2)
print("")

# Action      w1                  w2
# a1          l11(lambda11)       l12
# a2          l21                 l22

print("")
print("Loss Matrix ")


print("For action alpha1 i.e. medication")
lossMatrix_11 = int(input("Enter loss value for w1 i.e. Covid : "))
lossMatrix_12 = int(input("Enter loss value for w2 i.e. Non-Covid : "))

print("")
print("For action alpha2 i.e. non-medication")
lossMatrix_21 = int(input("Enter loss value for w1 i.e. Covid : "))
lossMatrix_22 = int(input("Enter loss value for w2 i.e. Non-Covid :"))


print("So loss mtrix is :")
print(lossMatrix_11, lossMatrix_12)
print(lossMatrix_21, lossMatrix_22)
print("")



def getBayesianRiskOptimalAction():
    R_a1 = (lossMatrix_11 * p_w1) + (lossMatrix_12 * p_w2)

    R_a2 = (lossMatrix_21 * p_w1) + (lossMatrix_22 * p_w2)
    
    print("")
    print("R_a1 = ",R_a1)
    print("R_a2 = ",R_a2)
    print("")
    
    if(R_a1 < R_a2):
        return a1
    else:
        return a2
        
 


def getConditionalRiskOptimalAction():
    print("Class conditional probability table:")
    
    # x1 = +ve blood test sample
    # x2 = -ve blood test sample
    
    print("For blood test sample +ve i.e. x1")
    p_x1_by_w1 = int(input("Enter percentage value for w1 i.e. Covid : "))/100
    p_x1_by_w2 = int(input("Enter percentage value for w2 i.e. Non-Covid : "))/100
    
    print("")
    print("For blood test sample -ve i.e. x2")
    p_x2_by_w1 = int(input("Enter percentage value for w1 i.e. Covid : "))/100
    p_x2_by_w2 = int(input("Enter percentage value for w2 i.e. Non-Covid :"))/100
    
    print("")
    # for x1
    R_a1_by_x1 = lossMatrix_11 * (p_x1_by_w1 * p_w1) + lossMatrix_12 * (p_x1_by_w2 * p_w2)
    R_a2_by_x1 = lossMatrix_21 * (p_x1_by_w1 * p_w1) + lossMatrix_22 * (p_x1_by_w2 * p_w2)
    
    print("R_a1_by_x1 = ",R_a1_by_x1)
    print("R_a2_by_x1 = ",R_a2_by_x1)
    
    x1_optimal_action = ""
    if(R_a1_by_x1 < R_a2_by_x1):
        x1_optimal_action = a1
    else:
        x1_optimal_action = a2
    
    print("For x1 (+ve blood test sample), optimal action = ", x1_optimal_action)
    print("")
    
    
    # for x2
    R_a1_by_x2 = lossMatrix_11 * (p_x2_by_w1 * p_w1) + lossMatrix_12 * (p_x2_by_w2 * p_w2)
    R_a2_by_x2 = lossMatrix_21 * (p_x2_by_w1 * p_w1) + lossMatrix_22 * (p_x2_by_w2 * p_w2)
    
    print("R_a1_by_x2 = ",R_a1_by_x2)
    print("R_a2_by_x2 = ",R_a2_by_x2)
    
    x2_optimal_action = ""
    if(R_a1_by_x2 < R_a2_by_x2):
        x2_optimal_action = a1
    else:
        x2_optimal_action = a2
    
    print("For x2 (-ve blood test sample), optimal action = ", x2_optimal_action)



print("Bayesian Risk")
print(getBayesianRiskOptimalAction(), " is the optimal action")

print("")
print("-------------------------------------------------------------------------------")
print("")

print("Conditional Risk")
getConditionalRiskOptimalAction()

'''
20
80
0
10
20
0
'''

'''
90
10
10
90
'''