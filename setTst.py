from ADT.linearset import Set

smith = Set()
smith.add( "CSCI-112")
smith.add( "MATH-121")
smith.add( "HIST-340")
smith.add( "ECON-101")

roberts = Set()
roberts.add( "POL-101" )
roberts.add( "ANTH-230" )
roberts.add( "CSCI-112" )
roberts.add( "ECON-101" )

for item in smith:
    print smith


#if smith == roberts:
#    print "Smith and Roberts are taking the same course"
#else:
#    sameCourse = smith.intersect(roberts)
#    if sameCourse.isEmpty():
#        print 'xxxx'
#    else:
#        for item in sameCourse:
#            print item