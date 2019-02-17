# Government History of Turkey
# parties list contain Turkish parties  and dates are active years in the politics, so these dates' indexes are exactly mapped to parties list.

parties = ["AKP", "ANAP", "AP", "B", "CGP", "CHF", "CHP", "CKMP", "DP", "DSP",\
           "DTP", "DYP","HDP", "MGP", "MHP", "MP","MSP", "RP", "SHP", "YTP"]

dates = [["2002-2019"],\
         ["1983-1991", "1996-1996", "1997-1999", "1999-2002"],\
         ["1961-1962", "1965-1974", "1975-1977", "1977-1978", "1979-1980"],\
         ["1963-1965", "1971-1974", "1978-1979", "2015-2015"],\
         ["1973-1974", "1975-1977", "1978-1979"],\
         ["1923-1935"],\
         ["1935-1950", "1971-1973", "1974-1974", "1977-1977", "1978-1979", "1995-1996"],\
         ["1962-1963", "1965-1965"],\
         ["1950-1960"],\
         ["1997-2002"],\
         ["1997-1999"],\
         ["1991-1997", "1996-1997"],\
         ["2015-2015"],\
         ["1971-1973"],\
         ["1975-1977", "1977-1978", "1999-2002"],\
         ["1965-1965"],\
         ["1974-1974", "1975-1977", "1977-1978"],\
         ["1996-1997"],\
         ["1991-1995"],\
         ["1962-1963", "1965-1965"]]

party = input("Enter a party name:")

if party in parties:
  for i in range(len(parties)):
    if parties[i] == party:
      index = i  
  terms = dates[index]
  total = 0
  print("Start Year - End Year: ")
  for term in terms:
    startYear = term[:4]
    endYear = term[-4:]
    print(startYear,"-",endYear)
    current = int(endYear) - int(startYear) + 1 # i.e 1965-1965 counts one year, 1991-1995 counts 5 years, so we need to add additional year.
    total += current
  print("Total:", total, "year(s)")
else:
  print("There is no such party!")
  
