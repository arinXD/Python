with open("file.txt", encoding = 'utf-8') as f:
  for i in f:
      i=i.strip("\n");
      i=i.split(',');
      print("INSERT INTO register VALUES ('"+"', '".join(i)+"');")
