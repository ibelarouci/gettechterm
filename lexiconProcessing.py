
import pandas as pandasForSortingCSV
import pandas as pd
import sqlite3
from pattern.text.fr import singularize
from pathlib import Path


def _singularize(plural):
    return singularize(plural)

filename='lexicon'


Path(filename+'.db').touch()
conn = sqlite3.connect(filename+'.db')
c = conn.cursor()
conn.create_function("SINGULARIZE", 1, _singularize)

c.execute("DROP TABLE IF EXISTS rawterms")
c.execute('''CREATE TABLE IF NOT EXISTS rawterms (id INTEGER PRIMARY KEY AUTOINCREMENT, term text, nb_occu int,branch text )''')


lexicon = pd.read_csv(filename+'.csv',delimiter=";")
# write the data to a sqlite table
#c.execute('''delete from rawterms''')
#c.execute("UPDATE sqlite_sequence SET  seq = 0 WHERE name= 'rawterms' ")
lexicon.to_sql('rawterms', conn, if_exists='append', index = False)

print("Database Created "+ filename+'.db')
print("nb records: "+str(c.execute('''SELECT count(*) FROM rawterms''').fetchall()))


sqlQuery ="update rawterms set term =SINGULARIZE(term)"
c.execute(sqlQuery)
conn.commit()


c.execute("DROP TABLE IF EXISTS techterms")
c.execute(''' CREATE TABLE IF NOT EXISTS techterms (id INTEGER PRIMARY KEY AUTOINCREMENT, term text,nb int, techrate int)''')
#c.execute('''delete from techterms''')
#c.execute("UPDATE sqlite_sequence SET  seq = 0 WHERE name= 'techterms' ")



sqlQuery = """ insert into techterms (term,nb,techrate)
SELECT t.term ,sum(nb) ,1.0*(max(nb)+min(nb))/(2*sum(nb)) techrate
FROM 
(
SELECT r.term, r.branch, sum (r.nb_occu) nb
from rawterms r 
group by r.term ,r.branch ) t 
GROUP BY t.term 
order by t.term """
c.execute(sqlQuery)
print("table techterms Created ")
print("nb records: "+str(c.execute('''SELECT count(*) FROM techterms''').fetchall()))

conn.commit()
db_df = pd.read_sql_query("SELECT * FROM techterms", conn)
db_df.to_csv('techterms.csv', index=False)



""" 
# assign dataset
csvData = pandasForSortingCSV.read_csv("fpdict.csv",delimiter=";",header=None)

  
# sort data frame
csvData.sort_values(csvData.columns[1], 
                    axis=0,
                    ascending=[True], 
                    inplace=True)
  
# displaying sorted data frame
print("\nAfter sorting:")
print(csvData)



#csvData.loc[0][2]
data_sum = 0
y=0
lines=""
for i in range(len(csvData)-1):
  
    if(csvData.iloc[i][1]!=csvData.iloc[i+1][1]):
        data_sum = data_sum+ csvData.iloc[i][2]
        #print(csvData.iloc[i][1]+" "+str(data_sum))
        y=y+1
        print(y)
        lines=lines+str(y)+";"+csvData.iloc[i][1]+";"+str(data_sum)+"\n"
        data_sum=0
    else : 
        data_sum=data_sum+csvData.iloc[i][2]
       # print(csvData.loc[i][1]+" "+str(data_sum))

text_file = open("LexiconWords.csv", "w")
for line in lines:
   text_file.write(line)
text_file.close()
         """
