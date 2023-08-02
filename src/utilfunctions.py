#clamps the num provided between min_value and max_value
def clamp(num, min_value, max_value) -> int:
   return max(min(num, max_value), min_value)

#Validation callback for range input entry field 
def rangeCallback(input) -> bool:
    if input.isdigit():
        return True              
    elif input is "":
        return True
    else:
        return False