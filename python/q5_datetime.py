# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

from datetime import date

start1 = date(2013, 1, 02)
end1 = date(2013, 7, 28)

delta1 = end1 - start1
print "%s days" % (delta1.days)

from datetime import date

start2 = date(2013, 12, 31)
end2 = date(2015, 5, 28)

delta2 = end2 - start2
print "%s days" % (delta2.days)

from datetime import date

start3 = date(1994, 1, 15)
end3 = date(2015, 7, 14)

delta3 = end3 - start3
print "%s days" % (delta3.days)