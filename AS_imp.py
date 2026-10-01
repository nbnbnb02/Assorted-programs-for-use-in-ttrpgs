
import random


#while above15 > 6:
    #print("Only six rolls dude")
#while sub10 > 6 - above15:
    #print(f"Only {6 - above15} rolls left dude")
    
#while mintot < 0 or mintot > ((6 - sub10)*18 + sub10*9):
    #print("Impossible total given limits")
    
    
def AS(above15,sub10,mintot):
    
    while True: #Rolls
        total_sum = 0
        Roll_list = []

        for R in range(6):
            rolls = [random.randint(1, 6) for _ in range(4)]
            rollR = sum(rolls) - min(rolls)
            # sum  &  list of rolls
            total_sum += rollR
            Roll_list += [ rollR ]
            
        # sort list highest to lowest
        Roll_list.sort(reverse=True)
        #get two highest
        Roll_list_max = []
        if above15 > 0:
            for i in range(0, above15):
                Roll_list_max.append(Roll_list[i])
        else:
            Roll_list_max = [20]
        
        sub10_count = 0
        for i in range(6):
            if Roll_list[i] < 10:
                sub10_count += 1 
        
        if min(Roll_list_max) >= 15 and sub10_count >= sub10:
            if total_sum > mintot:
                roll_res = f"\nRolls : :  {Roll_list}"
                roll_res += f"\nTotal: {total_sum}\n"
                break
    
    return roll_res
    
def AS2(above15,sub10,mintot):
    
    while True: #Rolls
        total_sum = 0
        Roll_list = []

        for R in range(6):
            rolls = [random.randint(1, 6) for _ in range(3)]
            rollR = sum(rolls)
            # sum  &  list of rolls
            total_sum += rollR
            Roll_list += [ rollR ]
            
        # sort list highest to lowest
        Roll_list.sort(reverse=True)
        #get two highest
        Roll_list_max = []
        if above15 > 0:
            for i in range(0, above15):
                Roll_list_max.append(Roll_list[i])
        else:
            Roll_list_max = [20]
        
        sub10_count = 0
        for i in range(6):
            if Roll_list[i] < 10:
                sub10_count += 1 
        
        if min(Roll_list_max) >= 15 and sub10_count >= sub10:
            if total_sum > mintot:
                roll_res = f"\nRolls : :  {Roll_list}"
                roll_res += f"\nTotal: {total_sum}\n"
                break
    
    return roll_res
    
    
if __name__ == "__main__":
    print(AS(2,0,75))
    print(AS2(2,0,75))

        
    
    
