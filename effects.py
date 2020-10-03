# *******************************************************
# Ege Ozguroglu (eo2464)
# effects file (includes obect_filter,shades_of_gray, horizontal_flip, 
# and additional helper functions.)
# Midterm
# ENGI E1006
# *******************************************************
import statistics as stat

def object_filter(infile1, infile2, infile3, outfile):
    """ filters images """
    
#   inputs: infile1, infile2, infile3
#    open infile 1, infile2, and infile 3 for reading.
#    open outfile for writing, name already inputted in tester.
    
    file1 = open(infile1, "r")
    file2 = open(infile2, "r")
    file3 = open(infile3, "r")
    out  = open(outfile, "w")
    
    #read metadata to get to actual data.
    type_ppm, xdim, ydim, max_value = read_metadata(file1)
    type_ppm, xdim, ydim, max_value = read_metadata(file2)
    type_ppm, xdim, ydim, max_value = read_metadata(file3)
    line1 = file1.readline()
    line2 = file2.readline()
    line3 = file3.readline()
    
    out.write(str(type_ppm))
    out.write('{} {}'.format(str(ydim), str(xdim)))
    out.write("\n")
    out.write(str(max_value))
    
    #read_metadata function needs to be defined!!! get xdim ydim max value. then get to the actual color values.
    #what it's doing? in order to get to actual image data, skip the metadata lines.
    # we're using it to skip line. we don't actually read the metadata. 
    
    #takes string that was just read and splits with white spaces it into a list.
    while (len(line1)>0):
        line1_list = line1.split()
        line2_list = line2.split()
        line3_list = line3.split()
         #iterate over the values over the length of line1_list,
         #assuming that line2_list and line3_list have the same dimensions.
        for i in range(len(line1_list)):
            list_combined = []
            list_combined.append(line1_list[i])
            list_combined.append(line2_list[i])
            list_combined.append(line3_list[i])
            out.write(stat.mode(list_combined))
            out.write(" ") #adds white space to seperate values from each other. 
        out.write("\n") #after iterating over the entire line, write a new line character. 
       
        line1 = file1.readline()  #when done iterating over the list, get the next line.    
        line2 = file2.readline()
        line3 = file3.readline()
        #the readline method by default reads the next line in its subsequent implementation. 
        
    file1.close()
    file2.close()
    file3.close()
    out.close()

def shades_of_gray(infile, outfile):
    """ converts images to grayscale """
    file1 = open(infile, "r")
    out = open(outfile, "w")
    
    type_ppm, xdim, ydim, max_value = read_metadata(file1)
    line = file1.readline()
    
    out.write(str(type_ppm))
    out.write('{} {}'.format(str(ydim), str(xdim)))
    out.write("\n")
    out.write(str(max_value))

    while (len(line)>0):
        line_list = line.split()
        i = 0
        while i < len(line_list) - 2:
            out.write(str(int((int(line_list[i])+int(line_list[i+1])+int(line_list[i+2]))/3)))
            out.write(" ")
            out.write(str(int((int(line_list[i])+int(line_list[i+1])+int(line_list[i+2]))/3)))
            out.write(" ")
            out.write(str(int((int(line_list[i])+int(line_list[i+1])+int(line_list[i+2]))/3)))
            out.write(" ")
            i = i + 3
        out.write("\n")
        
        line = file1.readline()
        
    file1.close()
    out.close()
   
def horizontal_flip(infile, outfile): #inputs: infile, outfile.
    """horizontally flips the images"""
    
    file1 = open(infile, "r") #open infile for reading.
    out = open(outfile, "w") #open outfile for writing.
    type_ppm, xdim, ydim, max_value = read_metadata(file1)
    
    out.write(str(type_ppm))
    out.write('{} {}'.format(str(ydim), str(xdim)))
    out.write("\n")
    out.write(str(max_value))
    
    image=file1.readlines()
    columns=int(ydim)
    rows=int(xdim)
    cleaned=[['000' for j in range(0,3*columns)]for i in range(0, rows)] 
    i=0
    j=0
    for row in image:
        elements=row.strip().split(' ')
        for itemm in elements:
            item=itemm.strip();
            if (not (item=='' or i>=rows or j>=3*columns)):
                cleaned[i][j]=item;
                j+=1;
                if (j==3*columns):
                    j=0;
                    i+=1
    file1.close();
    for i in range(0,rows):
        for j in range(0,columns):
            out.write(' '+str(cleaned[i][3*(columns-j-1)]))
            out.write(' '+str(cleaned[i][3*(columns-j-1)+1]))
            out.write(' '+str(cleaned[i][3*(columns-j-1)+2]))
        out.write('\n')
    out.close() 
        
    file1.close()
    out.close()

def read_metadata(file):

    #put the type of ppm in the first line into list type_ppm.
    type_ppm = file.readline()
    
    #put the x and y dimensions into lists xdim and y_dim.
    dimensions = file.readline()
    dimensions_list = dimensions.split()
    xdim =  dimensions_list[1]
    ydim =  dimensions_list[0]

    #put the max color value in the first line into list max_value.
    max_value = file.readline()
    
    return type_ppm, xdim, ydim, max_value














