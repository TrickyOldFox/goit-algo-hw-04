# Overview
Here you can see the results of series of 4 conducted tests showing the difference in sorting speed.

For each sorting method a random list of n elements was generated and sorted for 10_000 times. This processed was timed with timeit module.


# Results

Results for n - 2:
Insertion Sort: 0.01830670799999999, Merge Sort: 0.022116165999999993, Sorted: 0.015777917000000002

Results for n - 4:
Insertion Sort: 0.025736541, Merge Sort: 0.040064832999999994, Sorted: 0.021085624999999997

Results for n - 8:
Insertion Sort: 0.048816708000000014, Merge Sort: 0.08604187499999999, Sorted: 0.03290725

Results for n - 16:
Insertion Sort: 0.09977329200000001, Merge Sort: 0.17458383300000002, Sorted: 0.05197054099999998

Results for n - 32:
Insertion Sort: 0.26176729199999993, Merge Sort: 0.370886709, Sorted: 0.0905222080000001

Results for n - 64:
Insertion Sort: 0.8125153330000001, Merge Sort: 0.798583458, Sorted: 0.16957287500000007

Results for n - 128:
Insertion Sort: 2.857114208, Merge Sort: 1.7258546250000002, Sorted: 0.32915916699999936

Results for n - 256:
Insertion Sort: 10.669972334, Merge Sort: 3.7310666250000004, Sorted: 0.6530007080000004

Results for n - 512:
Insertion Sort: 43.94911425, Merge Sort: 8.102910332999997, Sorted: 1.4179345419999976

Results for n - 1024:
Insertion Sort: 183.108073041, Merge Sort: 17.55596054099999, Sorted: 2.920903334000002

# Summary
As can be seen from the results table above. Python's build in sorted showed itself as a best one performance-wise in absolute values.

Also, judging by collected data alone, it looks like 'sorted' is a little over linear complexity on chosen sample range, 
whereas Merging and Insertion go almost all the way to n*log(n) and quadratic respectfully.
