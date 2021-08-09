# Settings
#----------------------------------------------------------------------------
 
# Constraints
CON_NOOVERLAP    = True    # AddNoOverlap(machine_to_intervals[machine])
CON_PRECEDENCE   = True    # Add(nexttask.start >= task.end + POST_PROC + TRANSITION)
CON_PINNED       = True    # Add(task.start == PINNED)       
CON_EARLIESTSTART= True    # Add(task.start >= EARLIESSTART)
CON_MAX_DELAY    = True    # Add(nexttask.start <= task.end + POST_PROC + TRANSITION + MAX_DELAY)
CON_DEADLINE     = True    # Add(lasttask.tardiness >= min(0, last_task.end + POST_PROC + TRANSITION - DEADLINE))
CON_PRIORITY     = False   # Add(lasttask.priority >= lasttask.start * PRIO3_GRADIENT + PRIO3_OFFSET)
CON_CAMPAGNE     = False   # Add on the same machine: task.end == nexttask.start; nexttask.work_duration - SETUP
 
# Priority function p= start * gradient + offset
PRIO3            =  3
PRIO3_GRADIENT   =  1
PRIO3_OFFSET     =  0
 
PRIO2            =  2
PRIO2_GRADIENT   =  1
PRIO2_OFFSET     =  100
 
PRIO1            =  1
PRIO1_GRADIENT   =  1
PRIO1_OFFSET     =  200
 
# Penaltiy factors per time unit (0 .. n) for weighting the optimisation target
PENALTY_MAKESPAN =  1
PENALTY_TARDINESS=  1
PENALTY_PRIORITY =  0
 
# Solver parameters
NUM_SEARCH_WORKERS=  8    # 1 .. 8 Cores for parallel work
MAX_SECONDS       =  0    # Setting a time limit for the solver
MAX_SOLUTIONS     =  0    # Stopping a search after a specified number of solutions
 
# Print out
PRN_SOLUTIONS    = True
PRN_STATISTICS   = True
PRN_RESULT       = False
PRN_GRAFIC       = True
PRN_CALENDAR     = True
PRN_UNSATISFIED  = True
