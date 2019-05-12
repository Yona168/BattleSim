from features import run
from sys import argv
run.run_tests('json' if len(argv)==1 else argv[1],False)
