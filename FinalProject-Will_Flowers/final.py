
#Will Flowers
#Final Project



#Import Modules as needed
import numpy as np
import matplotlib.pyplot as plt
import math
import array
from scipy import stats

#Open a file results, to write in
e = open('results.csv', 'w')
e.close()
#Define a function to read data from files and give back certain columns of data
def avg_temp(filename):
    

    # open file to read
    with open(filename, 'r') as f, open('results.csv', 'a') as w:
    
        average_temp = []
        average_high_temp = []
        average_low_temp = []
        average_precip = []
        
       
        columns = []
        #for each line in f,split the line into a list of values
        for i in f:
            a = i.split(',')
            
        #for each item in the list, strip of components and print into a new list
            for j in a:
                j.strip('G*H')
            columns.append(a)
        
    #Append only certain 'columns' of data
        for t in columns:
            if t[3]:
                average_temp.append(t[3])
            if t[17]:
                average_high_temp.append(t[17])
            if t[18]:
                average_low_temp.append(t[18])
            if t[19]:
                average_precip.append(t[19])
                
        del average_temp[0] #Get rid of the headers in columns
        del average_high_temp[0]
        del average_low_temp[0]
        del average_precip[0]
        
        
        
        float_average_temp = []
        float_average_high_temp = []
        float_average_low_temp = []
        float_average_precip = []
        
        #make floating point
        for k in average_temp:
            float_average_temp.append(float(k))
     
        for l in average_high_temp:
            float_average_high_temp.append(float(l.strip('*')))
    
        for k in average_low_temp:
            float_average_low_temp.append(float(k.strip('*')))
            
        for k in average_precip: 
            float_average_precip.append(float(k.strip('*GHIABCDE')))
            
        #Compute mean
        number1 = len(average_temp)
        sum1 = math.fsum(float_average_temp)
        average1 = round(sum1/number1,2)
        
        number2 = len(average_high_temp)
        sum2 = math.fsum(float_average_high_temp)
        average2 = round(sum2/number2,2)
        
        number3 = len(average_low_temp)
        sum3 = math.fsum(float_average_low_temp)
        average3 = round(sum3/number3,2)
        
        number4 = len(average_precip)
        sum4 = math.fsum(float_average_precip)
        average4 = round(sum4,2)
        
        
        
        #Write to file called results, the results , keeping float
        w.write('%g, %g, %g, %g\n' % (average1, average2, average3, average4))
        
    
        

#Use a for loop to go through all files of data to be extracted
for i in range(1982,2013,1):
    avg_temp('%d.csv' % i)
   
    
#Open old file to extract data, and new file to write results in
with open('results.csv','r') as g,open('finalresults.txt', 'w') as v:
    average_all_temp = []
    average_all_high_temp = []
    average_all_low_temp = []
    average_all_precip = []
    
   
    columns = []
    #for each line in f,split the line into a list of values
    for i in g:
        a = i.split(',')
        
    #for each item in the list, strip of components and print into a new list
        for j in a:
            j.strip()
        columns.append(a)
    
#Bring in the numbers by columns
    for t in columns:
        if t[0]:
            average_all_temp.append(t[0])
        if t[1]:
            average_all_high_temp.append(t[1])
        if t[2]:
            average_all_low_temp.append(t[2])
        if t[3]:
            average_all_precip.append(t[3])

