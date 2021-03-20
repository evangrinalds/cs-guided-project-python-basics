def csRaindrops(number):
  ret_string = ""
  
  mod3 = number % 3
  mod5 = number % 5
  mod7 = number % 7
  
  if mod3 > 0 and mod5 > 0 and mod7 > 0:
    return str(number)
  
  if mod3 == 0:
    ret_string += "Pling"
  
  if mod5 == 0:
    ret_string += "Plang"
   
  if mod7 == 0:
    ret_string += "Plong"
    
  return ret_string
