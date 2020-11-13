# average temp in SBA (2019)
# Cameron Braaten

def get_averages(filename):
  print("average temperature of Santa Barbara, CA (2019) in celsius:\n")
  fhandle=open(filename)
  janTemps=[]
  febTemps=[]
  marTemps=[]
  aprilTemps=[]
  mayTemps=[]
  juneTemps=[]
  julyTemps=[]
  augTemps=[]
  sepTemps=[]
  octTemps=[]
  novTemps=[]
  decTemps=[]

  for line in fhandle:
    listitem=list(line.split(','))
    if listitem[-1]!='M\n':
      listitem1 = ' '.join(listitem).replace('\n','').split()
      #print(listitem1)
      temperature=listitem1[-1]
      #print(temperature)
      listitem2=(str(listitem1))
      #print(listitem2[14:16])
      if listitem2[14:16]=="01":
        janTemps.append(temperature)
      elif listitem2[14:16]=="02":
        febTemps.append(temperature)
      elif listitem2[14:16]=="03":
        marTemps.append(temperature)
      elif listitem2[14:16]=="04":
        aprilTemps.append(temperature)
      elif listitem2[14:16]=="05":
        mayTemps.append(temperature)
      elif listitem2[14:16]=="06":
        juneTemps.append(temperature)
      elif listitem2[14:16]=="07":
        julyTemps.append(temperature)
      elif listitem2[14:16]=="08":
        augTemps.append(temperature)
      elif listitem2[14:16]=="09":
        sepTemps.append(temperature)
      elif listitem2[14:16]=="10":
        octTemps.append(temperature)
      elif listitem2[14:16]=="11":
        novTemps.append(temperature)
      elif listitem2[14:16]=="12":
        decTemps.append(temperature)

  jansum=0
  jancount=0

  while(jancount < len(janTemps)):
    jansum = jansum + float(janTemps[jancount])
    jancount += 1
  janaverage=jansum/jancount
  print("january=","{:.2f}".format(janaverage),"\n")

  febsum=0
  febcount=0
  while(febcount < len(febTemps)):
    febsum = febsum + float(febTemps[febcount])
    febcount += 1
  #print(febsum)
  #print(febcount)
  febaverage=(febsum/febcount)
  print("february=","{:.2f}".format(febaverage),"\n")

  marsum=0
  marcount=0
  while(marcount < len(marTemps)):
    marsum = marsum + float(marTemps[marcount])
    marcount += 1
  #print(marsum)
  #print(marcount)
  maraverage=(marsum/marcount)
  print("march=","{:.2f}".format(maraverage),"\n")

  aprsum=0
  aprcount=0
  while(aprcount < len(aprilTemps)):
    aprsum = aprsum + float(aprilTemps[aprcount])
    aprcount += 1
  #print(aprsum)
  #print(aprcount)
  apraverage=(aprsum/aprcount)
  print("april=","{:.2f}".format(apraverage),"\n")

  maysum=0
  maycount=0
  while(maycount < len(mayTemps)):
    maysum = maysum + float(mayTemps[maycount])
    maycount += 1
  #print(maysum)
  #print(maycount)
  mayaverage=(maysum/maycount)
  print("may=","{:.2f}".format(mayaverage),"\n")

  junesum=0
  junecount=0
  while(junecount < len(juneTemps)):
    junesum = junesum + float(juneTemps[junecount])
    junecount += 1
  #print(junesum)
  #print(junecount)
  juneaverage=(junesum/junecount)
  print("june=","{:.2f}".format(juneaverage),"\n")

  julysum=0
  julycount=0
  while(julycount < len(julyTemps)):
    julysum = julysum + float(julyTemps[julycount])
    julycount += 1
  #print(julysum)
  #print(julycount)
  julyaverage=(julysum/julycount)
  print("july=","{:.2f}".format(julyaverage),"\n")

  augsum=0
  augcount=0
  while(augcount < len(augTemps)):
    augsum = augsum + float(augTemps[augcount])
    augcount += 1
  #print(augsum)
  #print(augcount)
  augaverage=(augsum/augcount)
  print("august=","{:.2f}".format(augaverage),"\n")

  sepsum=0
  sepcount=0
  while(sepcount < len(sepTemps)):
    sepsum = sepsum + float(sepTemps[sepcount])
    sepcount += 1
  #print(sepsum)
  #print(sepcount)
  sepaverage=(sepsum/sepcount)
  print("september=","{:.2f}".format(sepaverage),"\n")

  octsum=0
  octcount=0
  while(octcount < len(octTemps)):
    octsum = octsum + float(octTemps[octcount])
    octcount += 1
  #print(octsum)
  #print(octcount)
  octaverage=(octsum/octcount)
  print("october=","{:.2f}".format(octaverage),"\n")

  novsum=0
  novcount=0
  while(novcount < len(novTemps)):
    novsum = novsum + float(novTemps[novcount])
    novcount += 1
  #print(novsum)
  #print(novcount)
  novaverage=(novsum/novcount)
  print("november=","{:.2f}".format(novaverage),"\n")

  decsum=0
  deccount=0
  while(deccount < len(decTemps)):
    decsum = decsum + float(decTemps[deccount])
    deccount += 1
  decaverage=(decsum/deccount)
  print("december=","{:.2f}".format(decaverage),"\n")

get_averages('SBAreal.txt')
