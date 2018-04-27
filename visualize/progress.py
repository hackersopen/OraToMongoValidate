import matplotlib
import matplotlib.pyplot as plt
def cresult( str ):
    "This function compares the time per 100 records comparison for n number of records"

    #dummy datas,, Pass the pop_algo1,pop_algo2,pop_algo3 calculating time
    record = [100, 200, 300, 400, 500, 600]
    pop_algo1 = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
    pop_algo2 = [30.48, 52.57, 296.783, 370.133, 400.4, 459.1]
    pop_algo3 = [44.91, 90.09, 108.07, 150.7, 208.5, 370.6]
    plt.plot(record, pop_algo1, color='g')
    plt.plot(record, pop_algo2, color='orange')
    plt.plot(record, pop_algo3, color='red')
    plt.xlabel('Algorithms')
    plt.ylabel('Number of records')
    plt.title('Comparison of the Algorithms')
    plt.show()
    print(str)
    return