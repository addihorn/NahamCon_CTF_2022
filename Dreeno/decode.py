f = open("output.txt", "r")
output = ""
for line in f:
  newline = ""
  for i, v in enumerate(line):
  
    newflag = ''
    if(i in [1,3,5,7]):
      if v=='1':
        newflag='0'
      else:
        newflag='1'
    else:
      newflag=v

    newline += newflag

  output += chr(int(newline,2))
  
f.close()
print(output)