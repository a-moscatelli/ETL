# \python27\scripts\pip install pandas
# \python27\scripts\pip install sqlite3
import pandas
import sqlite3
conn = sqlite3.connect(':memory:')
curs = conn.cursor()
print('importing CSV into DF ...')
dfa = pandas.read_csv( 'C:\\scripts\\' + 'trade_set_dates1.csv')
mindt = dfa['trade_date'].min()
maxdt = dfa['trade_end_date'].max()
print('importing DF into DB ...')
dfa.to_sql('csvi', conn, if_exists='fail')
stmt0='''
create table csvo as
select casex, 999 as curdt
from csvi
where casex>casex
'''
curs.execute(stmt0)
for dt in range(mindt,maxdt):
                dts=str(dt)
                stmt = '''
                insert into csvo(casex,curdt)
                SELECT distinct casex, ? as curdt
                from csvi
                where trade_date < ? and ? < trade_end_date
                '''
                curs.execute(stmt,(dts,dts,dts))
print('exporting DB into DF ...')
dfo1 = pandas.read_sql("select distinct casex, curdt from csvo", con=conn)
stmt2='''
select count(*) as cases, curdt
from (select distinct casex, curdt from csvo)
group by curdt
'''
dfo2 = pandas.read_sql(stmt2, con=conn)
conn.close()
print('exporting DF into CSV ...')
dfo1.to_csv('csvo1.csv',index=False)
dfo2.to_csv('csvo2.csv',index=False)