import sys
import os
from pathlib import Path
 
dirpath = Path(os.getcwd()).parent
sys.path.insert(0,str(dirpath)+"\\visualize\\")

from progress import cresult


############## Write your logic here ###############



#visualize the result through compare result def 
#Pass the pop_algo1,pop_algo2,pop_algo3 calculating processing time per 100 record
pop_algo1=[]
pop_algo2=[]
pop_algo3=[]
cresult(pop_algo1,pop_algo2,pop_algo3)

