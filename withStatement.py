# No need to use f.close() 
with open('sample.txt','a') as f:
    a=f.write("\nthis is append file")
with open('sample.txt') as f:
    print(f.read())