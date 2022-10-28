def p12():
  Dr_set = {'Jeffy', 'David', 'Ted'} 
  namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
  titlednamelist =  [i if i not in Dr_set else 'Dr. '+i for i in namelist]
  #Expected Ans -> titlednamelist = ['kitty', 'Hinton', 'Jack', 'Dr. Ted', 'Bahab', 'Cebul', 'Dr. David', 'Koller']
  return titlednamelist