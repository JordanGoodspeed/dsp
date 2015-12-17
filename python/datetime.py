from datetime import date

start1 = date(2013, 1, 02)
end1 = date(2013, 7, 28)

delta = end1 - start1
print "%s days" % (delta.days)

from datetime import date

start2 = date(2013, 12, 31)
end2 = date(2015, 5, 28)

delta = end2 - start2
print "%s days" % (delta.days)

from datetime import date

start3 = date(1994, 1, 15)
end3 = date(2015, 7, 14)

delta = end3 - start3
print "%s days" % (delta.days)