#make the list floating numbers to do calculation on them
        float_average_all_temp = []
        float_average_all_high_temp = []
        float_average_all_low_temp = []
        float_average_all_precip = []
        
        for k in average_all_temp:
            float_average_all_temp.append(float(k))
     
        for l in average_all_high_temp:
            float_average_all_high_temp.append(float(l))
    
        for k in average_all_low_temp:
            float_average_all_low_temp.append(float(k))
            
        for k in average_all_precip: 
            float_average_all_precip.append(float(k))
            
    #Convert to arrays, to do calculations
    array1 = float_average_all_temp
    array2 = float_average_all_high_temp
    array3 = float_average_all_low_temp
    array4 = float_average_all_precip
    #Calculate mean
    mean1 = np.mean(array1)
    mean2 = np.mean(array2)
    mean3 = np.mean(array3)
    mean4 = np.mean(array4)
    #Calculate median
    median1 = np.median(array1)
    median2 = np.median(array2)
    median3 = np.median(array3)
    median4 = np.median(array4)
    #Calculate standard deviation
    sd1 = np.std(array1)
    sd2 = np.std(array2)
    sd3 = np.std(array3)
    sd4 = np.std(array4)
    #Calculate variance
    var1 = np.var(array1)
    var2 = np.var(array2)
    var3 = np.var(array3)
    var4 = np.var(array4)
    #Calculate max
    max1 = np.amax(array1)
    max2 = np.amax(array2)
    max3 = np.amax(array3)
    max4 = np.amax(array4)
    
    #Calculate min
    min1 = np.amin(array1)
    min2 = np.amin(array2)
    min3 = np.amin(array3)
    min4 = np.amin(array4)
    
    #See how much correlation between precipitation and mean temperature
    corr1 = np.corrcoef(array1,array4)
    corr = corr1[1][0]
    
    #Write these results to a new file 'final results'.  **These results will not show in the file, results until the graphs created have been closed**
    v.write('This is the mean,median,max,min,standard deviation, and variance of the average temperature in the Raleigh/Durham area over the last 30 years respectively:\n %g, %g, %g, %g %g, %g\n\n' % (mean1, median1, max1, min1, sd1, var1))
    v.write('This is the mean,median,max,min,standard deviation, and variance of the average high temperatures in the Raleigh/Durham area over the last 30 years respectively:\n %g, %g, %g %g, %g, %g\n\n' % (mean2, median2, max2, min2, sd2, var2))
    v.write('This is the mean,median,max,min,standard deviation, and variance of the average low temperatures in the Raleigh/Durham area over the last 30 years respectively:\n %g, %g, %g %g, %g, %g\n\n' % (mean3, median3, max3, min3, sd3, var3))
    v.write('This is the mean,median,max,min,standard deviation, and variance of the average precipitation in the Raleigh/Durham area over the last 30 years respectively:\n %g, %g,%g, %g %g, %g\n\n' % (mean4, median4, max4, min4, sd4, var4))
    v.write('This is correlation coefficient between yearly average temperatures, and yearly average precipitation:\n %g' % corr)

    
#Graph results
    x = np.arange(1982,2013)
    y1 = array1
    y2 = array2
    y3 = array3
    y4 = array4
    
    plt.plot(x,y1, color = 'g', linestyle = '-', marker = 'o', label = 'average temp')
    plt.plot(x,y2, color = 'r', linestyle = '--', marker = '8', label = 'average high temp')
    plt.plot(x,y3, color = 'b', linestyle = '-', marker = 'o', label = 'average low temp')
    
    plt.legend(loc = 1)
    
    plt.axis([1982, 2013, 0, 130])
    plt.xlabel('years', fontsize = 16, color = 'b')
    plt.ylabel('temperature(Fahrenheit)', fontsize = 16, color = 'b')
    plt.title('Average Temperature between years 1982-2012, in Raleigh, NC', fontsize = 16, color = 'r')
    plt.show()
#Make a sub-plot that shows a scatter plot to show correlation between average temperature and precipitation
#And a plot of the yearly precipitation
    plt.subplot(2,1,1)
    plt.scatter(y1,y4, s = 18, c = 'k', marker = 'o')
    plt.axis([55, 65, 30, 60])
    plt.xlabel('Average Temperature(F)')
    plt.ylabel('Average Precipitation per year(Inches)')
    plt.title('Average Temperature vs. Average precipitation per year')
    
    plt.subplot(2,1,2)
    plt.plot(x, y4)
    plt.xlabel('Years')
    plt.ylabel('Amount of Rain')
    plt.show()
    
    
    
#End of code

